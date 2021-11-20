import yagmail
import os

sender_email = 'thewayalgotrading@gmail.com'
receiver_email = 'thewayalgotrading@gmail.com'

subject = """"
This is the subject
"""
contents = """"
Here is the content of the email!
Hi!
"""

yag = yagmail.SMTP(user=sender_email, password=os.getenv('PASSWORD'))
yag.send(to=receiver_email, subject=subject, contents=contents)
print('Email Sent!')