"""
if语句的基本使用

"""

# if语句基本格式
"""
if 判断的条件:
    条件为真时执行的行动
"""

password = input("请输入密码\n")
if password == "297253":
    print("恭喜登入！")


# if else语句组合使用
password = input("请输入密码\n")
if password == "297253":
    print("恭喜登入！")
else:
    print("密码错误！")


# elif多重判断举例
password = input("请输入密码\n")
if password == "297253":
    print("恭喜登入！")
elif password == "136681":
    print("进入隐藏空间！")
else:
    print("密码错误！")

# input可以集成到if语句中
if input("请输入密码\n") == "297253":
    print("一级密码正确")
    if input("请输入二级密\n") == "136681":
        print("恭喜登录！")
    else:
        print("密码错误！")
else:
    print("密码错误！")