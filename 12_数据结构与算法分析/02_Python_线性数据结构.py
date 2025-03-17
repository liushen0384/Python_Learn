"""
栈的python实现
栈是一种线性数据结构的列表
栈的排序原则被称为LIFO（last-in-first-out）,即先进后出

"""
from Functions_LS.ls_Stack import Stack

def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

"""
队列是一种线性数据结构的列表
栈的排序原则被称为FIFO（first-in-first-out）,即先进先出
"""


if __name__ == "__main__":
    a = baseConverter(512, 2)
    print(a)