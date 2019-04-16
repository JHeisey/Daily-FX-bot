# Daily-FX-bot
Python script which web scrapes daily forex rates and notifies you if any recent rates exceed 2 standard deviations of past 30 days

Requirements: Python 3+
Libraries used: requests, BeautifulSoup, datetime, csv, smtplib, pandas, schedule

TO USE: run main.py, if you want a daily email sent to you, fill in the necessary information in main.py and set 'send_email' to True.

WHAT IT DOES: This program scrapes daily forex rates from x-rates.com, analyzes daily return compared to standard deviation of past 30 days of returns, and will notify you if any rates exceed it. The script will run a function daily and write a summary file to /daily_summaries, as well as append daily rates to /data/hist_rates.csv
