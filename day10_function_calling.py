from openai import OpenAI
import json

client = OpenAI(
    base_url="https://api.deepseek.com/v1",
    api_key="sk-97385e2c60b342489b102b17d23effa2",
)

# 第一步：定义一个"工具"——真实能执行的事
def get_weather(city):
    """查天气（假装查到了，其实就是写死的）"""
    weather_data = {
        "北京": "晴天，25°C",
        "上海": "小雨，20°C",
        "重庆": "多云，30°C",
    }
    return weather_data.get(city, "没这个城市的数据")

# 第二步：把工具告诉模型——这个工具长什么样
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "查询指定城市的天气",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "城市名，如北京"}
            },
            "required": ["city"]
        }
    }
}]

# 第三步：把用户问题 + tools 一起发给模型
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个天气助手，用户问天气时用 get_weather 工具查询"},
        {"role": "user", "content": "北京天气怎么样"},
    ],
    tools=tools,
    tool_choice={"type": "function", "function": {"name": "get_weather"}},
)

print("=== 模型请求的工具调用 ===")
print(response.choices[0].message)

# 第四步：取出模型要求的工具调用，执行函数，把结果发回去
tool_call = response.choices[0].message.tool_calls[0]
func_name = tool_call.function.name
func_args = json.loads(tool_call.function.arguments)
print(f"\n=== 执行函数：{func_name}({func_args}) ===")

result = get_weather(**func_args)
print(f"函数返回：{result}")

# 把结果发回给模型
messages = [
    {"role": "system", "content": "你是一个天气助手。"},
    {"role": "user", "content": "北京今天天气怎么样？"},
    response.choices[0].message,
    {"role": "tool", "tool_call_id": tool_call.id, "content": result},
]

final_response = client.chat.completions.create(
    model="deepseek-chat",
    messages=messages,
)

print("\n=== 模型最终回答 ===")
print(final_response.choices[0].message.content)
