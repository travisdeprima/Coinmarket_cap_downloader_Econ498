import urllib.request
import os
import datetime
import time

if not os.path.exists("html_files"):
	os.mkdir("html_files")

for i in range(1):
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print(current_time_stamp)
	f = open("html_files/coingecko" + current_time_stamp + ".html", "wb")
	response = urllib.request.urlopen("https://www.coingecko.com/en/")
	html = response.read()
	# print(html)
	f.write(html)
	f.close()
	time.sleep(20)