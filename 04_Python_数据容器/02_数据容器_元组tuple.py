"""
元组是不可修改的列表
元组一但定义完成，就不可修改
元组可以看为只读的列表
"""

# 元组的定义
t1 = ("liushen", 198, 648, False)
tuple1 = ()
tuple2 = tuple()
tuple3 = (1, )  # 定义单元素元组需要在元素后加上，

print(t1,type(t1))

# 元组的查找方法
a = t1.index(198)
print(a, t1[a])

# 统计元组中单个元素的个数
print(t1.count(648))

# 计算元组的元素个数
print(len(t1))

# 元组内容不可修改
# 元组内嵌套的list列表可以修改
t3 = (1, 2, 3, [1, 2, 3])
print(t3[3])
t3[3][2] = 9
print(t3[3])