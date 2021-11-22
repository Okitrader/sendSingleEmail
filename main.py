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
df = pd.read_csv('contacts.csv')

print(df)