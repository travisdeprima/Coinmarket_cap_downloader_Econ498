import urllib.request
import json
#import sys
#import os
#import time

#api_key = sys.argv[1]

#if not os.path.exists('json_files'):
#	os.mkdir('json_files')

# print(api_key)

response = urllib.request.urlopen('https://api.coingecko.com/api/v3/ping' + api_key)
json_response = json.load(response)

#coin_count = int(json_response['id'])
#print(coin_count)

#movie_start = movie_count-5 
# movie_start = 1