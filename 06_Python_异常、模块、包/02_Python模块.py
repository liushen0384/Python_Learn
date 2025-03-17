"""
模块（Module），是一个定义好的Python文件
可以调用其中提前写好的函数和方法

"""

# 模块的使用需要先进行导入，语法如下[]内为可选 同名函数后引用的会覆盖掉之前的
"""
[from 模块名] import [模块 | 类 | 变量 | 函数 | *][as 别名]

"""

# 调用模块
# import time
#
# # 调用函数
# time.sleep(5)
# print("你好")

# 调用模块中的单独函数
# from time import sleep
# sleep(5)
# print("再次你好")

# 调用模块并改变其名称
# import time as tt
# tt.sleep(5)
# #print("再次你好")

# 调用模块中的函数并改变其名称
from time import sleep as tt
tt(5)
print("再次你好")