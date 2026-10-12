---
name: katana
description: 使用 katana 在给定 URL 范围内爬取链接和接口线索，控制深度、时间及范围，并从 JSONL 提取请求端点；适用于已有 Web 入口的内容发现。
license: AGPL-3.0-only
---

# Web 链接与接口线索

适用版本：**katana 1.8.0**；Linux amd64 / arm64。依据见 [固定版本来源](references/sources.md)。

## 调用准备

先读 [Artemis 调用约定](references/artemis.md)。输入应是 httpx 已确认或用户指定的完整 URL，保留 scheme、端口和入口路径。爬取会发送请求；范围规则还需在结果交接时再次应用。

常规任务先用普通爬取器。浏览器、自动填表和混合模式有额外依赖或交互行为，不由“发现 URL”自动推导启用。

## 参数与示例

| 参数 | 用途 |
| --- | --- |
| `-u` / `-list` | 起始 URL 或包含 URL 的文件 |
| `-d` / `-ct` | 最大深度 / 单目标爬取时限，例如 `1m` |
| `-fs fqdn` | 限定完整域名；默认 `rdn` 范围可能更宽 |
| `-cs` / `-cos` | 跟随 URL 的包含 / 排除正则 |
| `-jc` | 解析 JavaScript 中的端点线索，按需启用 |
| `-rl -timeout -retry` | 请求速率、超时秒数、重试次数 |
| `-j -o` | JSONL 输出 |

```bash
katana -u https://app.example.com -d 2 -ct 1m -fs fqdn -cs '^https://app\.example\.com(?:/|$)' -rl 5 -timeout 10 -retry 1 -j -o /work/run-001/katana.jsonl -duc
```

替换起始 URL 时同步修改正则；示例仅允许该 HTTPS 主机的默认端口，不能直接用于其它主机或端口。路径受限任务还需将包含正则收窄至允许前缀，并检查跳转。`-fs fqdn` 本身不限定端口或路径。

## 解释 JSONL

根对象包括 `request`、`response`、`error`；URL 位于 **`request.endpoint`**，不能按顶层 `url` 取值。保留 `request.method`、`request.source` 及可用的 `response.status_code`。缺少 response 不代表请求成功，含 error 的行需独立统计。

按方法与完整端点去重，查询参数先保留用于接口分析。日志、HTML 正文和请求凭据不进入简要汇报。URL 是发现线索，不证明接口可匿名调用或存在漏洞。

需要目录字典发现时，先选择少量范围内入口交给 ffuf；需要模板核验时，先筛选相关 URL 和模板。不要对每条爬取记录无条件调用所有工具。

## 故障与停止

- URL 或正则错误：先修正一次，不能通过关闭范围控制让任务继续。
- 429、持续 5xx：降低速率并停止当前批；在预算允许时只补试失败入口一次。
- 浏览器缺失：普通爬取仍可用于适用任务；需要浏览器的页面明确标记覆盖不足，不自动下载浏览器。
- 达到时限或深度：报告实际边界。仅有登录页或空结果时不能声称前端接口已完整覆盖。
