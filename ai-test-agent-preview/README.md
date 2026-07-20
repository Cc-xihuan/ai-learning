# AI 接口测试 Agent —— 预览版

## 这项目干嘛的？

给它一个 API 的描述，自动生成测试用例 → 执行 → 出报告。

你现在打开 `ai_test_agent.py`，会发现大部分代码看着眼熟（变量、函数、if/else、字典、列表、requests、JSON 都是你 Python 基础学过的）。

## 每学完一个阶段，回来看这个项目

| 你刚学的 | 项目的哪里用到了 | 你能看懂什么 |
|----------|------------------|-------------|
| **Python 基础** ✅ | 全篇 | 变量、函数、列表、字典、if/else、f-string、json、文件读写 |
| **Git**（现在学） | 项目目录 | 用 `git init` 管理这个项目，`git log` 看提交历史 |
| **LLM API 调用** | 现在还看不到 | 真实版中 `generate_test_cases()` 由 LLM 生成，不是写死的规则 |
| **Function Calling** | 现在还看不到 | LLM 自己决定调用哪个工具（读文档/生成用例/执行测试/写报告） |
| **RAG** | 现在还看不到 | 把 API 文档存到向量库，检索相关用例模板 |
| **pytest + requests** | `run_tests()` 函数 | 你能用 pytest 改写这里，加断言、参数化、fixture |
| **HTTP** | `requests.request()` | 理解 GET/POST、状态码 200/201/400、Header、Body |
| **SQL** | 现在还看不到 | 真实项目中测试结果存数据库，方便查询历史 |
| **Linux 命令** | 现在还看不到 | 在终端里用 `grep` 搜日志、`cat` 看报告 |

## 现在就试试（可选）

```bash
cd ~/Desktop/ai-learning/ai-test-agent-preview
python ai_test_agent.py
```

会生成一个 `test_report.md` 文件，打开看看报告长什么样。
