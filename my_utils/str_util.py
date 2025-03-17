__all__ = ["", "str_reverse"]
def str_reverse(string:str):
    """
    j将字符串反转
    :param string:输入的字符串
    :return: 反转后的字符串
    """
    # re = ""
    # i = -1
    # for s in string:
    #     re = re + string[i]
    #     i -= 1
    # return re
    return string[::-1]


def substr(string:str, x:int, y:int):
    """
    对字符串进行切片
    :param string:带切片的字符串
    :param x: 切片开始的下标
    :param y: 切片结束的下标
    :return: 切片后的字符串
    """
    return string[x:y:1]
