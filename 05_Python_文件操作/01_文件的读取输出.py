"""
文件的读取和写入
文件的读取，上一次读取会影响下一次读取
"""
import time

# 文件的打开
"""
open函数可以打开一个文件，当文件不存在时会创建一个新的文件
open(name,mode,encoding)
name表示文件名，mode是打开文件的模式，包括只读r，写入w、追加a等
encoding表示编码格式
"""
f = open('C:/DSoftware/Python_txt/test.txt', 'r', encoding='UTF-8')
# print(type(f))

# 文件的读取
# 1、read(num) 默认读取所有的内容
# s = f.read(10)
s2 = f.read()
print(f"{s2,type(s2)}")

# 2、readlines() 读取文件内所有的内容并封装为一个列表 readline() 一次读取一行数据
# l1 = f.readlines()
# print(l1, type(l1))

# 3、for循环读取
# for i in f:
#     print(i)

# time.sleep(5000000)
# 程序运行时会占用文件，需要关闭文件的操作
# 文件的关闭
# f.close()

# 文件的自动关闭 with open
# with open('C:/DSoftware/Python_txt/test.txt', 'r', encoding='UTF-8') as f:
#     # 执行语句
#     for i in f:
#         print(i)   # 当with open中的执行语句执行结束后会自动关闭文件
# time.sleep(5000000)

