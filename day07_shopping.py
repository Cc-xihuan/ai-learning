# ============================================
# Day 7：购物清单小项目
# 列表套字典 + 函数 + 循环 + 判断
# ============================================

# 每个商品：{"name": "名字", "price": 价格, "bought": False}
# bought: False=还没买, True=已经买了


# ---- 1. 添加商品 ----
def add_item(shopping_list, name, price):
    # 在这里写：建一个商品字典，加到列表里，打印"已添加"
    pass


# ---- 2. 删除商品 ----
def remove_item(shopping_list, name):
    # 在这里写：遍历列表，找到名字匹配的，删掉，打印"已删除"
    # 如果没找到，打印"没找到"
    pass


# ---- 3. 标记已买 ----
def mark_bought(shopping_list, name):
    # 在这里写：找到名字匹配的，把 bought 改成 True，打印"已标记"
    pass


# ---- 4. 显示清单 ----
def show_list(shopping_list):
    # 在这里写：逐行打印每个商品+状态，最后打印总价
    # 格式参考需求文档
    pass


# ---- 测试 ----
goods = []
add_item(goods, "可乐", 3.5)
add_item(goods, "薯片", 8.0)
add_item(goods, "矿泉水", 2.0)
mark_bought(goods, "薯片")
show_list(goods)
remove_item(goods, "矿泉水")
show_list(goods)
