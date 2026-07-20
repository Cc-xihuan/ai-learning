"""
============================================================
  AI 接口测试 Agent —— 超简预览版
  这是你学完后的"王牌项目"的婴儿版。
  现在看不懂正常，学完阶段二+三回来看，会发现全都能看懂。
============================================================

这个 Agent 干了什么（面试时你就这么说）：
  1. 读入一个 API 的定义（JSON 格式）
  2. 自动生成测试用例（正常 + 异常场景）
  3. 用 requests 执行所有用例
  4. 输出一份测试报告

真实版会加上 LLM——让 AI 自己决定测什么、怎么测。
这里先用规则生成用例，让你看到完整流程。
"""

import requests
import json
from datetime import datetime


# ==========================================
# 第1步：定义 API（模拟"读文档"这一步）
# ==========================================
# 真实项目中，LLM 会自己读 API 文档并解析出这些信息
# 你现在学：这个 JSON 结构就是 HTTP 基础那节课的内容

API_DEFINITION = {
    "name": "JSONPlaceholder /posts",
    "base_url": "https://jsonplaceholder.typicode.com",
    "endpoints": [
        {
            "method": "GET",
            "path": "/posts",
            "description": "获取所有文章列表",
            "params": {"userId": "可选，按用户ID筛选"}
        },
        {
            "method": "POST",
            "path": "/posts",
            "description": "创建一篇新文章",
            "body": {"title": "字符串，必填", "body": "字符串，必填", "userId": "整数，必填"}
        }
    ]
}


# ==========================================
# 第2步：自动生成测试用例
# ==========================================
# 真实项目中，这步由 LLM 来做（Function Calling）
# 你现在学：理解"正常用例"和"异常用例"的区别

def generate_test_cases(api_def):
    """根据 API 定义，生成测试用例列表"""
    cases = []

    for ep in api_def["endpoints"]:
        method = ep["method"]
        path = ep["path"]
        url = api_def["base_url"] + path

        # 正常场景：合法的请求应该返回 2xx
        if method == "GET":
            cases.append({
                "name": f"GET {path} —— 正常获取",
                "request": {"method": "GET", "url": url},
                "expect": {"status": 200}
            })

        elif method == "POST":
            # 正常 POST
            cases.append({
                "name": f"POST {path} —— 正常创建",
                "request": {
                    "method": "POST",
                    "url": url,
                    "json": {"title": "测试标题", "body": "测试内容", "userId": 1}
                },
                "expect": {"status": 201}
            })

            # 异常场景：缺少必填字段
            cases.append({
                "name": f"POST {path} —— 缺少必填字段",
                "request": {
                    "method": "POST",
                    "url": url,
                    "json": {"title": "缺了body和userId"}
                },
                "expect": {"status": [400, 201]}  # JSONPlaceholder 不校验，所以接受 201
            })

    return cases


# ==========================================
# 第3步：执行测试
# ==========================================
# 真实项目中，这步由 pytest + requests 完成
# 你现在学：每次复习回来，能认出更多代码

def run_tests(cases):
    """执行所有测试用例，返回结果列表"""
    results = []

    for i, case in enumerate(cases, 1):
        req = case["request"]
        expected_status = case["expect"]["status"]

        try:
            # 发送 HTTP 请求 —— 这就是你阶段三要学的内容
            resp = requests.request(
                method=req["method"],
                url=req["url"],
                json=req.get("json"),
                timeout=10
            )

            # 判断是否通过
            if isinstance(expected_status, list):
                passed = resp.status_code in expected_status
            else:
                passed = resp.status_code == expected_status

            results.append({
                "id": i,
                "name": case["name"],
                "passed": passed,
                "status_code": resp.status_code,
                "response": resp.json() if resp.headers.get("content-type", "").startswith("application/json") else resp.text[:100],
                "error": None
            })

        except Exception as e:
            # 网络异常、超时等 —— 这就是你的异常处理知识
            results.append({
                "id": i,
                "name": case["name"],
                "passed": False,
                "status_code": None,
                "response": None,
                "error": str(e)
            })

    return results


# ==========================================
# 第4步：生成测试报告
# ==========================================
# 真实项目中，LLM 会帮你写报告的"分析建议"部分

def generate_report(results):
    """生成 Markdown 格式的测试报告"""
    total = len(results)
    passed = sum(1 for r in results if r["passed"])
    failed = total - passed

    report = f"""# 接口测试报告

> 生成时间：{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
> 测试接口：JSONPlaceholder /posts

## 概要

| 指标 | 数值 |
|------|------|
| 总用例数 | {total} |
| ✅ 通过 | {passed} |
| ❌ 失败 | {failed} |
| 通过率 | {passed/total*100:.1f}% |

## 详细结果

| # | 用例 | 结果 | 状态码 |
|---|------|------|--------|
"""

    for r in results:
        status = "✅ 通过" if r["passed"] else "❌ 失败"
        code = r["status_code"] or "N/A"
        report += f"| {r['id']} | {r['name']} | {status} | {code} |\n"

    # 失败详情
    failures = [r for r in results if not r["passed"]]
    if failures:
        report += "\n## 失败详情\n\n"
        for r in failures:
            report += f"### {r['id']}. {r['name']}\n"
            if r["error"]:
                report += f"- 错误：{r['error']}\n"
            elif r["response"]:
                report += f"- 响应：\n```json\n{json.dumps(r['response'], ensure_ascii=False, indent=2)[:500]}\n```\n"
            report += "\n"

    return report


# ==========================================
# 主流程 —— 就这么简单！
# ==========================================

if __name__ == "__main__":
    print("AI 接口测试 Agent 启动...")
    print(f"目标 API：{API_DEFINITION['name']}\n")

    # Step 1+2：生成用例
    cases = generate_test_cases(API_DEFINITION)
    print(f"生成了 {len(cases)} 条测试用例")

    # Step 3：执行测试
    print("执行测试中...")
    results = run_tests(cases)

    # Step 4：出报告
    report = generate_report(results)

    # 保存报告
    report_path = "test_report.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"[OK] 报告已生成：{report_path}")
    print(f"   通过 {sum(1 for r in results if r['passed'])}/{len(results)}")
