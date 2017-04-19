# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 16:33:18 2017

@author: Lily
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText
#==============================================================================
# fromaddr = 'lilyli@qnap.com'
# toaddrs  = 'lily60622@gmail.com'
# msg = "\r\n".join([
#   "From: lilyli@qnap.com",
#   "To: lily60622@gmail.com",
#   "Subject: Just a message",
#   "",
#   "Why, oh why"
#   ])
#==============================================================================
SUBJECT = "Email Data"
EMAIL_FROM = 'lilyli@qnap.com'
EMAIL_TO = ['lily60622@gmail.com', 'lilyli@qnap.com']
msg = MIMEMultipart()
msg['Subject'] = SUBJECT 
msg['From'] = EMAIL_FROM
msg['To'] = ', '.join(EMAIL_TO)
text = "Hi,\n\nHere is the top10 unhelpful pages.\nFYI.\n"
text1 = "Best Regards,\nLily, Li\n\nQNAP Systems, Inc.\n3F, No.22, Zhongxing Rd., Xizhi Dist., New Taipei City, 221, Taiwan\n Tel: 886-2-2641-2000 #11091"
part = MIMEBase('application', "octet-stream")
part1 = MIMEText(text1, 'plain')
part.set_payload(open("eggs.csv", "rb").read())
encoders.encode_base64(part)

part.add_header('Content-Disposition', 'attachment; filename="eggs.csv"')

msg.attach(part)
msg.attach(part1)

username = 'lilyli@qnap.com'
password = 'qnaplily07'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
#server.sendmail(fromaddr, toaddrs, msg)
server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
server.quit()
print('sent!')
#==============================================================================
# import MySQLdb
# 
# try:
#   # 建立DB 連線資訊定設定中文編碼utf-8
#   db = MySQLdb.connect("qnap.dev","root","root","yen_nas",charset='utf8')
# 
# except MySQLdb.Error as e:
#   print ("Error %d: %s" % (e.args[0], e.args[1]))
#==============================================================================
