"""
绝大多数编程语言,都允许多线程编程，Pyhton也不例外。
Python的多线程可以通过threading模块来实现。
import threading
thread obj = threading.Thread([group [, target [, name [, args [, kwargs]]]]])
- group:暂时无用，未来功能的预留参数
- target:执行的目标任务名
- args:以元组的方式给执行任务传参
- kwargs:以字典方式给执行任务传参
- name:线程名，一般不用设置
# 启动线程，让线程开始工作
thread_obj.start()

"""
import time
import threading

# 定义可执行单元
def sha():
    while True:
        print("杀！")
        time.sleep(1)

def pao():
    while True:
        print("跑！")
        time.sleep(1)

# 定义可传参执行单元
def unkonw(msg):
    while True:
        print(msg)
        time.sleep(1)



# 多线程编程实现
if __name__ == '__main__':
    # # 杀的线程任务创建
    # sha_thread = threading.Thread(target = sha)
    # # 跑的线程任务创建
    # pao_thread = threading.Thread(target = pao)
    # # 启动线程
    # pao_thread.start()
    # sha_thread.start()

    # 可传参线程任务创建
    unkonw_thread1 = threading.Thread(target = unkonw, args = ("饶命！",))
    unkonw_thread2 = threading.Thread(target=unkonw, kwargs={"msg": "找死！"})
    # 启动线程
    unkonw_thread2.start()
    unkonw_thread1.start()
    # time.sleep(30)
    # pao_thread.
