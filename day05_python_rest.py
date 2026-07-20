# ============================================
# Day 5-6：Python 基础全部收官
# 列表 / 字典 / 函数 / 文件 / JSON / 异常 / requests
# ============================================

# %% ===== 一、列表 [] =====
# 有顺序的盒子，按位置拿东西
nums = [1, 2, 3, 4, 5]
nums.append(6)      # 末尾加
nums.pop()           # 末尾删
nums[0] = 99         # 改第1个
print(nums[0])       # 查第1个
print(len(nums))     # 长度
for n in nums:       # 遍历
    print(n)

# 练习：创建一个颜色列表，增删改查遍历都写一遍
colors = ["红色","黄色","蓝色"]
colors.append("绿色")
colors.pop()
colors.remove("黄色")
colors[0]="青色"
print(colors[0])
print(len(colors))
for color in colors:
    print(color)

# %% ===== 二、字典 {} =====
# 键值对，按名字找人（不是按位置）
person = {"name": "张三", "age": 21, "city": "重庆"}
print(person["name"])           # 查
person["job"] = "学生"           # 加
person["age"] = 22              # 改
del person["city"]              # 删
for k, v in person.items():     # 遍历
    print(f"{k} → {v}")

# 练习：建一个通讯录，列表里套字典，存3个联系人
contacts = [{"name":"张三","phone":1234567890,"city":"重庆"},
{"name":"李四","phone":1234567890,"city":"北京"},
{"name":"王五","phone":1234567890,"city":"上海"}]

contacts.append({"name":"赵六","phone":1234567890,"city":"广州"})
del contacts[0]
contacts[0]["phone"] = 9876543210
contacts[1]["phone"] = 1234567890
for contact in contacts:
    print(f"{contact['name']} → {contact['phone']} → {contact['city']}")

# %% ===== 三、函数 def =====
# 把一段代码打包，起个名字，需要就用
def calc_total(price, count):
    """算总价"""
    return price * count

total = calc_total(15, 3)
print(f"总价：{total}")


def describe(name, age=0, city="未知"):
    """带默认值的函数"""
    return f"{name}，{age}岁，来自{city}"

print(describe("张三", 21, "重庆"))
print(describe("李四"))  # 用默认值

# 练习：写一个函数，接收一个数字列表，返回最大值和平均值
def analyze_numbers(nums):
    return max(nums) , sum(nums)/len(nums)

print(analyze_numbers([1,2,3,4,5]))
print(analyze_numbers([1,204,3240,23,89]))



# %% ===== 四、文件读写 =====
# open(文件名, 模式)  模式：'r'读 'w'写（覆盖） 'a'追加
# with 自动关文件

# 写文件
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")

# 读文件
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# 按行读
with open("test.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(f"行内容：{line.strip()}")


# %% ===== 五、JSON =====
# 把 Python 的列表/字典 和 字符串 互相转
# 存文件用 dumps，读文件用 loads
import json

data = [{"name": "张三", "age": 21}, {"name": "李四", "age": 22}]

# Python → JSON字符串 → 写文件
json_str = json.dumps(data, ensure_ascii=False, indent=2)
with open("data.json", "w", encoding="utf-8") as f:
    f.write(json_str)

# 读文件 → JSON字符串 → Python
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.loads(f.read())
    print(loaded[0]["name"])  # 张三


# %% ===== 六、异常处理 try/except =====
# 程序遇到错误别直接崩溃，优雅地处理

try:
    num = int(input("输入一个数："))
    print(f"100 ÷ {num} = {100 / num}")
except ValueError:
    print("让你输数字！不是文字！")
except ZeroDivisionError:
    print("不能除以零！")
finally:
    print("不管有没有错，这行都会跑")

# 常见异常：
# ValueError      → 类型转换失败
# ZeroDivisionError → 除以零
# FileNotFoundError → 文件不存在
# KeyError         → 字典里没有这个键


# %% ===== 七、requests：第一次和互联网说话 =====
# pip install requests（如果没装，终端跑这行）
import requests

# 调一个免费 API
url = "https://api.quotable.io/random"
resp = requests.get(url)

print(f"状态码：{resp.status_code}")  # 200 = 成功
if resp.status_code == 200:
    data = resp.json()
    print(f"名言：{data['content']}")
    print(f"作者：{data['author']}")

# 练习：调 https://api.github.com 看返回了什么
