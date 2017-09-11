#!/usr/bin/env python
import logging.handlers
import os
import json

API_KEY = ''
LONG_LAT =  '26.2172,50.1971'
PATH = "temp.log"
handler = logging.handlers.WatchedFileHandler(
    os.environ.get("LOGFILE", PATH))
formatter = logging.Formatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)
root = logging.getLogger()
root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
root.addHandler(handler)

logging.info('<<<START>>>')

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
	

def F2C(f):
	c =  (f - 32) * 5.0/9.0
	return c
	
def getTTSNumber(num):
	if len(num) >= 2:
		num = num[0] +'0'+ ' '+num[1]
	elif len(num) == 1:
		num = num[0] + '0'	
	return num

url = 'https://api.darksky.net/forecast/' + API_KEY + '/' + LONG_LAT

logging.info('Opening url : [{0}]...'.format(url))

response = urlopen(url)

logging.info('Url opened')
logging.info('Parsing data...')

data = response.read().decode('utf-8')
json = json.loads(data)
current = json['currently']

logging.debug('Data => {0}'.format(current))

hum =  str(int(float(current['humidity']) * 100))
temp = round(F2C(current['temperature']))
temp = str(int(temp))

logging.info('Temperature = {0}, Humidity = {1}'.format(temp,hum))

print("Temp: "+temp +", Humidity: "+hum)

#temp = getTTSNumber(temp)
#hum = getTTSNumber(hum)
	
#print('TTS Temp: ' +temp+", Humidity: "+hum)

print('Calling Festival tts...')

logging.info('Calling festival tts...')

try:
	os.system('echo "Temperature is: ' + temp + ' Degree. Humidity is: ' + hum + ' ." | festival --tts')
	logging.info('TTS called.')
except Exception as e:
	logging.error('Failed to call festival tts',exc_info=True)

logging.info('<<<END>>>')
print('Have a nice day :)')
