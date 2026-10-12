"""Check Skill packaging and documented flags; optionally run help only."""

import argparse
import hashlib
import json
import re
import shlex
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def example_flags(text, name):
    flags = set()
    for block in re.findall(r"```bash\n(.*?)\n```", text, re.S):
        for line in block.splitlines():
            argv = shlex.split(line)
            require(argv and argv[0] == name, f"{name}: unexpected example command")
            require(not any(x in argv for x in ["|", ";", "&&", "||"]),
                    f"{name}: shell composition needs separate review")
            flags.update(x for x in argv[1:] if re.fullmatch(r"--?[a-zA-Z][a-zA-Z0-9-]*", x))
    require(flags, f"{name}: no CLI examples")
    return flags


def validate(lock_path=None, source_cache=None, tools_root=None, platform=None, help_output=None):
    catalog = read_json(ROOT / "catalog/tool-coverage.json")
    provenance = read_json(ROOT / "catalog/verification-sources.json")["tools"]
    tools = catalog["tools"]
    names = {t["name"] for t in tools}
    require(len(names) == len(tools) == 8, "expected eight unique tools")
    require({p.name for p in (ROOT / "skills").iterdir() if p.is_dir()} == names,
            "Skill directories differ from coverage table")
    if lock_path:
        raw = lock_path.read_bytes()
        require(hashlib.sha256(raw).hexdigest() == catalog["lock_source"]["sha256"],
                "lock snapshot changed; review tool versions before changing the baseline")
        locked = {t["name"]: t for t in json.loads(raw)["tools"]}
        require(set(locked) == names, "lock inventory differs")
        for t in tools:
            row = locked[t["name"]]
            require(row["version"] == t["tool_version"] and sorted(row["assets"]) == t["platforms"],
                    f"{t['name']}: version/platform drift")
    installed = {}
    if tools_root:
        require(platform is not None, "--platform is required with --tools-root")
        require(help_output is not None, "--help-output is required with --tools-root")
        installed = {t["name"]: t for t in read_json(tools_root / "manifest.json")["tools"]}
        expected = {t["name"] for t in tools if platform in t["platforms"]}
        require(set(installed) == expected, "installed platform inventory differs")
        help_output.mkdir(parents=True, exist_ok=True)
    for t in tools:
        name = t["name"]
        folder = ROOT / "skills" / name
        text = (folder / "SKILL.md").read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
        require(match is not None, f"{name}: missing frontmatter")
        # Deliberately support only our simple scalar headers, not a partial YAML parser.
        head = dict(line.split(": ", 1) for line in match[1].splitlines())
        require(head.get("name") == name and head.get("description") and head.get("license"),
                f"{name}: invalid metadata")
        require(t["tool_version"] in text, f"{name}: missing version statement")
        for md in folder.rglob("*.md"):
            for link in re.findall(r"\]\(([^)]+)\)", md.read_text(encoding="utf-8")):
                if "://" in link or link.startswith("#"):
                    continue
                target = (md.parent / link.split("#")[0]).resolve()
                require(target.is_relative_to(folder.resolve()) and target.is_file(),
                        f"{name}: missing or non-self-contained reference {link}")
        flags = example_flags(text, name)
        source = provenance[name]
        require(re.fullmatch(r"[a-f0-9]{40}", source["commit"]), f"{name}: unpinned source")
        for file in source["files"]:
            require(f"/blob/{source['commit']}/" in file["url"], f"{name}: moving source URL")
        if source_cache:
            code = []
            for file in source["files"]:
                raw = (source_cache / name / file["path"]).read_bytes()
                require(hashlib.sha256(raw).hexdigest() == file["sha256"],
                        f"{name}: source hash mismatch: {file['path']}")
                code.append(raw.decode("utf-8"))
            all_code = "\n".join(code)
            for flag in flags:
                token = flag.lstrip("-")
                require(f'"{token}"' in all_code, f"{name}: example flag absent from reviewed source: {flag}")
        if name in installed:
            entry = installed[name]
            binary = (tools_root / entry["path"]).resolve()
            require(binary.is_relative_to(tools_root.resolve()), f"{name}: invalid binary path")
            require(entry["version"] == t["tool_version"] and entry["platform"] == platform,
                    f"{name}: installed version/platform mismatch")
            require(hashlib.sha256(binary.read_bytes()).hexdigest() == entry["sha256"],
                    f"{name}: installed binary changed")
            # Never execute the examples: help has no target, template or wordlist.
            result = subprocess.run([str(binary), "-help" if name == "fscan" else "-h"],
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=30)
            output = result.stdout.decode("utf-8", errors="replace")
            (help_output / (name + ".txt")).write_text(output, encoding="utf-8")
            require(result.returncode == 0, f"{name}: help exited {result.returncode}")
            for flag in flags:
                require(re.search(r"(?<![\w-])-{1,2}" + re.escape(flag.lstrip("-")) + r"(?![\w-])", output),
                        f"{name}: example flag missing from binary help: {flag}")
        print(f"PASS {name}: references, version, example flags" + (", binary help" if name in installed else ""))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lock", type=Path)
    parser.add_argument("--source-cache", type=Path)
    parser.add_argument("--tools-root", type=Path)
    parser.add_argument("--platform", choices=["linux/amd64", "linux/arm64"])
    parser.add_argument("--help-output", type=Path)
    args = parser.parse_args()
    validate(args.lock, args.source_cache, args.tools_root, args.platform, args.help_output)


if __name__ == "__main__":
    main()
