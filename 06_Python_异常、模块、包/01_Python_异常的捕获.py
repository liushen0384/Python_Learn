"""
异常就是程序运行中出现的错误
异常的捕获的基本语法
try
    可能发生异常的代码
except
    异常发生后补救的代码
else
    没有出现异常时执行的代码
finally
    无论有无异常都要执行的代码，一般用于关闭文件
"""

# 打开一个不存在的文件会出现异常
# try:
#     f = open("C:/DSoftware/Python_txt/bug.txt", "r", encoding="UTF-8")
# except:
#     print("文件不存在")
#     f = open("C:/DSoftware/Python_txt/bug.txt", "w", encoding="UTF-8")

# 捕获指定的异常
# try:
#     f = open("C:/DSoftware/Python_txt/bug.txt", "r", encoding="UTF-8")
# except NameError as e:  # e记录了异常的具体类型
#     print(e)
#     f = open("C:/DSoftware/Python_txt/bug.txt", "w", encoding="UTF-8")


# 捕获多个异常
# try:
#     f = open("C:/DSoftware/Python_txt/bug.txt", "r", encoding="UTF-8")
# except (NameError, ZeroDivisionError)as e:  # e记录了异常的具体类型
#     print(e)
#     f = open("C:/DSoftware/Python_txt/bug.txt", "w", encoding="UTF-8")

# 捕获所有的异常
try:
    f = open("C:/DSoftware/Python_txt/bug.txt", "r", encoding="UTF-8")
except Exception as e:  # e记录了异常的具体类型：Exception代表所有异常
    print(e,type(e))
    f = open("C:/DSoftware/Python_txt/bug.txt", "w", encoding="UTF-8")
