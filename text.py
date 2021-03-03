import time

print(time.strftime('%Y-%m-%d %H:%M:%S'))
# print(time.asctime())
message = []
while True:
    a = int(input('身份认证系统:\n1.查询用户\n2.录入用户\n3.删除用户\n4.列出所以数据\n5.退出系统\n'))
    # 查找
    if a == 1:
        inname = input('请输入查询的用户:')
        find = 0
        for m in message:
            if m['name'] == inname:
                print(m['name'], m['age'])
                find = 1
                break
        if find == 0:
            print('提示:查无此人!')
            # else:
            #     break
    #  添加
    elif a == 2:
        # input('请输入用户名字：')
        user = {}
        user['name'] = input('请输入用户名字：')
        user['age'] = input('请输入年龄:')
        message.append(user)
        # print(message)
    elif a == 3:
        input('请输入删除的用户：')
    elif a == 4:
        print(message)
    elif a == 5:
        break
