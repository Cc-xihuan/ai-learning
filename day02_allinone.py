# ============================================
# Day 2 综合练习：变量 + f-string + input
# ============================================
# 把今天学的三个东西串起来

print("===== 📋 个人信息登记系统 =====")
print()

# 收集信息
name = input("姓名：")
age_input = input("年龄：")
height_input = input("身高（米）：")
city = input("城市：")
school = input("学校：")

# 转换类型（input 拿到的都是字符串，数字需要转）
age = int(age_input)          # 转成整数
height = float(height_input)  # 转成小数

print()
print("===== 📄 登记结果 =====")
print(f"姓名：{name}")
print(f"年龄：{age} 岁")
print(f"身高：{height} 米")
print(f"城市：{city}")
print(f"学校：{school}")
print(f"出生年份：大约是 {2026 - age} 年")
print("===== ✅ 登记完成 =====")
