# 固定版本依据

核查日期：2026-10-12。以官方 v3.11.1 解析后的提交 `a8c88feb4a1c8e961b7902534ce3af97e9d524a4` 为依据；正文为独立编写的指导，没有复制社区 Skill。参数声明和结果结构是源码核验，不能等同于真实目标扫描验收。

- [cmd/nuclei/main.go](https://github.com/projectdiscovery/nuclei/blob/a8c88feb4a1c8e961b7902534ce3af97e9d524a4/cmd/nuclei/main.go)
- [pkg/output/output.go](https://github.com/projectdiscovery/nuclei/blob/a8c88feb4a1c8e961b7902534ce3af97e9d524a4/pkg/output/output.go)

运行本机工具前仍需核对工具版本。升级后重新检查参数与输出字段，不沿用旧版结论。
