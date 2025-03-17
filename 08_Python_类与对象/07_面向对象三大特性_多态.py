"""
多态
"""

"""
多态：指的是多种状态，及完成某个行为时，使用不同的对象会得到不同的状态

函数形参以父类做定义声名，以子类做实际传入对象，用以获得同一行为，不同的状态

函数的多态多体现于抽象类的使用上
"""


# 抽象类，指的是有抽象方法的类，多用于做顶层设计
class Animal:
    def speak(self):
        pass  # 函数体为空实现即为抽象类

class Cat(Animal):
    def speak(self):
        print("喵喵喵")

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

def speak(animal: Animal):
    animal.speak()

cat = Cat()
dog = Dog()
speak(cat)
speak(dog)
