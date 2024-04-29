import datetime as dt
import smtplib
from random import choice
import flet

import pandas as pd

birthday_person = pd.read_csv("birthdays.csv")

my_email = "😶‍🌫️"  # <---- Your Mail Here
my_password = "☠️☠️☠️☠️☠️"  # <---- Your password here

files = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
path = f"letter_templates/{choice(files)}"

date_now = dt.datetime.now()
today = (date_now.month, date_now.day)
birthday_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in birthday_person.iterrows()}

if today in birthday_dict:
    birthday_values = birthday_dict[today]
    with open(path) as file:
        f = file.read()
        f_update = f.replace('[NAME]', birthday_values['name'])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_values["email"],
                            msg=f"Happy Birthday!\n\n{f_update}")