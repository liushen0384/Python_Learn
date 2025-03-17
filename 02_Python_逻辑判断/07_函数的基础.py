"""
函数是指组织好的、可重复使用的，用来实现特定功能的代码段

"""

# 统计字符串长度

# 函数基础定义语法

# 关键字 函数名 传入参数
def len2(str_a):
    # 说明文档
    """
    可用于字符串、元组、列表、集合、字典等字面量的长度计算
    :param str_a:形参，为可计算长度的字面量
    :return:函数返回值1，函数长度值
    """

    # 函数主体
    # global关键字，可以在函数内定义全局变量
    count = 0
    for i in str_a:
        count += 1
    # 返回值
    return count


######
str1 = "liushen"

print(len2(str1))

# None  可用于判断，相当于False    可以赋予一些无初始值的变量 name = None