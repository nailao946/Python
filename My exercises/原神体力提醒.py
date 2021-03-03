import datetime
import time
from win10toast import ToastNotifier
import smtplib  # smtp服务器
from email.mime.text import MIMEText  # 邮件文本
import apscheduler
import os

# 邮件构建
def xsendmail():
    subject = "树脂已经满了!!!"  # 邮件标题
    sender = "1499964238@qq.com"  # 发送方
    content = "周本" \
              "世界Boss" \
              "副本" \
              "地脉"
    recver = "2224357710@qq.com"  # 接收方
    password = "ajbdtkdyklfohcbj"  # 输入SMTP授权码，不是你的邮箱密码
    message = MIMEText(content, "plain", "utf-8")
    # content 发送内容     "plain"文本格式   utf-8 编码格式

    message['Subject'] = subject  # 邮件标题
    message['To'] = recver  # 收件人
    message['From'] = sender  # 发件人

    smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 实例化smtp服务器
    smtp.login(sender, password)  # 发件人登录
    smtp.sendmail(sender, [recver], message.as_string())  # as_string 对 message 的消息进行了封装
    smtp.close()

a = input('输入当前剩余树脂：')
if 161 > int(a) > -1:
    c = 160 - int(a)
    xtime = c * 8 * 60
    Nowtime = time.time()  # 读取当前秒时间戳
    Endtime = Nowtime + xtime  # 加上树脂等待的时间
    tupTime = time.localtime(Endtime)  # 格式化时间戳为本地时间
    stadardTime = time.strftime("%Y-%m-%d %H:%M:%S", tupTime)  # 函数接收以时间元组，并返回以可读字符串表示的当地时间
    print(stadardTime)
else:
    print('提示:请输入正确的树脂数量！')

toaster = ToastNotifier()

# 有icon的版本
toaster.show_toast("您的原神树脂已经满了呢！",
                   "开始肝了老弟!",
                   icon_path="yuanshen.ico",
                   duration=10)
while toaster.notification_active(): time.sleep(0.1)
