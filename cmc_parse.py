from bs4 import BeautifulSoup
import os
import glob
import pandas as pd

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

df = pd.DataFrame()

for one_file_name in glob.glob("html_files/*.html"):
	# one_file_name = "html_files/coinmarketcap20200929132624.html"
	print(one_file_name)
	scrape_time = os.path.basename(one_file_name).replace("coinmarketcap","").replace(".html","")
	f = open(one_file_name, "r")
	soup = BeautifulSoup(f.read(), "html.parser")
	f.close()

	currencies_table = soup.find("tbody")
	currency_rows = currencies_table.find_all("tr")

	for r in currency_rows:
		currency_columns = r.find_all("td")
		if len(currency_columns)>10:
			currency_price = currency_columns[3].find("a", {"class": "cmc-link"}).text.replace("$","").replace(",","")
			currency_name = currency_columns[2].find("p").text
			currency_symbol = currency_columns[2].find("p", {"class": "coin-item-symbol"}).text
			currency_marketcap = currency_columns[6].find("p").text.replace("$","").replace(",","")
			currency_link = currency_columns[2].find("a")["href"]
			df = df.append({
					'time': scrape_time,
					'name': currency_name,
					'price': currency_price,
					'symbol': currency_symbol,
					'marketcap': currency_marketcap,
					'link': currency_link
				}, ignore_index=True)


df.to_csv("parsed_files/coinmarketcap_dataset.csv")
