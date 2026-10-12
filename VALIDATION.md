# 八份 Skill 验证记录

日期：2026-10-12。

## 已执行

- 根据 Registry 锁文件核对八项版本及平台，固定八个官方源码提交和关键文件 SHA-256。
- `python scripts/validate_skills.py --lock <registry-lock> --source-cache <reviewed-sources>`：八项通过，验证名称、版本、独立包内引用、锁文件摘要及示例选项在已审阅源码中的存在性。
- `skill-creator/scripts/quick_validate.py`：八项元数据与正文检查通过。
- 使用 Artemis 已锁定的 Norma v0.4.3 `skill.LoadDir` 加载八个实际目录，逐个调用 `Registry.Tool().Call`：八项均返回独立指导消息，name、description、license 及参考入口完整。此验证不连接数据库，不调用扫描器。
- 工作流 actionlint 通过；自动检查只调用固定二进制的帮助命令，不执行 Skill 中的目标示例。

## 核验中的关键差异

- fscan 的 `-h` 是目标，`-help` 才是帮助；kscan 的 `-t` 是目标，并发用 `--threads`。
- httpx、naabu、subfinder、katana、nuclei 使用文中指定的 JSONL 输出；ffuf 为含 results 的完整对象，fscan 为分类汇总对象，kscan 为数组。
- katana 端点在 request.endpoint，subfinder 的 collect-sources 对应 sources 数组，kscan 输出键包含大写 URL/Keyword。
- naabu 固定版本源码将 timeout 定义为 duration，README 整数毫秒说明滞后；示例显式使用 2s。
- Artemis 默认 `{args}` 模板不会拆分 argv；八份 Skill 明确说明实际 schema 适配前不能直接用它传递整串 CLI。

## 验证边界

双架构帮助检查状态以本仓库 Actions 与覆盖表为准。帮助检查只证明二进制可运行且识别相关选项，不证明目标扫描、示例输出或端到端编排正确。

本次未采集真实扫描输出、未连接业务数据库、未导入用户运行中的 Skill 库、未修改 command 执行器，也未将八份 Skill 发布到 Registry 稳定源。输出字段和错误处理依赖固定源码审阅；真实输出样本与隔离靶场验证留在 P2。
