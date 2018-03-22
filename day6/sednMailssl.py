#!/usr/bin/env python
# -*- coding:utf-8 -*-
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText

def send(arg):
    if isinstance(arg,dict):
        # 这里使用SMTP_SSL就是默认使用465端口
        smtp = SMTP_SSL(mail_info["hostname"])
        smtp.set_debuglevel(1)

        smtp.ehlo(mail_info["hostname"])
        smtp.login(mail_info["username"], mail_info["password"])

        msg = MIMEText(mail_info["mail_text"], "plain", mail_info["mail_encoding"])
        msg["Subject"] = Header(mail_info["mail_subject"], mail_info["mail_encoding"])
        msg["from"] = mail_info["from"]
        msg["to"] = mail_info["to"]

        smtp.sendmail(mail_info["from"], mail_info["to"], msg.as_string())

        smtp.quit()
    else:
        return "传入参数不正确！"

if __name__ == '__main__':
    who = input("请输入你的邮箱：")
    passwd = input("授权密码：")
    towho = input("收件人邮箱：")
    subject = input("邮件主题：")
    text = input("邮件内容：")
    mail_info = {
        "from": who,
        "to": towho,
        "hostname": "smtp.163.com",
        "username": who,
        "password": passwd,
        "mail_subject": subject,
        "mail_text": text,
        "mail_encoding": "utf-8"
    }
    send(mail_info)