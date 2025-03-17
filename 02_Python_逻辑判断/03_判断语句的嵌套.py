"""
if语句嵌套使用


"""

# 简单的判断嵌套
if input("请输入密码\n") == "297253":
    print("一级密码正确")
    if input("请输入二级密\n") == "136681":
        print("恭喜登录！")
    else:
        print("密码错误！")
else:
    print("密码错误！")