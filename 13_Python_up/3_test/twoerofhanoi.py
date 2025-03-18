"""汉诺塔程序。
一个堆叠移动解谜游戏"""

import sys
import copy

TOLAL_DISKS = 3 #圆盘数。圆盘越多，难度越高

#开始时所有圆盘都在塔A上
SLOVED_TOWER = list(range(TOLAL_DISKS, 0, -1))

def main():
    """运行一局汉诺塔游戏"""
    print(
        """汉诺塔小游戏， 作者LS
将圆盘移动到另一个塔上，每次只能移动一个圆盘，并且不能把大圆盘放到小圆盘上面"""
    )

    towers = {"A": copy.copy(SLOVED_TOWER), "B": [], "C": []} # 初始化圆盘状态

    while True:
        # 展示圆盘状态
        DispalyTowers(towers)

        # 询问玩家移动方向
        fromTower, toTower = getPlayerMove(towers)

        # 将圆盘从fromTower移动到toTwoer上
        disk = towers[fromTower].pop()
        towers[toTower].append(disk)

        # 查询玩家是否完成游戏
        if SLOVED_TOWER in (towers["C"], towers["B"]):
            # 最后一次展示圆盘状态
            DispalyTowers(towers)
            print("恭喜你完成了游戏！！！")
            sys.exit() # 退出游戏

def DispalyTowers(Towers):
    for hight in range(TOLAL_DISKS, 0, -1):
        for tower in Towers: # 逐层显示与塔与圆盘
            if hight > len(Towers[tower]):
                displayRow(0)
            else:
                displayRow(Towers[tower][hight - 1])

        # 输出空，代表着换行
        print()

    emptySpace = " " * TOLAL_DISKS
    # 显示塔的名称
    print('{0}A{0}{0} B{0}{0} C{0}\n'.format(emptySpace))

def displayRow(diskWidth):
    emptySpace = " " * TOLAL_DISKS
    if diskWidth == 0:
        # 没有圆盘时显示塔
        print('{0}|{0}'.format(emptySpace), end = " ")
    else:
        # 当塔上有圆盘时的空格数量
        emptySpace = " " * (TOLAL_DISKS - diskWidth)
        disk = '#' * diskWidth
        # 显示塔上的圆盘
        print(f'{emptySpace}{disk}{diskWidth}{disk}{emptySpace}', end = " ")

def getPlayerMove(Towers):
    """询问玩家移动方向并返回（fromTower， toTower）"""
    while True: # 重复询问玩家直至输入正确的移动方向
        print("请输入移动方向（比如从A->C请输入：AC）：")
        MoveKey = input().upper().strip()
        fromTower, totower = MoveKey[0], MoveKey[1]

        # 检测到玩家输入退出时，退出程序
        if MoveKey == "QUIT":
            sys.exit()

        # 检测到玩家输入正确的移动方向时退出循环，否则继续询问
        if MoveKey not in ("AB", "AC", "BA", "BC", "CA", "CB"):
            print("输入错误！，请再次输入")
            continue

        # 检测移动是否合法
        if len(Towers[fromTower]) == 0:
            # 塔不能为空
            print("塔上没有圆盘！，请重新输入")
            continue
        elif len(Towers[totower]) == 0:
            return  fromTower, totower
        elif Towers[fromTower][-1] > Towers[totower][-1]:
            print("大圆盘不能放置在小圆盘上！，请重新输入")
            continue
        else:
            return fromTower, totower

if __name__ == "__main__":
    main()