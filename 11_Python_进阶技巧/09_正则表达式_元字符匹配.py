"""
在刚刚我们只是进行了基础的字符串匹配，正则最强大的功能在于元字符匹配规则。
单字符匹配:
.  匹配任意1个字符(除了\n)，\.匹配点本身
[] 匹配[]中列举的字符
\d 匹配数字，即0-9
\D 匹配非数字
\s 匹配空白，即空格、tab键
\S 匹配非空白
\w 匹配单词字符，即a-z、A-Z、0-9、_
\W 匹配非单词字符

# 数量匹配
* 匹配前一个规则的字符出现0到∞次
+ 匹配前一个规则的字符出现1到∞次
？ 匹配前一个规则的字符出现0到1次
{m} 匹配前一个规则的字符出现m次
{m, } 匹配前一个规则的字符至少出现m次
{m, n} 匹配前一个规则的字符出现m到n次

边界匹配:
^ 匹配字符串开头
$ 匹配字符串结尾
\b 匹配一个单词的边界
\B 匹配非单词边界

分组匹配:
| 匹配左右任意一个表达式
() 将括号中字符作为一个分组

"""
import re

# # 简单示例:
# # 定义原始字符串
# s='itheima1 @@python2!!666 ##itcast3'
#
# # 找出全部数字:
# print(re.findall(r'\d', s))    #字符串的r标记,表示当前字符串是原始字符串,即内部的转义字符无效而是普通字符
# # 找出特殊字符:
# print(re.findall(r'\W', s))
# # 找出全部英文字母:
# print(re.findall(r'[a-zA-Z]', s))    #[]内可以写:[a-zA-Z0-9]这三种范围组合或指定单个字符如[aceDFG135]

# 经典案例
# 匹配账号，只能由字母和数字组成，长度限制6-10位
# r = r'^[0-9a-zA-z]{6,10}$' # 正则匹配表达式
# s = ['123456789', '52sdsd$#asd', 'sdjasdjawia8wrefe', 'sdasdasda5--', '25639841']
# for i in s:
#     if re.findall(r, i):
#         print(re.findall(r, i))

# 匹配qq号 要求纯数字，长度5-11，首位不为0
# r = r'^[1-9][0-9]{4,10}$'
# s = ['0123456789', '52sdsd$#asd', 'sdjasdjawia8wrefe', 'sdasdasda5--', '25639841', '1392948746']
# for i in s:
#      if re.findall(r, i):
#          print(re.findall(r, i))

# 皮皮额邮箱，只允许qq、163、gmail这三种邮箱地址
r = r'^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$'
s = ['0123456789', '52sdsd$#asd', 'sdjasdjawia8wrefe', 'sdasdasda5--.123@gmail.com', '25639841', '1392948746@qq.com']
for i in s:
    ss = re.findall(r, i)
    if ss:
        print(ss) # findall会将表达式中（）中的匹配结果分组返回
# for i in s:
#     ss = re.match(r, i)
#     if ss:
#         print(ss)