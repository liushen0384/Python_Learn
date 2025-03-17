"""
什么是数据容器：一种可以容纳多份数据的数据类型
包括列表list、元组tuple、字符串str、集合set、字典dict


"""

# 列表list
"""
可以容纳多个元素
可以容纳不同类型的元素
数据存储是有序的
允许数据重复
可以修改
"""
# 字面量
[1,2,3,4,5]

# 定义变量
list1 = [1,2,3,4,5]

# 空列表
list2 = []
list3 = list()

print(list1,type(list1))

# 列表的遍历输出
for i in list1:
    print(i)

# 列表嵌套
list4 = [[1, 2, 3], [4, 5, 6]]

# 遍历输出
# for i in list4:
#     for j in i:
#         print(j)

# 反向遍历列表
# i = 0
# j = -1
# while i < len(list1):
#     i += 1
#     print(list1[j])
#     j -= 1

# 列表的常用功能，称之为列表的方法
# 在指定位置插入元素
list1.insert(1, 100)
print(list1)

# 在列表结尾追加元素
list1.append(200)
print(list1)

# 在列表结尾追加多个元素
list1.extend(list4)
print(list1)

# 删除指定下标元素
# 两种方式 1、del 列表元素 2、pop方法取出
del list1[-1]
a = list1.pop(1)
print(list1, a)

# 删除指定元素,遍历删除，只会删除第一个
list5 = [99,100,99]
list1.extend(list5)
print(list1)
list1.remove(99)
print(list1)

# 统计单个元素数量
count = list1.count(99)
print(count)

# 统计全部元素数量
count = len(list1)
print(count)

# 查询某元素的下标值
a = list1.index(4)
print(a)

# 修改元素值
list1[3] = 9
print(list1[3])

# 清空列表
list1.clear()
print(list1)



