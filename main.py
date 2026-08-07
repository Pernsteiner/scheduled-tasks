##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import random
import datetime as dt
import pandas
import os

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")


letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

now = dt.datetime.now()
day = now.day
month = now.month

data = pandas.read_csv("birthdays.csv")
birthday_days = data.day.tolist()
birthday_months = data.month.tolist()
#message = ""
if day in birthday_days and month in birthday_months:
    print("Hey")
    relevant_data1 = data[data.day == day ]
    relevant_data = relevant_data1[relevant_data1.month == month]
    for (index, row) in relevant_data.iterrows():
        with open(random.choice(letters)) as letter:
            content = letter.read()
            message = content.replace("[NAME]", row["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=row.email, msg=f"Subject: Happy Birthday\n\n{message}")


        






