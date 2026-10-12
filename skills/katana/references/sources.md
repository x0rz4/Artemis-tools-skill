# 固定版本依据

核查日期：2026-10-12。以官方 v1.8.0 解析后的提交 `35267ac5c8ff1db9694a319d0eb466ed97b0969f` 为依据；正文为独立编写的指导，没有复制社区 Skill。参数声明和结果结构是源码核验，不能等同于真实目标扫描验收。

- [cmd/katana/main.go](https://github.com/projectdiscovery/katana/blob/35267ac5c8ff1db9694a319d0eb466ed97b0969f/cmd/katana/main.go)
- [pkg/output/result.go](https://github.com/projectdiscovery/katana/blob/35267ac5c8ff1db9694a319d0eb466ed97b0969f/pkg/output/result.go)
- [pkg/navigation/request.go](https://github.com/projectdiscovery/katana/blob/35267ac5c8ff1db9694a319d0eb466ed97b0969f/pkg/navigation/request.go)
- [pkg/navigation/response.go](https://github.com/projectdiscovery/katana/blob/35267ac5c8ff1db9694a319d0eb466ed97b0969f/pkg/navigation/response.go)

运行本机工具前仍需核对工具版本。升级后重新检查参数与输出字段，不沿用旧版结论。
