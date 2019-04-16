import requests
from bs4 import BeautifulSoup as BS
from pathlib import Path
from datetime import datetime, timedelta
import csv

n_hist_days = 31

def gen_csv(n_hist_days=31):
	csv_data = []
	for i in range(n_hist_days,0,-1):
		day = datetime.today()-timedelta(days=i)
		day_str = day.strftime('%Y-%m-%d')
		day_url ='https://www.x-rates.com/historical/?from=USD&amount=1&date='+day_str
		day_html = requests.get(day_url).text.split("<span class='ratesTableAlpha'>Alphabetical order</span>")[1]
		day_soup = BS(day_html, "html.parser")
		tds = day_soup.find_all('td')

		if i == n_hist_days:
			names = []
			currs = tds[::3]
			for name in currs:
				name = name.text
				names.append(name)
			csv_data.append(names)

		rates = tds[2::3]
		
		day_rates = []

		for day_rate in rates:
			day_rate = day_rate.text
			day_rates.append(day_rate)
		csv_data.append(day_rates)

	with open("data/hist_rates.csv", "w") as f:
		writer = csv.writer(f)
		writer.writerows(csv_data)
	print("Historical data obtained for last %i days."%n_hist_days)


def daily_update():
	config = Path('data/hist_rates.csv')
	if config.is_file():
	    pass
	else:
		print("Historical data not found, obtaining from x-rates.com...")
		gen_csv(n_hist_days)


	today = datetime.today().strftime('%Y-%m-%d')

	url = 'https://www.x-rates.com/table/?from=USD&amount=1'

	html = requests.get(url).text.split("<span class='ratesTableAlpha'>Alphabetical order</span>")[1]
	soup = BS(html, "html.parser")

	tds = soup.find_all('td')

	today_rates = []
	rates = tds[2::3]

	for day_rate in rates:
		day_rate = day_rate.text
		today_rates.append(day_rate)

	with open('data/hist_rates.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow(today_rates)

	print("Today's currency rates ("+today+") obtained...")