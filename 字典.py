information = {'name': 'Aris',
               'Pho': '1376654238',
               'Adress': 'China'}  # 排版可以写成横或者竖
informationpro = {'age': '18', 'hight': '180'}
# 字典的合并
information.update(informationpro)
print(information)
print(information['name'])  # 第一种输出
print(information.get(input('输入查找的信息:'), '提示:没有这个信息'))  # 第二种.get（查找的内容，没找到后返回的内容）

# 修改数据
information['name'] = 'kEO'
# 添加数据
information['UID'] = '587421-54879-52145'
print(information)
# 数据的删除 pop
c = information.pop('name')
information.pop('UID')
print(information)  # 将会显示被删除的值
print(c)
# popitem
x = information.popitem()  # 显示删掉的字典组
print(x)
# 遍历
for i in information:
    print(i, '=', information[i])
# for x,y in information.keys():
#     print(x,y)
information.setdefault('sex', '男')  # 如果setdefault('a','b') 查找有没有'a'有就输出a没有就添加a，b
print(information)
