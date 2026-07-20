# ============================================
# Day 5 综合练习：列表 + 字典 + 函数
# 每个练习都自己写，写完运行看结果
# ============================================

# ---- 练习1：函数 + 列表 ----
# 写一个函数 get_even_numbers，接收一个数字列表，返回其中所有的偶数
# 偶数：能被2整除 → x % 2 == 0
# 示例输入：[1,2,3,4,5,6] → 返回 [2,4,6]
# 提示：建一个空列表 result=[]，遍历，偶数就 append，最后 return

def get_even_numbers(nums):
    result = []
    for n in nums:
        if n % 2 == 0:
            result.append(n)
    return result   
    

# 测试（写完函数后删掉下面的 pass 再运行）
print("练习1:", get_even_numbers([1, 2, 3, 4, 5, 6]))


# ---- 练习2：函数 + 字典 ----
# 写一个函数 get_score_grade，接收一个字典（含 name 和 score），返回评语
# >= 90 → "优秀"  >= 70 → "良好"  >= 60 → "及格"  否则 → "不及格"
# 示例输入：{"name": "张三", "score": 85} → 返回 "张三的成绩：良好"
# 提示：用 if/elif/else 判断 score，用 f-string 拼接
def get_score_grade(student):
    name = student["name"]
    score = student["score"]
    if score >= 90:
        return f"{name}的成绩：优秀"
    elif score >= 70:
        return f"{name}的成绩：良好"
    elif score >= 60:
        return f"{name}的成绩：及格"
    else:
        return f"{name}的成绩：不及格"
# 测试
print("练习2:", get_score_grade({"name": "张三", "score": 85}))
print("练习2:", get_score_grade({"name": "李四", "score": 55}))


# ---- 练习3：列表套字典 + 函数 ----
# 写一个函数 find_most_expensive，接收一个商品列表（每个商品有 name 和 price）
# 返回最贵的那个商品（整个字典）
# 示例输入：[{"name":"可乐","price":3},{"name":"薯片","price":8},{"name":"巧克力","price":12}]
# → 返回 {"name":"巧克力","price":12}
# 提示：设一个变量 most = products[0]，遍历，谁更贵就换谁

def find_most_expensive(products):
    # 在这里写你的代码
    pass

# 测试
goods = [
    {"name": "可乐", "price": 3},
    {"name": "薯片", "price": 8},
    {"name": "巧克力", "price": 12},
    {"name": "矿泉水", "price": 2}
]
print("练习3:", find_most_expensive(goods))


# ---- 练习4：综合——通讯录搜索（列表 + 字典 + 函数） ----
# 写一个函数 search_contacts，接收通讯录列表 和 城市名
# 返回该城市的所有联系人（一个列表）
# 示例：search_contacts(contacts, "重庆") → [{"name":"张三","phone":"138","city":"重庆"}]

contacts = [
    {"name": "张三", "phone": "138xxx", "city": "重庆"},
    {"name": "李四", "phone": "139xxx", "city": "成都"},
    {"name": "王五", "phone": "137xxx", "city": "重庆"},
    {"name": "赵六", "phone": "136xxx", "city": "南通"},
]

def search_contacts(contacts, city):
   def search_contacts(contacts, city):
    contacts_in_city = []
    for contact in contacts:
        if contact["city"] == city:
            contacts_in_city.append(contact)        
    
    return contacts_in_city

    pass

# 测试
print("练习4:", search_contacts(contacts, "重庆"))


# ---- 练习5：综合——统计每个城市有多少人（有点挑战） ----
# 写一个函数 count_by_city，接收通讯录列表
# 返回一个字典：{"城市名": 人数, ...}
# 示例：上面 contacts → {"重庆": 2, "成都": 1, "南通": 1}
# 提示：遍历 contacts，city = c["city"]，如果字典里还没有这个城市就新建

def count_by_city(contacts):
    result = {}
    for contact in contacts:
        city = contact["city"]
        if city not in result:
           city = contact["city"]
           result [city] =1
        else: 
           result[city] = result[city] + 1
    return result

    pass

# 测试
print("练习5:", count_by_city(contacts))
