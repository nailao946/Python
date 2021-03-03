import smtplib  # smtp服务器
from email.mime.text import MIMEText  # 邮件文本


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
