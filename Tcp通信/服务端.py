import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9090))  # 绑定端口号
s.listen(128)  # 设置连接最大数
a, b = s.accept()
s.recv(1024) # 接受小于1024字节的数据
print('a = {},b = {}'.format(a[0], b[1]))
