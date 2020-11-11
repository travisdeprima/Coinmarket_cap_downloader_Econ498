# ECON498_midterm

## Contents
- [Introduction](https://github.com/travisdeprima/ECON498_midterm/new/master?readme=1#introduction)
- [Technologies](https://github.com/travisdeprima/ECON498_midterm/new/master?readme=1#technologies)
- [Installation](https://github.com/travisdeprima/ECON498_midterm/new/master?readme=1#installation)
- [Usage](https://github.com/travisdeprima/ECON498_midterm/new/master?readme=1#usage)
  - [Step 1](https://github.com/travisdeprima/ECON498_midterm/new/master?readme=1#step-1)
  - [Step 2](https://github.com/travisdeprima/ECON498_midterm/new/master?readme=1#step-2)
  - [Step 3](https://github.com/travisdeprima/ECON498_midterm/new/master?readme=1#step-3)
- [Limitations and Issues](https://github.com/travisdeprima/ECON498_midterm/new/master?readme=1#limitations-and-issues)

## Introduction
This code scrapes and parses 500 cryptocurrencies from [CoinMarketCap](https://coinmarketcap.com/) 8 times every 15 minutes over the span of 2 hours. Then the program creates a CSV file that, in turn, is used to create summary statistics that calculate the mean, median, max, min, variance, and standard deviation of the cryptocurrencies over the time period. 
## Technologies
This program was written in Python version 3.7.6. Earlier versions of Python might not be up-to-date with the code provided in the program. Along with this, packages like pandas, glob, BeautifulSoup(bs4), urllibrequest, sklearn, and matplotlib should be installed. 
## Installation
To install the program onto your computer, you can write the provided request into your terminal: 
```
pip install https://github.com/travisdeprima/ECON498_midterm.git
```
## Usage
After installing the program onto your computer we then run can run the file

#### Step 1:

First off we have our request file in which we've imported the following packages:
``` 
import urllib.request
import os
import datetime
import time
```
Then the program creates a new file titled ```html_files```, which will store all of our request files from CoinMarketCap. 
```
if not os.path.exists("html_files"):
    os.mkdir("html_files")
```
The current state of this program is written to collect 100 cryptocurrencies from CoinMarketCap, but note that I have commented out 4 other "For loops" that can be uncommented simply by highlighting them and using the 'shift+option+a' command on Mac or simply by deleting ```"""``` that surrounds the code. 

Along with this, the user also has the ability to set whatever time he/she pleases by changing the ```for i in range(8):``` and changing the ```time.sleep(900)``` to resemble the time frame in which the user wants to sleep for. It is currently programmed to collect data every 15 minutes over the span of 2 hours but this can be changed by doing the former. 

Once the request file is run, a folder should be created titled "html_files" and this is where your computer will place the html files the user has requested. 

#### Step 2:

Now that the user has scraped the html files from CoinMarketCap, we can noe parse the files. 

We use the following packages in this file:
```
from bs4 import BeautifulSoup
import os
import glob
import pandas as pd
```
Just like the request file, the parse file will create a folder titled ```pased_files```
```
if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")
```
Then the program parses the html files that were requested and placed into the ```html_files``` folder and parsed using the ```bs4``` package. 
```

for one_file_name in glob.glob("html_files/*.html"):
	# one_file_name = "html_files/coinmarketcap20200929132624.html"
	print(one_file_name)
	scrape_time = os.path.basename(one_file_name).replace("coinmarketcap","").replace(".html","")
	f = open(one_file_name, "r")
	soup = BeautifulSoup(f.read(), "html.parser")
	f.close()
```
Then the program appends key inficators such as price, marketcap, time the data was scrapped, symbol, and the currency link. 
```
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
```
After appending the html files, the program creates a csv file containing a table of all the data collected over the time frame, which can be opened in excel or numbers. This will be used to determine the summary statistics.  

### Step 3:

After parsing the data recieved from the html files we, then can create summary statistics based off of the data we scrapped. 

In the program, I've provided the option to reorder the csv file to be better organized for the user:
```
df = pd.read_csv('coinmarketcap_dataset.csv')
df_reorder = df[['name', 'price', 'marketcap', 'symbol', 'link', 'time']] # rearrange 
df_reorder.to_csv('coinmarketcap_dataset_reorder.csv', index=False)
```
**NOTE ** This isn't required so the user can simply comment this out. Just make sure the program is reading the correct file. 

The program then creates a folder called ```sumstat_files```
```
if not os.path.exists("sumstat_files"):
	os.mkdir("sumstat_files")
```

After pandas reads the csv file, the program will calculate a plethora of summary statistics. 
```
mean1 = df['price'].mean()
mean2 = df['marketcap'].mean()
min1 = df['price'].min()
min2 = df['marketcap'].min()
max1 = df['price'].max()
max2 = df['marketcap'].max()
median1 = df['price'].median()
median2 = df['marketcap'].median()
var1 = df['price'].var()
var2 = df['marketcap'].var()
std1 = df['price'].std()
std2 = df['marketcap'].std()
```
This will calculate the mean, min, max, median, variance, and standard deviance of all of the coins collected price and marketcap over the time frame. 

The program will also compile the median and standard deviation based off of the coin name. 
```
groupby_median1 = df.groupby(['name']).median()
groupby_std1 = df.groupby(['name']).std()
```
Then the program will compile that summary statistics in the terminal, along with a csv that is placed in ```sumstat_files```. 
## Limitations and Issues
Whilst writing this program I ran into many issues that stemed from my inexperience of coding, but as I went about writing this program I started to understand it more. I feel confident enough that I would have been able to complete the midterm in it's entirety if I was able to spend more time on it. Along with this, I was not able to download any data from coingecko.com, due to the fact that I had gotten denied the ability to request html files from their website due to testing my request file without a long enough sleep time. This forced me to attempt to download the data through an API key on google sheets, which I then accidentally corrupted the data by mistake. This caused my data to correlate to a different time frame then originally collected (Both CoinMarketCap data and original CoinGecko data were collected at the same time, I went back in at a later date to continue the project and my data was accidentally updated to that day's data). Despite not adequately finishing the midterm, it was still a learning experience and I still was able to take away some aspects of the skills that are being taught for the final.   
