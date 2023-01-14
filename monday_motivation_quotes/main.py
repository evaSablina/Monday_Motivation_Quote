import datetime as dt
import random
import smtplib

MY_EMAIL = "garaninaeva300@gmail.com"
PASSWORD = "sbxytclwvmidlicr"

now = dt.datetime.now()
day_of_the_week = now.weekday()
if day_of_the_week == 0:
    with open("quotes.txt") as quote:
        all_quotes = quote.readlines()
        random_quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Motivation Quote\n\n{random_quote}."
        )

# if day_of_the_week == 0:
#     day_of_the_week = "Monday"
# elif day_of_the_week == 1:
#     day_of_the_week = "Tuesday"
# elif day_of_the_week == 2:
#     day_of_the_week = "Wednesday"
# elif day_of_the_week == 3:
#     day_of_the_week = "Thursday"
# elif day_of_the_week == 4:
#     day_of_the_week = "Friday"
# elif day_of_the_week == 5:
#     day_of_the_week = "Saturday"
# elif day_of_the_week == 6:
#     day_of_the_week = "Sunday"
