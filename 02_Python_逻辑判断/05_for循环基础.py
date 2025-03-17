"""
for循环语句
轮询执行机制
for 临时变量 in 待处理数据集：
    执行语句
    ....
将待处理数据集中的变量一次赋予临时变量，直到完成查询

range()函数，返回一个数字序列
"""


# 示例
name = "liushen"
for x in name:
    print(x)

# 示例2
for x in range(8):
    print(x)

# 示例3
for x in range(2, 8):
    print(x)

# 示例
for x in range(2, 8, 3):
    print(x)