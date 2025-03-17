"""
集合set 使用{}定义，其内部元素是无序且不可重复的
因为集合无序，所以不支持下标索引

"""

# 定义集合
my_set = set()
my_set = {5, 6, 7, 5, 6, 0}
print(my_set,type(my_set))

# 集合添加新元素
my_set.add("liushen")
print(my_set)

# 移除元素
my_set.remove(6)
print(my_set)

# 将集合中的元素取出，同时集合中元素移除
a = my_set.pop()
print(a, my_set)

# 清空集合
my_set.clear()
print(my_set)

# 得到差集
set1 = {1, 2, 3, 5}
set2 = {2, 3, 9, 10}
set3 =set1.difference(set2)   # set1中有，而set2中没有的元素
print(set3)

set1.difference_update(set2)  # 将set1中与set2的相同元素移除
print(set1)

# 集合合并
set3 = set1.union(set2)
print(set3)

# 统计集合内元素的数量
s = len(set3)
print(s)