"""
类的构造方法
__init__()方法
在创建类对象的时候，其会自动执行

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
        print("成功构建了一个类对象")

    # 定义一个成员方法
    def up(self, year: int = 1):  # self表示类本身
        self.age += year

    def sound(self):
        import winsound
        winsound.Beep(2000, 3000)


stu = Student("liushen", "五年级", 23)