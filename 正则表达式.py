import re

# match 查找字符串

a = r'absg\\\\cuqnd'
s = re.search(r'\\', a)
m = re.match('cu', a)
# print(s ,'|||',  m)


# group 的使用
b = '0doiaw1dnoaw2wad3rqw'
s1 = re.search('(?P<group1>0.*)(1.*)(2.*)', b)
# print(s1.group(0))
# print(s1.group(group1)) # 除了可以使用序列还可以使用组名字
# print(s1.group(1))
# print(s1.group(2))
# print(s1.groupdict())  # 如上使用?P<name>可以给分组取名
c = 'https://www.bilibili.com/video/BV1HD4y1S7FH?p=233'
s2 = re.search(r'https://.*\/.*', c)
print(s2)
