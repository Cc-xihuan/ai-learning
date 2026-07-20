# ============================================
# Day 4：循环 — 让程序重复干活
# ============================================
# 用法：选中任意一段代码，按 Shift+Enter 单独运行
# 或者点每个 # %% 上面的 Run Cell

# 人话版：
# for   = "挨个来一遍"（你知道要重复多少次）
# while = "只要...就一直做"（你不知道要重复多少次）

import random


# ============================================
# 新知识：range() 怎么用
# ============================================
# range(结束)          → 0, 1, 2, ..., 结束-1
# range(开始, 结束)     → 开始, 开始+1, ..., 结束-1
# range(开始, 结束, 步长) → 每次跳步长
#
# 核心规则：永远不包含"结束"那个数！
#   range(5)        → 0, 1, 2, 3, 4        （5个，没有5）
#   range(1, 5)     → 1, 2, 3, 4           （没有5！）
#   range(1, 10)    → 1, 2, 3, ..., 9      （没有10！）
#   range(1, 10, 2) → 1, 3, 5, 7, 9        （每次+2）

# ============================================
# 新知识：random.randint() 怎么用
# ============================================
# random.randint(a, b)：在 a 和 b 之间随机抽一个整数
# 注意：和 range 不一样，randint 包含最后一个数！
#   range(1, 100)             → 1 到 99        没有100！
#   random.randint(1, 100)    → 1 到 100 任意一个  包含100！


# %% ===== 一、for 循环：做固定次数的事 =====
print("===== 一、for 循环 =====")

# range(5) = 0,1,2,3,4 —— 五次
for i in range(5):
    print(f"第{i+1}次：你好！")

print()

# 遍历列表
fruits = ["苹果", "香蕉", "橘子"]
for fruit in fruits:
    print(f"我喜欢吃{fruit}")


# %% ===== 二、while 循环：满足条件就一直做 =====
print("\n===== 二、while 循环 =====")

# 倒计时
num = 5
while num > 0:
    print(f"倒计时：{num}")
    num = num - 1  # 每次减1，不然会死循环！
print("发射！🚀")


# %% ===== 三、break 和 continue =====
print("\n===== 三、break 和 continue =====")

# break：中途退出
print("--- break：数到5就停 ---")
for i in range(1, 11):
    if i == 5:
        print("到5了，不数了！")
        break
    print(i)

# continue：跳过当前，继续下一个
print("\n--- continue：跳过3 ---")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# %% ===== 四、九九乘法表 =====
print("\n===== 四、九九乘法表 =====")

# i = 行号（第几行），从 1 到 9，共 9 行
# j = 每行的第几个，第 i 行有 i 个
# range(1, i+1) 就是 1 到 i（不包含 i+1，所以最后一个是 i）
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i*j}", end="\t")
    print()  # 一行结束，换行


# %% ===== 五、猜数字游戏（完整版） =====
print("\n===== 五、猜数字游戏 =====")

secret = random.randint(1, 100)  # 抽一个 1-100 的随机整数（包含100！）
guess = 0                         # 初始化，保证能进入 while 循环

print("我想了一个 1-100 之间的数字，你猜猜看。")

while guess != secret:
    guess = int(input("请输入你的猜测："))
    if guess < secret:
        print("太小了！往大猜")
    elif guess > secret:
        print("太大了！往小猜")
    else:
        print("🎉 猜对了！恭喜！")
