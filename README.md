# Artemis Tools Skill

围绕 `Artemis-registry/packaging/tools-lock.json` 中的工具，维护适合 Artemis Agent 阅读的使用指导：何时使用、输入如何准备、参数如何选择、输出如何理解，以及失败后何时重试或停止。

当前阶段：**规划与来源调查**。已记录八个工具的覆盖目标和社区参考，尚未提供可发布的工具 Skill，也未接入自动同步。

## 仓库分工

| 仓库 | 职责 |
| --- | --- |
| [Artemis](https://github.com/x0rz4/Artemis) | 主程序、工具执行与审批、库管理、检查和手动更新 |
| **Artemis-tools-skill** | 工具使用指导、Skill 源码、参考资料与适配记录 |
| [Artemis-registry](https://github.com/x0rz4/Artemis-registry) | 工具锁文件、经审核的 Skill 打包、版本化 Releases 和稳定索引 |

本仓库以 Registry 的固定锁文件版本为依据。主程序的同名锁文件继续用于离线安装；版本差异需要单独核验。本仓库不维护另一份可独立升级的二进制下载锁，也不直接改变 Artemis 的运行时更新源。

## 首批覆盖

下列版本来自当前锁文件，表示待验证的指导目标，不表示各工具上游最新版本。

| 工具 | 锁定版本 | 拟维护内容 | 目标 Skill |
| --- | --- | --- | --- |
| httpx | 1.12.0 | HTTP 探活、标题与技术信息、结构化结果 | `httpx` |
| naabu | 2.6.1 | 主机与端口输入、权限和依赖、结果交接 | `naabu` |
| subfinder | 2.17.0 | 子域发现、数据源配置、去重与范围过滤 | `subfinder` |
| katana | 1.8.0 | 爬取范围、深度、URL 与接口结果 | `katana` |
| ffuf | 2.3.0 | 字典输入、匹配与过滤、结果噪声处理 | `ffuf` |
| nuclei | 3.11.1 | 模板选择与版本、结果证据、错误分类 | `nuclei` |
| fscan | 2.2.2 | 探测模块选择、参数核验、结果分类 | `fscan` |
| kscan | 1.85 | 端口与指纹识别、输出解释、架构限制 | `kscan` |

当前工具包支持 Linux amd64；Linux arm64 支持除 kscan 外的七项。Skill 文本本身可跨平台阅读，不代表对应二进制可在任意平台运行。

已有 api-recon、playwright-cli、scopesentry 继续按现有方式维护和发布。本批八项指导采用独立名称。

## 维护入口

- [维护计划](MAINTENANCE.md)：内容规范、GitHub 搜索、验证及发布衔接。
- [工具覆盖表](catalog/tool-coverage.json)：固定锁文件来源、版本、平台和实现状态。
- [候选来源](catalog/sources.json)：已找到的社区 Skill 固定提交、许可线索与待适配问题。
- [来源说明](SOURCES.md)：官方工具文档及社区候选的使用边界。

本仓库原创文档沿用 Artemis 的 AGPL-3.0 许可，见 [LICENSE](LICENSE)。链接的上游内容遵循各自许可；当前仅保存引用和调查元数据，未复制社区 Skill。未来复用文件时逐项保留版权和许可证。
