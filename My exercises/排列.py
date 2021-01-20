up = int(input('请输入 A 上标：'))
down = int(input('请输入 A 下标：'))
n = 1
for i in range(0, down):
    n = n * up
    up = up - 1
print(n)
