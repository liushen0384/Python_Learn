"""
单例模式
class Tool:
pass

t1 =To0L()
t2 = To0L()
print(t1)
print(t2)
创建类的实例后,就可以得到一个完整的、独立的类对象。通过print语句可以看出,它们的内存地址是不相同的,即t1和t2是完全独立的两个对象
<__main_-.Tool object at 0x0000027246FCCEE0>
<__main_-.Tool object at 0x0000027246FCD9F0>
某些场景下，我们需要一个类无论获取多少次类对象,都仅仅提供一个具体的实例用以节省创建类对象的开销和内存开销
比如某些工具类，仅需要1个实例，即可在各处使用
这就是单例模式所要实现的效果

"""

#单例模式基本使用
from Singleton import str_tool

s1 = str_tool
s2 = str_tool

print(s1, s2)
