"""
Python操作mysql数据库
"""

from pymysql import Connection

#构建到mysql数据库的连接
conn = Connection(
    host = "localhost", # 主机名
    port = 3306,         # 端口
    user = "root",       #账户名
    password = "123456",  #密码
    autocommit = True    # 设置为自动确认
)

print(conn.get_server_info())

# 执行非查询性质的语句

# 获取游标对象
cursor = conn.cursor()

# 选择数据库
conn.select_db("genshinimpact")

# 执行sql语句
# cursor.execute("create table test(num int,value varchar(100));")
# cursor.execute("select * from figure")

# 执行插入语句
cursor.execute("insert into figure values('云堇',6,8,90);")
# conn.commit() # 确认插入语句

# 获取执行结果
# results = cursor.fetchall()
# for i in results:
#     print(i)

# 关闭连结
conn.close()
