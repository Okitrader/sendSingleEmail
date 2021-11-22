import yagmail
import os
import pandas as pd

sender_email = 'thewayalgotrading@gmail.com'

subject = """"
This is the subject
"""
contents = """"
Here is the content of the email!
Hi!
"""

yag = yagmail.SMTP(user=sender_email, password=os.getenv('PASSWORD'))

df = pd.read_csv('contacts.csv')
#print(df)

for index, row in df.iterrows():
  contents = f""""
  Hi {row['first_name']} Here is the content of the email!
Hi!
  """
  yag.send(to=row['email'], subject = subject, contents=contents)
  print('Email Sent')
