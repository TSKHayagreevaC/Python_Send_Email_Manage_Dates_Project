# import smtplib
#
# my_email = "srikanthhayagreeva1993@gmail.com"
# password = "Hayasri@1993"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="srikanthhayagreeva@yahoo.com",
#         msg="Subject:Hello\n\nThis Is The Body Of My Email.")

# Working With Date Time Module...

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
# # if year == 2021:
# #     print("Wear A Face Mask")
# # print(type(now))
#
# date_of_birth = dt.datetime(year=1993, month=12, day=15, hour=4)
# print(date_of_birth)

# Send Motivational Quote On Monday Code

# import datetime as dt
# import datetime as dt
# import random
# import smtplib
#
# MY_EMAIL = "srikanthhayagreeva1993@gmail.com"
# MY_PASSWORD = "Hayasri@1993"
#
# now = dt.datetime.now()
# weekday = now.weekday()
# if weekday == 5:
#     with open("quotes.txt") as quotes_file:
#         all_quotes = quotes_file.readlines()
#         quote = random.choice(all_quotes)
#
#     print(quote)
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=MY_PASSWORD,
#             msg=f"Subject:Monday Motivation\n\n{quote}")

# BirthDay Wishing Code

from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "srikanthhayagreeva1993@gmail.com"
MY_PASSWORD = "Hayasri@1993"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birth Day...!\n\n{contents}"
        )

