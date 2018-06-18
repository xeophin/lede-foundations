
# coding: utf-8


import datetime

import requests
from apikeys import mailgun_api_key
from apikeys import darksky_api_key


location = '40.8009,-73.9600'
base_endpoint = 'https://api.darksky.net/forecast/' + darksky_api_key
additional_modifiers = '&'.join(['exclude=minutely,hourly,alerts,flags',
                                 'units=si'])
location_endpoint = base_endpoint + '/' + location + '?' + additional_modifiers
response = requests.get(location_endpoint)
forecast_data = response.json()

# TEMPERATURE is the current temperature
temperature = forecast_data['currently']['temperature']

# SUMMARY is what it currently looks like (partly cloudy, etc - it's "summary" in the dictionary). Lowercase, please.
summary = forecast_data['currently']['summary'].lower()

# HIGH_TEMP is the high temperature for the day.
high_temp = forecast_data['daily']['data'][0]['temperatureHigh']

# LOW_TEMP is the low temperature for the day.
low_temp = forecast_data['daily']['data'][0]['temperatureLow']

# TEMP_FEELING is whether it will be hot, warm, cold, or moderate. You will probably use HIGH_TEMP and your own thoughts and feelings to determine this.
# Actually, I'm going to use the dew point here, because I think this is 
# going to give a better overview of how terrible I'll find the weather
dew_point = forecast_data['daily']['data'][0]['dewPoint']
temp_feeling = 'crisp and dry'

if dew_point > 23:
  temp_feeling = 'sweltering and terrible'
elif dew_point > 18:
  temp_feeling = 'hot and humid'
elif dew_point > 16:
  temp_feeling = 'somewhat damp'


# RAIN_WARNING is something like "bring your umbrella!" if it is going to rain at some point during the day.
precip_intensity = forecast_data['daily']['data'][0]['precipIntensity']
rain_warning = 'no rain is expected'

if precip_intensity > 2:
  rain_warning = 'you will get wet without an umbrella'
elif precip_intensity > 0.2:
  rain_warning = 'you just might get away with no umbrella today'

# collect forecast
robo_forecast = """
Greetings, human!

It's a new day, and we have currently {:.0f}°C and it's {} outside.

Today's temperature will reach {:.0f}°C, it will feel {}, and {}.

Enjoy!
""".format(
  temperature,
  summary,
  high_temp,
  temp_feeling,
  rain_warning
)

# Mailgun stuff
now = datetime.datetime.now()
subject = '[Weather Bulletin] {:%A morning, %x}'.format(now)

# pewpewpew
requests.post(
  "https://api.mailgun.net/v3/sandbox89536ea6abb24b7495d37dbb678fdac4.mailgun.org/messages",
  auth=("api", mailgun_api_key),
  data={
    "from": "Mailgun Sandbox <postmaster@sandbox89536ea6abb24b7495d37dbb678fdac4.mailgun.org>",
    "to": "Kaspar <xeophin@gmail.com>",
    "subject": subject,
    "text": robo_forecast
  })

