from rate_analysis import analysis
from scraper import gen_csv, daily_update
from daily_summary import notify_user, summarize
import schedule
import time

# If a daily email notification is desired, fill out
# the necessary fields in string format, and turn
# send_email=False to True.
email = ""
password = ""

def fx_daily_bot(hist_return_days=30, send_email=False, email=email, pw=password):
	daily_update()
	summary = analysis()
	summarize(summary, send_email=send_email, email=email, password=password)

#Script will run every day at 8:00 AM
# schedule.every().day.at("08:00").do(fx_daily_bot)
schedule.every().day.at("08:00").do(fx_daily_bot)

while True:
	schedule.run_pending()
	time.sleep(5)

