"""
新的类可以继承老的类的所有属性
"""
"""
class 类名(父类)
    类内容体
    
多继承子类中，同名的属性、方法，先继承的优先，后继承的被覆盖

在继承的子类中，可以复写父类的方法和属性，从而使我们的子类更加完善

复写后，类对象仍然想要调用父类的属性或者方法，可以使用以下方法
1、
父类名.成员变量
父类名.成员方法(self)
2、super函数
super()成员变量
super()成员方法()
"""
"""
pass语句，占位语句
"""
# 父类1
class Student:
    # name = None  # 记录名字
    # gender = None  # 记录年纪
    # age = None  # 记录年龄    有构造方法这一段声名可以省略

    # 定义一个私有成员变量
    __grade = None   # 成绩

    # 定义一个构造方法
    def __init__(self, name: str, gender: str, age: int):
        self.age = age  # 记录年龄
        self.name = name  # 记录名字
        self.gender = gender  # 记录年纪
        print(f"成功构建了一个类对象:{self.name}")

    # 定义一个私有成员方法
    def __grade_out(self):
        print(f"学生的成绩为：{self.__grade}")

    def grade_get(self, grade: str):
        self.__grade = grade

    def grade_out(self, password: str):
        if password == "123456789":
            self.__grade_out()

# 父类2
class Adv:
    level = 1
    strength = 10

    def __init__(self, level: int, strength: int):
        self.level = level
        self.strength = strength

    def punch(self):
        print(f"hp-{self.level + self.strength}")


# 单继承子类
class Student_2(Student):

    # 子类新的变量
    new_id = None  # 学生的学号

    def id(self):
        print(f"{self.name}的学号是{self.new_id}")

# 多继承子类
class character(Student, Adv):
    # 复写父类属性
    level = 10

    # 复写父类方法
    def punch(self):
        # 输出改版前伤害
        Adv.punch(self)
        print(f"改版前等级{super().level}")  # 两种调用父类属性方法的方法

        print(f"hp-{self.level * self.strength}")  # 改版后伤害

# stu = Student_2("lushuai", "四年级",23)
# stu.id()

char = character("lushuai", "四年级",23)
char.punch()