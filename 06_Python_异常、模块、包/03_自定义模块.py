"""
自己制作模块，模块调用时会运行其中的代码


"""
# __main__名称 可以使模块中的代码行在被调用时不会被执行
#if __name__ == "__main__":
  #  print("你好")

# __all__可以定义模块中被引入是*关键字所能引入的函数
from test_module import *
count1(1,3)
count2(1,3)