import smtplib
import random
#handling datetime
import datetime as dt
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
date_of_birth = dt.datetime(year,month,day=15,hour=4)

if day_of_week == 5:
  #picking up the random qoute...
  with open("quotes.txt") as qoutes_file:
    all_qoutes = qoutes_file.readlines()
    qoute = random.choice(all_qoutes)
    print(qoute)
    #email sending 
    my_email = "xyz@gmail.com"
    passs ="xyz"
    connection = smtplib.SMTP("smtp.gmail.com",587)
    connection.starttls()
    connection.login(user = my_email , password = passs)
    connection.sendmail(from_addr = my_email , to_addrs= "24cp035@bvmengineering.ac.in" , msg = qoute)
    connection.close()
