from datetime import datetime
from pathlib import Path
import smtplib


def notify_user(email, password, body):
	fromaddr = email
	toaddr = email
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.login(fromaddr, password)
	server.sendmail(fromaddr, toaddr, body)
	server.quit()
	print("Summary emailed to "+email+".")

def summarize(summary, send_email=False, email='your_email@somewhere.com', password="your-password"):
	fname = "daily_summaries/"+datetime.today().strftime('%Y-%m-%d')+"_summary.txt"
	summary.insert(0,"Daily summary for "+datetime.today().strftime('%Y-%m-%d')+":")
	summary = '\n'.join(summary)
	with open(fname, "w") as text_file:
		text_file.write(summary)

	if send_email:
		notify_user(email, password, summary)
	print("Summary recorded.")

