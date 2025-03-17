"""
while语句
基本机构
while 条件:
    执行语句1
    执行语句2
    ...

"""

# while循环基本案例
# import random
# num = random.randint(1,100)
# i = 0
# guass_num=0
#
# while num != guass_num:
#     guass_num = int(input("请输入猜测值："))
#     i += 1
#
#     if num > guass_num:
#         print("您猜错了！猜测值小了，请再次输入猜测值")
#     elif num < guass_num:
#         print("您猜错了！猜测值大了，请再次输入猜测值")
#
# print(f"恭喜您猜对了！一共猜测{i}次")


# while循环的循环嵌套：列表的排序
list1 = list(map(int,input("请输入一个数字列表:\n").split()))
list2 = list1
list2.sort()
i = 0
j = 0

while i < int(len(list1)-1):
    while j < int(len(list1)-i-1):
        if list1[j] > list1[j + 1]:
            inter = list1[j]
            list1[j] = list1[j + 1]
            list1[j + 1] = inter
        j += 1
    j = 0
    i += 1

print(f"{list1}\n{list2}")