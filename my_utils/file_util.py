__all__ = ["print_file_info", "append_to_file"]

def print_file_info(name:str):
    """
    将给定路径文件中的内容打印输出
    :param name: 文件的路径
    :return: none
    """
    f = None
    try:
        f = open(name, "r", encoding="UTF-8")
        count =f.read()
        print(count)
    except Exception as e:
        print("文件不存在！")
    finally:
        if f:
            f.close()

def append_to_file(name:str, date:str):
    """
    将指定数据追加到指定路径的文件中
    :param name: 需要添加数据的文件路径
    :param date: 添加的指定数据
    :return: none
    """
    f = open(name, "a")
    f.write(date)
    f.flush()
    f.close()

if __name__ == "__main__":
    print("测试")