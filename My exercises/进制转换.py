in1 = input("输入需要转化的内容：")
in2 =int(input("输入需要转化数据的进制(2-8-10-16):"))
in3 = input("输入转化后的进制(2-8-10-16):")
# print(oct(int(in1, in2)))
# in1数据
# in2转化前
# in3转化后
if in3 == "2":
    print(bin(int(in1, in2)))
elif in3 == '8':
    print(oct(int(in1, in2)))
elif in3 == '10':
    print(int(in1, in2))
elif in3 == '16':
    print(hex(int(in1, in2)))