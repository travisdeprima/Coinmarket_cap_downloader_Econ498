import urllib.request
import os
import datetime
import time
#for time stamp


if not os.path.exists("html_files"):
    os.mkdir("html_files")


for i in range(8):
    current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
    print(current_time_stamp)
    f = open("html_files/coinmarketcap" + current_time_stamp + ".html", "wb")
    response = urllib.request.urlopen("http://coinmarketcap.com/")
    html = response.read()
    #print(html)
    f.write(html)
    f.close()
    time.sleep(900)

""" for i in range(8):
     current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
     print(current_time_stamp)
     f = open("html_files/coinmarketcap" + current_time_stamp + ".html", "wb")
     response = urllib.request.urlopen("http://coinmarketcap.com/2/")
     html = response.read()
     #print(html)
     f.write(html)
     f.close()
     time.sleep(900)

for i in range(8):
     current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
     print(current_time_stamp)
     f = open("html_files/coinmarketcap" + current_time_stamp + ".html", "wb")
     response = urllib.request.urlopen("http://coinmarketcap.com/3/")
     html = response.read()
     #print(html)
     f.write(html)
     f.close()
     time.sleep(900)

for i in range(8):
     current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
     print(current_time_stamp)
     f = open("html_files/coinmarketcap" + current_time_stamp + ".html", "wb")
     response = urllib.request.urlopen("http://coinmarketcap.com/4/")
     html = response.read()
     #print(html)
     f.write(html)
     f.close()
     time.sleep(900)  """

"""for i in range(8): 
     current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
     print(current_time_stamp)
     f = open("html_files/coinmarketcap" + current_time_stamp + ".html", "wb")
     response = urllib.request.urlopen("http://coinmarketcap.com/5/")
     html = response.read()
     #print(html)
     f.write(html)
     f.close()
     time.sleep(900)""" 