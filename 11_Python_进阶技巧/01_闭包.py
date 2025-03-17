"""
闭包简单的讲就是双层嵌套函数
闭包能够提高代码本次运行的稳定性

优点，使用闭包可以让我们得到:
无需定义全局变量即可实现通过函数，持续的访问、修改某个值
闭包使用的变量的所用于在函数内，难以被错误的调用修改
缺点:
由升内部函数持续引用外部函数的值，所以会导致这一部分内存空间不被释放一直占用内存

"""

# 简单闭包
# def outer(logo):
#
#     def inner(msg):
#         print(f"{logo}{msg}{logo}")
#
#     return inner

# 使用nonlocal关键字声名外部变量，可以对其进行修改
# def outer(num1):
#
#     def inner(num2):
#         nonlocal num1
#         num1 += num2
#         print(num1)
#     return inner

# ATM机实现
def ATM_UP(initial_acount: int = 0):

    def atm(num: int, deposit: bool = True):
        nonlocal  initial_acount
        if deposit:
            initial_acount += num
            print(f"存入{num}元，目前账户余额{initial_acount}元")
        else:
            initial_acount -= num
            print(f"取出{num}元，目前账户余额{initial_acount}元")

    return atm

fn1 = ATM_UP()
fn1(200, True)
fn1(200, True)
fn1(100, False)