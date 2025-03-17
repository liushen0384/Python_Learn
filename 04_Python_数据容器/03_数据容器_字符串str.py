"""
字符串也是一个不可修改的数据容器
只能存储字符串
支持下标索引
不可修改
允许重复

"""

# 字符串下标索引
str1 = "liu sh en "
print(str1[0])
print(str1[-1])

# 字符串的查找
a = str1.index("u s")
print(a)

# 字符串的替换，会得到一个新字符串
new_str1 = str1.replace("en", "ne")
print(new_str1, str1)

# 字符串的切分，通过特定参数隔开得到一个列表
list1 = str1.split(" ")
print(str1, list1, type(list1))

# 字符串的规整
str2 = str1.strip()
print(str2)
# 去除首尾特定的参数
str2 = str2.strip("ln")
print(str2)

# 统计出现字符串次数
a = str1.count("en")
print(a)

# 统计字符串长度
num = len(str1)
print(str1, num)