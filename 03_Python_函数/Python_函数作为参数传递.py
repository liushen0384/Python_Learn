"""
函数也可以作为函数的传入参数,这是一种计算逻辑的传递

"""

def fun(com,x,y):
    s = com(x, y)
    print(s)

def com1(x, y):
    s = x + y
    return s

def com2(x, y):
    s = x - y
    return s

fun(com1,4,5)


# lambda关键字可以定义匿名函数，无名称的函数只能临时使用一次
# 函数主体只能有一行
fun(lambda x, y: x + y, 1, 4)