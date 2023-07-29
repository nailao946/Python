import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation

# 创建GUI窗口
root = tk.Tk()
root.title("SHUAI")
root.geometry("800x600")

# 创建Matplotlib图形容器
fig = Figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot(111)
line, = ax.plot([], [], '-')

# 创建Matplotlib绘图区域
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# 读取数据并绘制波形图
def update_graph():
    data = []
    with open("shuai.txt", "r") as file:
        lines = file.readlines()
        start = 40 * (int(len(lines) / 40))
        for line in lines[start:]:
            data.append(float(line.strip()))

    x = list(range(len(data)))
    y = data

    ax.clear()
    ax.plot(x, y, '-')
    ax.set_xlabel('MHz')
    ax.set_ylabel('V')
    ax.set_title('SO NIU B')

    canvas.draw()

# 更新图形的动画函数
def animate(i):
    update_graph()

# 创建动画对象
ani = animation.FuncAnimation(fig, animate, interval=1000)

# 启动GUI主循环
tk.mainloop()
