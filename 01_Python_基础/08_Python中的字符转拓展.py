"""
字符串拓展

"""

# 三种定义方式
# 单引号定义
name1 = '卢帅'
print(type(name1),name1)

# 双引号定义
name2 = "柳神"
print(type(name2),name2)

# 三引号定义，有变量接收则为字符串，没有变量接受为多行注释
name3= """
卢帅
柳神
"""
print(type(name3),name3)

# 字符串的引号嵌套
# 1、单引号定义包含双引号
name4 = '"卢帅"'
print(type(name4),name4)

# 2、双引号定义包含单引号
name5 = "'柳神'"
print(type(name5),name5)

# 3、使用转义字符\
name6 = "\"卢帅\""
print(type(name6),name6)


# 字符串拼接
# 变量拼接
name7 = name1 + name2
print(type(name7),name7)

# 字面量与变量拼接
name8 = name1 + "7"
print(type(name8),name8)


# 字符串格式转换
#  通过占位符进行拼接,多个变量占位要用括号括起来并按照顺序排放
# 占位符 % ，%d %s %f  转换为整数、字符串、浮点数插入
age = 25
id = "liushen%s%s" % (name1, age)
print(id)


# 字符串格式化的精度控制 m.n m为字符串长度，.n为小数位数
print("liushen%s%6.2f" % (name1, age))


# 字符串快速格式化  语法f"内容{变量}"，无法控制精度
print(f"liushen{name1}{age}")


# 对表达式进行格式化
# 表达式：有明确执行结果的代码语句
print(f"liushen{1+1}")
print(f"liushen{type(name1)}")