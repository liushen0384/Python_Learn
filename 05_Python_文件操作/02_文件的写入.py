"""
三个步骤
1、打开文件
f = open("名称", "打开方式", "编码格式")
2、写入数据
f.write("数据") # 实际上该代码只是将数据写入到了内存中的某一个地方
3、内容刷新
f.flush()   # 刷新内容后，才真正的将数据写入到了文件中

"""
import time

# # 文件的写入
# f = open("C:/DSoftware/Python_txt/new_test.txt", "w", encoding="UTF-8")
#
# f.write("新的开始")
#
# # f.flush()
#
# f.close() # close方法中内置flush方法


# 文件的追加写入模式
f = open("C:/DSoftware/Python_txt/new_test.txt", "a", encoding="UTF-8")

f.write("lushuai")

f.flush()

f.close()