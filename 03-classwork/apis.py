# We're using APIs, oh yay!

# https://swapi.co/api/people/1/
import requests

# Get data from the API
response = requests.get('https://swapi.co/api/people/2')

# Do we have an answer? Yes
print(response.text)

# But it's a string
print(type(response.text))

# It's JSON, so use the proper method
data = response.json()

print(data['name'], 'has', data['hair_color'], 'hair.')

for film in data['films']:
  response = requests.get(film)
  film_data = response.json()
  print(film_data['title'])
  


# Let's get some weather
response = requests.get('https://api.darksky.net/forecast/db93a4074cf7c69448376c29a0b5008f/37.8267,-122.4233')
data = response.json()
print(data)