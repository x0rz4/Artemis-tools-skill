---
name: nuclei
description: 使用 nuclei 对已筛选目标执行明确的本地模板集合，核对模板依赖与版本，解释 JSONL 命中证据及失败情况；适用于范围和检测内容已确定的模板核验。
license: AGPL-3.0-only
---

# 模板核验与证据整理

适用版本：**nuclei 3.11.1**；Linux amd64 / arm64。依据见 [固定版本来源](references/sources.md)。

## 调用准备

先读 [Artemis 调用约定](references/artemis.md)。准备范围内 URL 列表和已经审核的本地模板目录，记录模板来源提交/版本及摘要。**二进制锁文件不锁定 nuclei-templates**，安装 nuclei 不等于模板已就绪。

根据前序服务和技术线索选择模板；检查模板协议、请求行为、目标变化和依赖。低 severity 不保证没有副作用；不要默认运行全部模板、启用代码执行、浏览器或模糊测试模式。需要这些模式时以明确任务范围另行选择。

## 参数与示例

| 参数 | 作用 |
| --- | --- |
| `-l` / `-u` | 目标列表 / 单个目标 |
| `-t` | 指定现有模板文件或审核目录 |
| `-validate` | 校验模板；不代表已经对目标核验成功 |
| `-jsonl -o` | JSONL 结果文件 |
| `-rl -timeout -retries` | 请求速率、请求超时秒数、失败重试次数 |
| `-duc` | 关闭自动引擎/模板更新检查 |
| `-ni` | 禁用 Interactsh 并排除 OAST 模板；会减少覆盖范围 |

先做模板校验，再按实际工具 schema 执行指定检测：

```bash
nuclei -t /work/templates-reviewed -validate -duc
```

```bash
nuclei -l /work/urls.txt -t /work/templates-reviewed -jsonl -o /work/run-001/nuclei.jsonl -rl 5 -timeout 10 -retries 1 -duc -ni
```

示例关闭外部回连，不适合依赖 OAST 的检测；该类任务需要明确的回连服务条件和范围。缺少模板时停止并报告，不能用自动更新 latest 来填补依赖。保持部署配置可追溯，避免加载未审核的自定义模板源。

## 解释命中

逐行读取 `template-id`、`info`、`type`、`host`、`matched-at`、`matcher-name`、`matcher-status`、`timestamp`。severity 位于 `info`；字段可能缺失，匹配状态应结合模板语义判断。提取结果可能含敏感数据，只在任务证据中保留必要内容。

按模板 ID、匹配位置和 matcher 去重，但保留每条原始证据。区分“模板命中”“待复核”和“已证实”；不能仅凭模板标题宣称漏洞已被利用。无命中仅说明所选模板在本次条件下未发现匹配。

## 故障与停止

- 模板不兼容或校验失败：记录模板与引擎版本并停止该集合，不关闭校验硬跑。
- 没有可执行模板：核对目录、筛选条件与 `-ni` 造成的排除，不扩大到全模板集合。
- 网络超时：仅对失败目标在预算内补试一次；持续错误、429 或明显服务异常则停止。
- 空文件：同时汇报实际执行模板数、目标覆盖和错误；模板未执行不能记为检测通过。
