"""
socket(简称 套接字)是进程之间通信一个工具,好比现实生活中的插座,所有的家用电器要想工作都是基于插座进行进程之间想要进行网络通信需要socket.
Socket负责进程之间的网络数据传输，好比数据的搬运工
"""

# 主要分为如下几个步骤:
# 1.创建socket对象
import socket
socket_client = socket.socket()

# 2.连接到服务端
socket_client.connect(("localhost", 8888))

# 3.发送消息
while True:
    # 可以通过无限循环来确保持续的发送消息给服务端send_msg = input("请输入要发送的消息")if send _msg ='exit':
    # 通过特殊标记来确保可以退出无限循环break
    msg = input("->:")
    if msg == "q":
        break
    socket_client.send(msg.encode("UTF-8"))
    # 消息需要编码为字节数组(UTF-8编码)

    # 接受返回消息
    recv_data = socket_client.recv(1024).decode("UTF-8")    # 传入参数为缓冲区的大小，recv同样为阻塞函数
    print(recv_data)

# 关闭链接
