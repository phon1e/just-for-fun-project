import smtplib
import datetime as dt
import random

def send_email_now(data):

	if(check_day_now):
		my_email = "phoniedev2000@gmail.com"
		pwd = "dskbtziwjswnhgdl"
		target = "phoniedummy2000@yahoo.com"

		with smtplib.SMTP("smtp.gmail.com", 587) as connection:
			connection.starttls()
			connection.login(user = my_email, password = pwd)
			connection.sendmail(
				from_addr= my_email, 
				to_addrs = target,
				msg = data
			)

def randPickTxt():
	
	with open("quotes.txt","r") as file:
		data = file.readlines()
		rand_txt = random.choice(data)
		print(rand_txt)
		return rand_txt

def check_day_now():
	now = dt.datetime.now()
	currDay = now.weekday()

	if(currDay == 0):
		return True
	else:
		return False 

send_email_now(randPickTxt())
