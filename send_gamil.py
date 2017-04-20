# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 09:59:23 2017

@author: Lily
"""

#!/usr/bin/env python
"""
python_3_email_with_attachment.py
Created by Robert Dempsey on 12/6/14.
Copyright (c) 2014 Robert Dempsey. Use at your own peril.

This script works with Python 3.x

NOTE: replace values in ALL CAPS with your own values
"""

import sys
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

COMMASPACE = ', '

def main():
    sender = 'lilyli@qnap.com'
    gmail_password = 'qnaplily07'
    recipients = ['lily60622@gmail.com', 'lilyli@qnap.com']
    
    # Create the enclosing (outer) message
    outer = MIMEMultipart()
    outer['Subject'] = 'Top10 unhelpful Tutorial & FAQ'
    outer['To'] = COMMASPACE.join(recipients)
    outer['From'] = sender
    outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'
    body = """
    Hi,
    
    Here is the top10.
    FYI.
    
    Best Regards,
    Lily, Li
    QNAP Systems, Inc.
    3F, No.22, Zhongxing Rd., Xizhi Dist., New Taipei City, 221, Taiwan
    Tel: 886-2-2641-2000 #11091
    """    
    outer.attach(MIMEText(body, 'plain'))     
#    text1 = ""
#    text2 = "Hi,\nHere is the top10.\nFYI.\n\nBest Regards,\nLily, Li\n\nQNAP Systems, Inc.\n3F, No.22, Zhongxing Rd., Xizhi Dist., New Taipei City, 221, Taiwan\n Tel: 886-2-2641-2000 #11091"

   
    # List of attachments
    attachments = ['unhelpful_tutorial.csv', 'unhelpful_faq.csv']

    # Add the attachments to the message
    for file in attachments:
        try:
            with open(file, 'rb') as fp:
                msg = MIMEBase('application', "octet-stream")
                msg.set_payload(fp.read())
            encoders.encode_base64(msg)
            msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
            outer.attach(msg)

        except:
            print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
            raise



    composed = outer.as_string()

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(sender, gmail_password)
            s.sendmail(sender, recipients, composed)
            s.close()
        print("Email sent!")
    except:
        print("Unable to send the email. Error: ", sys.exc_info()[0])
        raise

if __name__ == '__main__':
    main()