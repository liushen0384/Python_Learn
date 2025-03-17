"""
封装：将现实世界中的事物描述为程序中的类的一种思想
在现实世界中有隐藏的属性和行为，在类中也有私有成员变量和私有成员方法
私有变量或方法定义，只需要在方法名前面加__即可
"""
"""
私有成员变量和方法，类对象无法使用，但是类对象内其他成员可以使用
"""

# 创建一个对象类
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

stu1 = Student("liushen", "五年级", 24)
stu1.grade_get("A")
stu1.grade_out("123456789")

