"""
递归的应用
"""
# 通过递归实现数制转换
def tostr(decnumber, base): #
    digits = "0123456789ABCDEF"
    if decnumber < base:
        return digits[decnumber]
    else:
        return tostr(decnumber // base, base) + digits[decnumber % base]


# 汉诺塔问题
def move(fromT, toT):
    print("moving disk from", fromT, "to", toT)
def moveTower(height, fromT, toT, withT):
    if height >= 1:
        moveTower(height - 1, fromT, withT, toT)
        move(fromT, toT)
        moveTower(height - 1, withT, toT, fromT)

# 谢尔平斯基三角
from turtle import *

def drawTriangle(points, color, myTurtle): # 绘制三角形的函数
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1])
    myTurtle.goto(points[2])
    myTurtle.goto(points[0])
    myTurtle.end_fill()

def getMid(p1, p2): # 获取中位点
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points, degree, myTurtle):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    drawTriangle(points, colormap[degree], myTurtle)
    if degree > 0:
        sierpinski((points[0], getMid(points[0], points[1]), getMid(points[0], points[2])),
                   degree - 1, myTurtle)
        sierpinski((points[1], getMid(points[0], points[1]), getMid(points[1], points[2])),
                   degree - 1, myTurtle)
        sierpinski((points[2], getMid(points[0], points[2]), getMid(points[1], points[2])),
                   degree - 1, myTurtle)

# 贪婪算法


if __name__ == "__main__":
    # print(tostr(6, 2))
    # moveTower(5, "1", "2", "3")

    myTurtle = Turtle()
    myWin = myTurtle.getscreen()
    myPoints = [(-400, -200), (0, 400), (400, -200)]
    sierpinski(myPoints, 6, myTurtle)
    myWin.exitonclick()


