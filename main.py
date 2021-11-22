import yagmail
import os
import pandas as pd

sender_email = 'thewayalgotrading@gmail.com'

yag = yagmail.SMTP(user=sender_email, password=os.getenv('PASSWORD'))

df = pd.read_csv('contacts.csv')

for index, row in df.iterrows():
  receiver_email = row['email']
  subject = 'This is the subject'
  contents = [f"""
  Hey, {row['first_name']} you have to pay {row['amount']}
  Bill is attached!""",
  row['filepath']
  ]
  yag.send(to=row['email'], subject = subject, contents=contents)
  print('Email Sent')
