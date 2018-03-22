#!/usr/bin/env python
# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def sendMail(Subject,text,to="960285350@qq.com"):
    ret = True
    try:
        msg = MIMEText(text, 'plain', 'utf-8')
        msg['From'] = formataddr(["15867144598", '15867144598@163.com'])
        msg['To'] = formataddr([to, to])
        msg['Subject'] = Subject

        server = smtplib.SMTP("smtp.163.com",25)
        server.login("15867144598@163.com", "FngJe930128")
        server.sendmail('15867144598@163.com', [to], msg.as_string())
        server.quit()
    except:
        ret =False
    return ret

Subject = input("请输入邮件主题：")
text = input("请输入邮件内容：")
to = input("请输入收件人邮箱：")
rr = sendMail(Subject,text,to)
