# ============================================
# Day 3：条件判断 — 让程序自己拿主意
# ============================================

# 人话版：if = "如果"，elif = "否则如果"，else = "否则"
# 就像你做选择：如果下雨→带伞，否则如果阴天→带外套，否则→直接出门


# ---- 一、基础 if ----
print("===== 基础 if/else =====")

score = int(input("输入你的分数（0-100）："))

# 下面这个判断逻辑你来补完——
# 提示：>= 90 打印"优秀"，>= 70 打印"良好"，>= 60 打印"及格"，否则"不及格"

# （在这里写你的 if/elif/else 代码，然后删掉这行注释）
if score >= 90:
    print("优秀")
elif score >= 70:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# ---- 二、比较运算符 ----
print("\n===== 比较运算符 =====")

a = 10
b = 5

print(f"a = {a}, b = {b}")
# 下面每行你来补，模仿第一行的写法：

print(f"a == b ,{a == b}")   # == 是"等于"，注意是双等号！
print(f"a != b, {a != b}")             # != 是"不等于"
print(f"a > b, {a > b}")              # > 大于


print(f"a < b, {a < b}")              # < 小于


# ---- 三、逻辑运算符：and / or / not ----
print("\n===== 逻辑运算符 =====")

has_id = True   # 有身份证
can_pay = False # 有钱吗

# and：两边都是 True 才 True
print(f"有身份证 且 有钱 → {has_id and can_pay}")

# or：任一边是 True 就 True
print(f"有身份证 或 有钱 → {has_id or can_pay}")

# not：反过来
# （在这补一行 print，用 not）
print(f"没有身份证 → {not has_id}")

# ---- 四、综合练习 ----
print("\n===== 综合：网吧门禁 =====")
# 要求：满18岁 且 带了身份证 → 能上网，否则 → 不能
age =int(input("请输入你的年龄:"))
take_id = True  # 带身份证吗
if age >= 18 and take_id:
        print("可以上网")
else:
        print("不能上网")
