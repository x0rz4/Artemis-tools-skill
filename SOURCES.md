# 来源与调查范围

调查日期：2026-10-12。以下链接用于核查来源与后续适配，不代表其内容已经通过 Artemis 验证。

## 工具官方资料

| 工具 | 官方仓库 | 使用依据 |
| --- | --- | --- |
| httpx | [projectdiscovery/httpx](https://github.com/projectdiscovery/httpx) | 锁定版本的帮助、参数与输出说明；注意与 Python 同名库区分 |
| naabu | [projectdiscovery/naabu](https://github.com/projectdiscovery/naabu) | 端口扫描方式、依赖和输出说明 |
| subfinder | [projectdiscovery/subfinder](https://github.com/projectdiscovery/subfinder) | 被动子域发现与数据源配置 |
| katana | [projectdiscovery/katana](https://github.com/projectdiscovery/katana) | 爬取范围与输出说明 |
| ffuf | [ffuf/ffuf](https://github.com/ffuf/ffuf) | 输入、过滤与输出说明 |
| nuclei | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei) | 模板执行、模板依赖与结果说明 |
| fscan | [shadow1ng/fscan](https://github.com/shadow1ng/fscan) | 版本对应的模块、参数与输出 |
| kscan | [lcvvvv/kscan](https://github.com/lcvvvv/kscan) | 端口与指纹功能、参数及架构支持 |

这些首页属于发现入口，实施时需要解析覆盖表中对应 Release 的固定版本资料，不能直接把主分支新参数写入旧版指导。

## 社区 Skill 候选

| 文件 | 已核查事实 | 尚需适配 |
| --- | --- | --- |
| [PAIPlugin / ffuf](https://github.com/danielmiessler/PAIPlugin/blob/6125f29522966c169dc6e1929187f5685aa7dfa4/skills/ffuf/SKILL.md) | 原文件存在；仓库声明 MIT；固定到明确提交 | ffuf 2.3.0 参数、附带资源许可、Artemis 已注册工具调用、结果样本 |
| [hack-skills / recon-and-methodology](https://github.com/yaklang/hack-skills/blob/6fbf0bc8d5c71830d62543a308d8744606c43d7c/skills/recon-and-methodology/SKILL.md) | 原文件存在；仓库声明 MIT；包含现有侦察工具的流程参考 | 裁剪未安装工具依赖，按八项锁定版本核验参数，分拆为单工具指导 |

仅保存链接和调查元数据，没有复制上述 Skill 或执行其中命令。MIT 是仓库级初筛信息；后续采用具体文件时重新核对文件与依赖许可，并保留原始版权声明。
