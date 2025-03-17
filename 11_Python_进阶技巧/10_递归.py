"""
递归
递归在编程中是一种非常重要的算法递归:即方法(函数)自己调用自己的一种特殊编程写法如:
def func():
    if ...:
        func()
    return ...
函数调用自己，即称之为递归调用。

"""
import time

# class Solution:
#     def lastRemaining(self, n: int) -> int:
#         return 2*(n//2 + 1 - self.lastRemaining(n//2)) if n>1 else 1
class Solution(object):
    def del_list(self, num_list: list):
        re_num_list = []
        re_num_list = num_list[1::2][::-1]
        if len(re_num_list) == 1:
            pass
        else:
            re_num_list = self.del_list(re_num_list)
        return re_num_list
    def lastRemaining(self, n: int):
        """
        列表 arr 由在范围 [1, n] 中的所有整数组成，并按严格递增排序。请你对 arr 应用下述算法：
            从左到右，删除第一个数字，然后每隔一个数字删除一个，直到到达列表末尾。
            重复上面的步骤，但这次是从右到左。也就是，删除最右侧的数字，然后剩下的数字每隔一个删除一个。
            不断重复这两步，从左到右和从右到左交替进行，直到只剩下一个数字。
        给你整数 n ，返回 arr 最后剩下的数字。
        :type n: int
        :rtype: int
        """
        if n == 1:
            print(1)
        else:
            num_list = list(range(1, n + 1))
            re_num_list = self.del_list(num_list)
            print(int(re_num_list[0]))

if __name__ == "__main__":
    n = int(input("->:"))
    T1 = time.perf_counter()
    s = Solution()
    s.lastRemaining(n)
    T2 = time.perf_counter()
    print('程序运行时间:%s毫秒' % ((T2 - T1) * 1000))