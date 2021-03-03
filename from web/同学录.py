#用来存储名片的列表
card_infors = []



def print_menu():
    #1. 打印功能提示
    print("="*50)
    print(" 名片管理系统")
    print("1. 增加一个新名片")
    print("2. 删除一个名称")
    print("3. 修改一个名片")
    print("4. 查询一个名片")
    print("5. 显示所有名片")
    print("6. 退出系统")
    print("="*50)


def add_new_card_infor():
        """完成文档输入："""
        new_name = input("请输入新的名字：")
        new_qq = input("请输入新的QQ：")
        new_weixin = input("请输入新的微信：")
        new_addr = input("请输入地址：")

        # 定义一个新的字典，用来存储新的名片
        new_infor = {}
        new_infor['name'] = new_name
        new_infor['qq'] = new_qq
        new_infor["weixin"] = new_weixin
        new_infor['addr'] = new_addr
        global card_infors
        card_infors.append(new_infor)


def find_card_infor():
        find_name = input("请输入要查找的姓名：")

        find_flag = 0   # 默认没有找到

        global card_infors
        for temp in card_infors:
            if find_name == temp["name"]:
               print("%s\t%s\t%s\t%s"%(temp['name'],temp['qq'],temp['weixin'],temp['addr']))
               find_flag=1
               break
        if find_flag == 0:
            print("查无此人")

def show_all_infor():
        """显示所有信息"""
        print("姓名\tQQ\t微信\t住址")
        global card_infors
        for temp in card_infors:
            # print(temp)
            print("%s\t%s\t%s\t%s"%(temp['name'],temp['qq'],temp['weixin'],temp['addr']))


def del_card_infor():
        del_name = input("请输入要查找的姓名：")
        find_flag = 0   # 默认没找到

        global card_infors
        for temp in card_infors:
            if del_name == temp["name"]:
                card_infors.remove(temp)
                find_flag = 1
                show_all_infor()
                break
        if find_flag == 0:
            print("查无此人")


def del_modify_infor():
        modify_name = input("请输入要修改信息的名称：")
        find_flag = 0

        global card_infors
        for temp in card_infors:
            if modify_name == temp["name"]:
                modify_content = input("请输入要修改的信息，如name，qq，weixin，addr等：")
                for name in temp.keys():
                    print("+"*50)
                    print(temp.keys())
                    print("+"*50)
                    print(name)
                    if modify_content == name:
                        modify_value = input("请输入要修改的值：")
                        temp[name] = modify_value
                        show_all_infor()
                        find_flag = 1
                        break

        if find_flag == 0:
            print("查无此人")




def main():
        """完成对整个程序得控制"""

        print_menu()
        while True:
            #2. 获取用户的输入
            num = int(input("请输入操作序号："))

            #3. 根据用户的数据执行相应的功能：
            if num == 1:
                add_new_card_infor()
            elif num == 2:
                del_card_infor()
            elif num == 3:
                del_modify_infor()
            elif num == 4:
                find_card_infor()
            elif num == 5:
                show_all_infor()
            elif num == 6:
                break
            else:
                print("输入有误，请重新输入：")



# 调用主函数
main()