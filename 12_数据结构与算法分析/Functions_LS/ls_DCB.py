"""
数字电路模拟

"""

class LogicGate:
    """
    父类门电路
    """
    def __init__(self, n):
        self.label = n  # 门电路标签
        self.output = None    # 门电路输出

    def getLabel(self):
        return self.label  # 得到门电路标签

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output   # 得到门电路输出

    def __str__(self):
        return self.label

class BinaryGate(LogicGate):
    """
    # 二元输入类，获取两个引脚（pin）的值
    """
    def __init__(self, n: str):
        super().__init__(n) # 调用父类LogicGate的初始化方法
        self.pinA = None    # 定义两个引脚初始化值为空
        self.pinB = None

    def getPinA(self):
        return int(input(f"Enter Pin A input for gate {self.getLabel()} -->"))

    def getPinB(self):
        return int(input(f"Enter Pin B input for gate {self.getLabel()} -->"))    # 得到两个引脚的输入值

    def setNextPin(self, fgate, n):
        if n == 1:
            self.pinA = fgate.getOutput()
        elif n == 2:
            self.pinB = fgate.getOutput()
        else:
            raise TypeError()


class UnaryGate(LogicGate):
    """
    # 二元输入类，获取两个引脚（pin）的值
    """

    def __init__(self, n: str):
        super().__init__(n)  # 调用父类LogicGate的初始化方法
        self.pin = None  # 定义引脚初始化值为空

    def getPin(self, n = None):
        if n == None:
            return int(input(f"Enter Pin input for gate {self.getLabel()} -->"))  # 得到引脚的输入值
        else:
            return n

    def setNextPin(self, fgate):
        self.pin = fgate.getOutput()

class NotGate(UnaryGate):
    """
    非门
    """
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPin()
        return int(not a)

class OrGate(BinaryGate):
    """
    或门
    """
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a | b:
            return 1
        else:
            return 0

class AndGate(BinaryGate):
    """
    与门
    """
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a & b:
            return 1
        else:
            return 0

class Connector:
    def __init__(self, fgate, tgate, n = 1):
        self.formgate = fgate
        self.togate = tgate
        if isinstance(tgate, NotGate):
            tgate.setNextPin(fgate, n)
        else:
            tgate.setNextPin(fgate)

    def getFrom(self):
        return self.formgate

    def getTo(self):
        return self.togate

if __name__ == "__main__":
    no_gate1 = NotGate("G1")
    print(no_gate1.getOutput())
    # for i in range(5):
    #     or_gate1 = OrGate("G2")
    #     print(or_gate1.getOutput())
    # for i in range(5):
    #     and_gate1 = AndGate("G3")
    #     print(and_gate1.getOutput())
    #     print(and_gate1)