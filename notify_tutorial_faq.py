# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 16:33:18 2017

@author: Lily
"""

import smtplib

gmail_user = 'lilyli@qnap.com'  
gmail_password = 'lilyshea07'

sent_from = gmail_user  
to = ['lily60622@gmail.com', 'lilyli@qnap.com']  
subject = 'OMG Super Important Message'  
body = 'Hey, what\'s up?\n\n- You'

email_text = """\  
From: %s  
To: %s  
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print ('Email sent!')
except:  
    print ('Something went wrong...')