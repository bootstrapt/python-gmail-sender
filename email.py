#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders

def mail(to, subject, text, attach):
  msg = MIMEMultipart()

  gmail_user = "{GMAIL EMAIL ADDRESS}"
  gmail_pwd = "{GMAIL PASSWORD}"
  msg['From'] = gmail_user
  msg['To'] = to
  msg['Subject'] = subject

  msg.attach(MIMEText(text))

  part = MIMEBase('application', 'octet-stream')
  part.set_payload(open(attach, 'rb').read())
  Encoders.encode_base64(part)
  part.add_header('Content-Disposition',
         'attachment; filename="%s"' % os.path.basename(attach))
  msg.attach(part)

  mailServer = smtplib.SMTP("smtp.gmail.com", 587)
  mailServer.ehlo()
  mailServer.starttls()
  mailServer.ehlo()
  mailServer.login(gmail_user, gmail_pwd)
  mailServer.sendmail(gmail_user, to, msg.as_string())
  # Should be mailServer.quit(), but that crashes...
  mailServer.close()


def main():

  mail("{TO EMAIL}",
     "{SUBJECT}",
     "{BODY}",
     "{OPTIONAL: ATTACHMENT}")
  
if __name__ == '__main__':
	main()