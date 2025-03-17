"""
算法分析基础

"""
import timeit

"""
大O记法
O(1) 常数
O(logn) 对数
O(n) 线性
O(nlogn) 线性对数
O(n*2) 平方
O(n*3) 立方
O(2^n) 指数
"""

# 列表常用操作大O效率
"""
索引                      O(1)            
索引赋值                   O(1)
追加                      O(1)
pop()                    O(n)
pop(i)                   O(n)
insert(i, item)          O(n)
删除                      O(n)
遍历                      O(n)
包含                      O(n)
切片                      O(K)
删除切片                   O(n)
设置切片                   O(n+k)
反转                      O(n)
连接                      O(k)
排序                      O(nlogn)
乘法                      O(nk)
"""

# pop() 和 pop(i)性能比较
popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
popend = timeit.Timer("x.pop()", "from __main__ import x")

print("pop(0) pop()")

for i in range(1000000, 100000001, 1000000):
    x = list(range(i))
    pt = popend.timeit(number=1000)
    x = list(range(i))
    pz = popzero.timeit(number=1000)
    print("%15.5f, %15.5f" % (pz, pt))


# 字典操作的大o效率
"""
赋值O(1) 取值O(1) 复制O(n) 删除O(1) 包含O(1) 遍历O(n)
"""