"""
socket(简称 套接字)是进程之间通信一个工具,好比现实生活中的插座,所有的家用电器要想工作都是基于插座进行进程之间想要进行网络通信需要socket.
Socket负责进程之间的网络数据传输，好比数据的搬运工
"""

# 创建Socket服务端主要分为如下几个步骤:
# 1.创建socket对象
import socket
socket_server = socket.socket()

# 2.绑定socket server到指定IP和地址
socket_server.bind(("localhost", 8888))

# 3.服务端开始监听端口3.
socket_server.listen(1)    # back1og为int整数，表示允许的连接数量，超出的会等待，可以不填，不填会自动设置一个合理值

# 4.接收客户端连接，获得连接对象
conn, address = socket_server.accept()
# accept方法会发返回一个二元元组，（链接对象 ，对象IP地址）
# accept是一个阻塞方法，如果没有链接，就会使代码停在这里

# 确认成功连结
print(f"接收到客户端连接，连接来自:{address}")

while True:
    # 接受客户端信息，需要使用客户端和服务端的本次链接对象，而非socket_server对象
    data = conn.recv(1024).decode("UTF-8")
    # recv接受的参数是缓冲区大小，一般给1024即可
    # recv方法的返回值是一个字节数组，也就是bytes对象，不是字符串，可以通过decode方法使用UTF-8编码转换为字符串
    print(data)
    # 发送回复消息
    msg = input("请输入回文")
    if msg == "q":
        break
    # msg1 = msg.encode("UTF-8")) # encode方法可以将字符串转换为字节数组
    conn.send(msg.encode("UTF-8"))

# 关闭链接
conn.close()
socket_server.close()