"""
分数类

"""
import re
def gcd(a, b):
    """
    通过欧几里得算法求两个数的最大公因数(greatest common divisor)
    :param a: 数a
    :param b: 数b
    :return: a 与 b的最大公因数
    """
    if a % b != 0:
        newa = b
        newb = a % b
        return gcd(newa, newb)
    else:
        return b

class Fraction:

    def __init__(self, top, bottom):
        """
        定义一个分数类
        :param top: 分子
        :param bottom: 分母
        """
        if (top % 1) == 0 | (bottom % 1) == 0:
            common = gcd(abs(top), abs(bottom))
            if top * bottom < 0:
                self.num = abs(top) // common * (-1)
                self.den = abs(bottom) // common
            else:
                self.num = abs(top) // common
                self.den = abs(bottom) // common
        else:
            raise TypeError("Error: 请确保输入的参数为整数！")

    # def __init__(self, n):
    #     """
    #     定义一个分数类
    #     :param n: 分数
    #     """
    #     # if re.findall(r'[1-9][0-9]*/[0-9]*', n):
    #     #     top = int(n.split('/')[0])
    #     #     bottom = int(n.split('/')[1])
    #     # else:
    #     #     raise TypeError("Error: 请输入正确的分数格式 \'num1/num2\'")
    #     common = gcd(top, bottom)
    #     self.num = top // common
    #     self.den = bottom // common

    def __str__(self):
        """
        print输出调用重写
        :return: 返回一个分数值
        """
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        """
        加法逻辑重写
        :param other: 另外一个分数类对象
        :return: 二者相加的结果
        """
        newnum = self.den * other.num + self.num * other.den
        newden = self.den * other.den
        common = gcd(newden, newnum)
        return  Fraction(newnum // common, newden // common)

    def __sub__(self, other):
        """
        减法逻辑重写
        :param other: 另外一个分数类对象
        :return: 二者相减的结果
        """
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return  Fraction(newnum // common, newden // common)

    def __mul__(self, other):
        """
        乘法逻辑重写
        :param other: 另外一个分数类对象
        :return: 二者相乘的结果
        """
        newnum = self.num * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __truediv__(self, other):
        """
        除法逻辑重写
        :param other: 另外一个分数类对象
        :return: 二者相除的结果
        """
        newnum = self.num * other.den
        newden = self.den * other.num
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __eq__(self, other):
        """
        等于逻辑重写
        :param other: 另一个分数
        :return: 二者是否相等
        """
        num1 = self.num * other.den
        num2 = self.den * other.num
        return num1 == num2

    def __ne__(self, other):
        """
        不等于逻辑重写
        :param other: 另一个分数
         :return: 二者是否不相等
        """
        num1 = self.num * other.den
        num2 = self.den * other.num
        return num1 != num2

    def __gt__(self, other):
        """
        大于逻辑运算
        :param other: 另外一个分数
        :return: 前者是否大于后者
        """
        return True if self.num * other.den > self.den * other.num else False

    def __ge__(self, other):
        """
        大于等于逻辑运算
        :param other: 另外一个分数
        :return: 前者是否大于等于后者
        """
        return True if self.num * other.den >= self.den * other.num else False

    def __lt__(self, other):
        """
        小于逻辑运算
        :param other: 另外一个分数
        :return: 前者是否小于后者
        """
        return True if self.num * other.den < self.den * other.num else False

    def __le__(self, other):
        """
        小于等于逻辑运算
        :param other: 另外一个分数
        :return: 前者是否小于后者
        """
        return True if self.num * other.den <= self.den * other.num else False

    def getNum(self):
        """
        得到分数的分子
        :return: 分子的值：int
        """
        return self.num

    def getDen(self):
        """
        得到分数的分母
        :return: 分母的值：int
        """
        return self.den


if __name__ == "__main__":
    a = Fraction(-2, -8)
    b = Fraction(-3, 9)
    print(a, b)
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a > b)
    print(a == b)

