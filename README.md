# weather2tts-raspi
Play current weather and humidity on raspberry pi by tts
This module depends on festival tts package.
to install write 

`sudo apt-get install festival`

# First
login to https://api.darksky.net and get an API key to get the current weather.

# Second
replace the long & lat on the url to your city's

# Third 
run
- python temp.py
or
- sh temp.sh
---
you can put the `sh temp.sh` on crontab to make it as schedule 

`crontab -e`

`*/30 * * * * sh /home/pi/temp.sh`
