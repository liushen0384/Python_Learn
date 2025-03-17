"""
类的内置方法，一般统称为魔术方法

"""

# 创建一个对象类
class Student:
    # name = None  # 记录名字
    # gender = None  # 记录年纪
    # age = None  # 记录年龄    有构造方法这一段声名可以省略

    # 定义一个构造方法
    def __init__(self, name: str, gender: str, age: int):
        self.age = age  # 记录年龄
        self.name = name  # 记录名字
        self.gender = gender  # 记录年纪
        print(f"成功构建了一个类对象:{self.name}")

    # 定义一个__str__魔术方法，用来将类对象中的内容转换为字符串输出
    def __str__(self):  # self表示类本身
        return f"{self.name, self.gender, self.age}"

    # d定义一个__lt__魔术方法，用来实现两个类之间的小于比较
    def __lt__(self, other):
        return self.age < other.age

    # d定义一个__le__魔术方法，用来实现两个类之间的小于等与比较
    def __le__(self, other):
        return self.age <= other.age

    # d定义一个__eq__魔术方法，用来实现两个类之间是否相等
    def __eq__(self, other):
        return (self.age == other.age and self.name == other.name)

stu1 = Student("liushen", "五年级", 24)
stu2 = Student("liushen", "五年级", 24)
print(stu1)
print(stu1 < stu2)
print(stu1 == stu2)
