# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 16:33:18 2017

@author: Lily
"""

import smtplib
fromaddr = 'lilyli@qnap.com'
toaddrs  = 'lily60622@gmail.com'
msg = "\r\n".join([
  "From: lilyli@qnap.com",
  "To: lily60622@gmail.com",
  "Subject: Just a message",
  "",
  "Why, oh why"
  ])
username = 'lilyli@qnap.com'
password = 'lilyshea07'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()

import MySQLdb

try:
  # 建立DB 連線資訊定設定中文編碼utf-8
  db = MySQLdb.connect("qnap.dev","root","root","yen_nas",charset='utf8')

except MySQLdb.Error as e:
  print ("Error %d: %s" % (e.args[0], e.args[1]))