# 列表
list = ['松鼠党', '国王', '猎魔人', '狩魔猎人', '巫师', '狂猎']
list1 = ['a','b']
# 查看下标
print(list.index('国王'))

list.append('hehe')  # 添加数据
print(list)

list.insert(2, 'haha')  # 指定位置添加
print(list)
# list.reverse()  # 反转
# print(list)

list.remove('狂猎')  # 移除
print(list)

list.pop(0)
print(list)  # 移除指定位置的

# 合并列表
list.extend(list1)
print(list1)

# ctrl+左键查看更多用法 左边'准心'定位函数列表（准心右边的齿轮状设置要设置'显示成员'）
