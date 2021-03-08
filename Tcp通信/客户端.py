import socket
# 建立服务器连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接指定服务器的主机和端口
s.connect(('', 9090))
# 用指定编码发送
s.send(''.encode())
