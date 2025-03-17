"""



"""
# 调用包两种方式
# import my_utils.my1
# import my_utils.my2
# from my_utils import my1
# from my_utils import my2
# my1.fun1()
# my2.fun1()

# __all__ 可以控制包中*关键字可以调用的模块
from my_utils import *
my1.fun1()
my2.fun1()