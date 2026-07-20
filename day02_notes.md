# Day 2 笔记：变量、数据类型、input、f-string

**日期**：2026/06/23

---

## 1. 变量 —— 用自己的话重新写一遍


你的解释：给盒子贴标签


## 2. 四种数据类型

| 类型 | 代码里长什么样 | 能做什么 | 不能做什么 |
|---|---|---|---|
| str 字符串 | `"hello"` |能拼接不能运算
| int 整数 | `42` |能运算| 不能跟字符串直接+
| float 浮点数 | `3.14` | 能运算| 不能跟字符串直接+
| bool 布尔值 | `True` `False` |是判断条件 不能计算

## 3. 什么时候需要 `int()` `float()` `str()`

写出三条规则：

```
规则1：input() 返回的全是字符串，要算数就 int() 或 float()
规则2：整数用 int()，小数用 float()
规则3：数字要拼进字符串用 str() 或直接 f-string

## 4. `input()` 的本质

`input()` 不管你输入什么，返回的永远是__字符串_____。

所以如果你要拿用户输入做数学计算，必须先_在前面加个int_。

而名字本身就是文字，所以___直接input。

## 5. f-string —— 什么场景用它

没有 f-string 之前你得这样写：
```python
print("我叫" + name + "，今年" + str(age) + "岁")
```
又长又丑还得手动转类型。

有 f-string 之后：
```python
（把你代码里实际用过的一句 f-string 贴在这里）
```print(f"我叫{name},今年{age}岁")
你的感受：f-string 让代码变得更 __________。
 print(f"{contact['name']} → {contact['phone']} → {contact['city']}")
## 6. 今天报过的错

至少写一个你今天遇到的报错：

```
报错信息：没找到文件
原因（自己话）：打开python他自动在最大的目录cc
怎么修的：用cd -~加文件名定位到当前文件，就可以用python了
```

## 7. 迷你计算器 —— 把你跑通的代码贴下来
input1=int(input("请输入第一个数字:"))
input2=int(input("请输入第二个数字:"))
result=input1+input2
print(f"两个数字之和是{result}")
diff=input1-input2
print(f"两个数字之差是{diff}")
product=input1*input2
print(f"两个数字之积是{product}")
quotient=input1/input2
print(f"两个数字之商是{quotient}")
```python
# 在这里贴你的计算器代码
```

## 8. 自我检测（不跑代码，用脑想）

看这段代码，说出哪里会报错，为什么：
```python
x = input("输入数字：")
print(x + 5)
```

你的答案：input的是字符串
没办法直接进行数字运算要在前面加int（）


---

*填完告诉 Claude 检查*
