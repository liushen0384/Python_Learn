"""
可以作为注解帮助我们快速编写代码
"""
"""
类型注解只是一个备注，并非决定性的，不会影响代码的运行
"""

import json
import random


class Student:
    name: str = "空"
    age: int = 9  # 类型注解

    # 容器的基础类型注解
    my_list: list = []
    my_tuple: tuple = ()
    my_set: set = set()
    my_dict: dict = {}
    my_str: str = ""

    # 容器的详细类型注解
    my_list_s: list[int] = [1, 2]
    my_tuple_s: tuple[str, int] = ("liushne",3)
    my_set_s: set[int] = {1, 2, 8}
    my_dict_s: dict[str, int] = {"name": 235}
    my_str_s: str = ""

    # 函数的形参、返回值的类型注解
    def fun(self, data: int = 10) -> int: # -> 类型，对函数返回值进行类型注解
        self.age += data
        return self.age

# 类对象的类型注解
stu: Student = Student()

# 通过注释进行类型注解
var1 = 2    # type: int
var2 = "liushne"    # type: str
var3 = random.randint(1,10)    # type: int
var4 = json.loads('{"level": 9}')    # type: dict[str, int]
def fun():
    return 10
var5 = fun()    # type: int

'''
Union联合类型进行类型注解
'''
from typing import Union

my_list: list[Union[int, str]] = [1, "name"]
my_dict: dict[str,Union[int, str]] = {"name": "name", "age": 9}
def fun(self, data: Union[int, float] = 10) -> Union[int, float]:  # -> 类型，对函数返回值进行类型注解
    self += data
    return self