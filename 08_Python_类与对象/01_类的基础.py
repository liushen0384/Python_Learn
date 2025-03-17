"""
类由两部分组成
1、类的属性：成员属性
2、类的行为：成员方法

"""

# 创建一个对象类
class Student:
    name = None  # 记录名字
    gender = None  # 记录年纪
    age = None  # 记录年龄

    # 定义一个成员方法
    def up(self, year: int = 1):  # self表示类本身
        self.age += year

    def sound(self):
        import winsound
        winsound.Beep(2000, 3000)



# 声名一个对象
class1 = Student()

# 录入对象属性
class1.name = "lushuai"
class1.gender = "毕业"
class1.age = 24

print(class1.age, class1.name, class1.gender)
print("一年后")
class1.up(6)
print(f"{class1.name}今年{class1.age}")

class1.sound()