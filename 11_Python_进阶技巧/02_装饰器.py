"""
装饰器其实也是一种闭包，其功能就是在不破坏函数原有的代码和功能的情况下，为目标函数增加新功能。

"""

# 装饰器的一般写法（闭包）
# def outer(fun):
#     def inner():
#         print("go to bed")
#         fun()
#         print("get up")
#
#     return inner
# def sleep():
#     import random
#     import time
#     print("sleeping")
#     time.sleep(random.randint(5, 10))
#
# fn = outer(sleep)
# fn()

# 装饰器的语法糖写法
def outer(fun):
    def inner():
        print("go to bed")
        fun()
        print("get up")

    return inner

@outer    # 使用@函数名将sleep作为参数传入闭包函数
def sleep():
    import random
    import time
    print("sleeping")
    time.sleep(random.randint(5, 10))

sleep()
