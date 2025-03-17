"""
函数的多返回值
函数的传入参数

"""


# 函数的多返回值
def function():
    return 1, 2, "hello"

x, y, z = function()
print(x, y, 2)

# 函数
def fun1(x, y, z = 1): # 参数设置默认值必须在最后
    print(x, y, z)
    return
x = 0
y = 0
z = 0

# 位置参数
fun1(x, y, z) # 通过参数的位置找到其对应关系

# 关键字参数
fun1(y = "1", x = "20", z = "30") # 通过键=值的方式将参数传入，可与位置参数混用，位置参数在前

# 缺省参数
fun1(y = "1", x = "20")

# 不定长参数
# 位置传递的不定长参数
def fun2(*args):
    print(args)

fun2("10", 10)    #传入参数可以有无限个，最终合并为一个元组
fun2("10")

# 关键字传递的不定长参数
def fun3(**kwargs):
    print(kwargs)

fun3(liushne1 = 1,name2 = 2)  # 传入参数也可以有无限个，但是必须是键=值的形式

# 限定参数格式
def fun4(x:int,z:list):
    print(z[x])

fun4(2,[1, 3, 9])


