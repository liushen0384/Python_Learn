"""
通过key 与 value间的映射关系建立的集合
key值不可重复

"""

# 基础定义
dict1 = {}
dict1 = dict()
dict1 = {"liushen": 8000, "lushuai": 9000}
print(dict1, type(dict1))

# 取出字典中的value
print(dict1["liushen"])

# 字典新增元素
dict1["shihao"] = 10000
print(dict1)

# 字典更新元素
dict1["shihao"] = 12000
print(dict1)

# 删除元素
dict1.pop('shihao')
print(dict1)

# 获取字典中所有的key
list1 = dict1.keys()
print(list1, type(list1))

# # 清空元素
# dict1.clear()
# print(dict1)

# 统计字典内的元素数量
s = len(dict1)
print(s)

