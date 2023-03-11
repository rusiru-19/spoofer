import smtplib
import time
print(
"""
************************************************************************
**								      **
** sssssss ppppppp  oooooo  FFFFF  oooooo  FFFFF  EEEEEEE RRRRRRR     **
** sss     pp   pp  oo  oo  FF     oo  oo  FF     EE      RR   RR     **
** sssssss ppppppp  oo  oo  FFFFF  oo  oo  FFFFF  EEEEEE  RRRRRRR     **
**     sss pp       oo  oo  FF     oo  oo  FF     EE      RR    RR    **
** sssssss pp       oooooo  FF     oooooo  FF     EEEEEEE RR     RR   **
**								      **
**                                         ~DEVELOPED BY A RUSIRU~    **
************************************************************************
"""
)


email_sender = input("[+]enter username to login to smtp: ")
email_password = input("[+]password : ")
smtp_server = input("[+] smtp server: ")
smtp_port = input("port: ")
email_receiver = input("[+]enter the email of receiver: ")
email_subject = input("[+]enter the subject of the email: ")
email_body =  input("[+]enter the body for the email: ")
spoof_email = input("[+] enter spoofing email: ")
print("[+]sending email....")
time.sleep(2)


email_msg = f"""\
From: {spoof_email}
To: {email_receiver}
Subject: {email_subject}

{email_body}
"""

context = smtplib.ssl.create_default_context()

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls(context=context)
    server.login(email_sender, email_password)
    server.sendmail(email_sender, email_receiver, email_msg)
    print("[+] email send successfully!! ")


