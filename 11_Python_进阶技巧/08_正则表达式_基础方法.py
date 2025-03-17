"""
正则表达式
正则表达式，又称规则表达式(Reqular Expression),是使用单个字符串来描述、匹配某个句法规则的字符串,常被用来检索、替换那些符合某个模式(规则)的文本。
简单来说,正则表达式就是使用字符串定义规则,并通过规则去验证字符串是否匹配。
比如,验证一个字符串是否是符合条件的电子邮箱地址,只需要配置好正则规则,即可匹配任意邮箱。
比如通过正则规则:(^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$)即可匹配一个字符串是否是标准邮箱格式
但如果不使用正则，使用if else来对字符串做判断就非常困难了，

"""
import re
# 正则的三个基础方法
# Python正则表达式,使用re模块,并基于re模块中三个基础方法来做正则匹配。分别是: match、search、findall三个基础方法

s1 = 'keli keqing diluke aleiqinuo keli diluke'
s2 = '1keli keqing diluke aleiqinuo keli diluke'

# # 1.re.match(匹配规则，被匹配字符串)从被匹配字符串开头进行匹配，匹配成功返回匹配对象(包含匹配的信息)匹配不成功返回空
# result =re.match('keli',s1)
# print(result) # <re.Match object;span=(0,4),match='keli'>
# print(result.span()) # (0，4)
# print(result.group()) # keli
#
# result =re.match('python',s2)
# print(result) # None

# 2.search(匹配规则，被匹配字符串)搜索整个字符串,找出匹配的。从前向后,找到第一个后,就停止,不会继续向后
# result = re.search('keli', s2)
# print(result)    #<re.Match object; span=(1，5)，match='keli'>
# print(result.span())    #(1，5)
# print(result.group())     # keli
# # 整个字符串都找不到，返回None
# s2 = 'keqing diluke'
# result = re.search('keli', s2)
# print(result) # None

# 3.findall(匹配规则，被匹配字符串)匹配整个字符串，找出全部匹配项
result = re.findall('keli', s2)
print(result) # ['keli', 'keli']
# 找不到返回空 list:[]
result = re.findall('itcast', s2)
print(result)  #[]