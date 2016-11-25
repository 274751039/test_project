#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
from email.mime.multipart import MIMEMultipart

#定义文件目录
result_dir = 'C:\\Users\\Administrator\\PycharmProjects\\test_project\\report'
lists=os.listdir(result_dir)
#重新按时间对目录下的文件进行排列
lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn))
print ('最新的文件为： '+lists[-1])
file = os.path.join(result_dir,lists[-1])
print file

#发送邮箱
sender = 'hourufen@unionbigdata.com'
#接收邮箱
receiver = 'wangyoulan@unionbigdata.com'
#发送邮件主题
subject = 'Python email test'
#发送邮箱服务器
smtpserver = 'mail.unionbigdata.com' #'smtp.126.com'
#发送邮箱用户/密码
username = 'hourufen@unionbigdata.com'
password = 'hourufen123'
#编写text 类型的邮件正文
# msg = MIMEText('<html><h1>你好！</h1></html>','html','utf-8')
# msg['Subject'] = Header(subject, 'utf-8')

#编写带附件的邮件
msgRoot = MIMEMultipart('related')
#邮件主题
msgRoot['Subject'] = 'Python email test'
#构造附件
att = MIMEText(open(file, 'rb').read(), 'base64','utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="log.txt"'
msgRoot.attach(att)

smtp = smtplib.SMTP()
smtp.connect('mail.unionbigdata.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()