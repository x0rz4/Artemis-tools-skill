# 固定版本依据

核查日期：2026-10-12。以官方 v2.6.1 解析后的提交 `5a0ca8bde91b5bb16213e9e8b5c6871eac954bd8` 为依据；正文为独立编写的指导，没有复制社区 Skill。参数声明和结果结构是源码核验，不能等同于真实目标扫描验收。

- [pkg/runner/options.go](https://github.com/projectdiscovery/naabu/blob/5a0ca8bde91b5bb16213e9e8b5c6871eac954bd8/pkg/runner/options.go)
- [pkg/runner/output.go](https://github.com/projectdiscovery/naabu/blob/5a0ca8bde91b5bb16213e9e8b5c6871eac954bd8/pkg/runner/output.go)
- [README.md](https://github.com/projectdiscovery/naabu/blob/5a0ca8bde91b5bb16213e9e8b5c6871eac954bd8/README.md)

运行本机工具前仍需核对工具版本。升级后重新检查参数与输出字段，不沿用旧版结论。

该 tag README 把 timeout 写为整数毫秒，实际 options.go 已使用 DurationVar；正文使用显式 duration（2s），以代码声明为依据。
