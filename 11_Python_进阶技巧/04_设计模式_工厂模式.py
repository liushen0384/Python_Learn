"""
当需要大量创建一个类的示例时，可以使用工厂模式
即从原生的使用类的构造去创建对象的形式迁移到，基于工厂提供的方法去创建对象的形式

使用工厂类的get person()方法去创建具体的类对象优点:
大批量创建对象的时候有统一的入口，易于代码维护
当发生修改，仅修改工厂类的创建方法即可
符合现实世界的模式，即由工厂来制作产品(对象)
"""

# 工厂模式示例
class person:
    pass

class Worker(person):
    pass

class Student(person):
    pass

class Teacher(person):
    pass

class PersonFactory:
    def get_person(self, P_type):
        if P_type == "Worker":
            return Worker()
        elif P_type == "Student":
            return Student()
        elif P_type == "Teacher":
            return Teacher()
        else:
            return person()

pf = PersonFactory()
worker = pf.get_person("Worker")



