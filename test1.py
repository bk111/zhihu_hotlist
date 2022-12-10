import requests
import datetime

now_time = datetime.datetime.now()
year = now_time.year
month = now_time.month
day = now_time.day
hour = now_time.hour

url = 'https://www.artstation.com/a_shipwright'
strhtml = requests.get(url)
output = strhtml.text
print(output)

fp = open("./hotlist1/{}_{}_{}_{}.txt".format(year, month, day, hour), mode="w")
print(output, file=fp)
fp.close()
