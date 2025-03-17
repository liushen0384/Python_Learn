"""
字符串类型转换语句
int()  float()  str()

"""
# 循环结构
for i in range(10000):
    num = input()
    if num == "q":
        break
    a = int(num)
    print(type(a),a)

# 浮点数转小数会丢失精度