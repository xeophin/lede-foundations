# Kaspar Manz
# 2018-05-23
# Homework 2, Part 2

# PART TWO: Lists
# 
# 1) Make a list called "countries" - it should contain seven different countries and NOT be in alphabetical order

countries = ['Sweden', 'Japan', 'Norway', 'Island', 'France', 'Puerto Rico',
             'Finnland']

# 2) Using a for loop, print each element of the list

for country in countries:
  print(country)

# 3) Sort the list permanently.

countries.sort()

# 4) Display the first element of the list.
print(countries[0])
# 5) Display the second-to-last element of the list.
print(countries[-2])
# 6) Delete one of the countries from the list using its name.
countries.remove('Japan')
# 7) Using a for loop, print each country's name in all caps.
for country in countries:
  print(str.upper(country))
# PART TWO: Dictionaries
# 
# These will require LATITUDE and LONGITUDE. You can ask Google for latitude and longitude by typing in *coordinates of CITYNAME*. You can also use http://itouchmap.com/latlong.html. Store the latitude and longitude without the N/S/E/W - if the latitude is S, make it negative. If the longitude is W, make it negative. See here for explanation: https://answers.yahoo.com/question/index?qid=20080211182008AAMdUe8
# 
# 1) Make a dictionary called 'tree' that responds to 'name', 'species', 'age', 'location_name', 'latitude' and 'longitude'. Pick a tree from: https://en.wikipedia.org/wiki/List_of_trees

tree = {
  'name': 'King\'s Pine',
  'species': 'Scots Pine',
  'age': 380,
  'location_name': 'Järvselja',
  'latitude': 58.266667,
  'longitude': 27.316667
}

# 2) Print the sentence "{name} is a {years} year old tree that is in {location_name}"

print("{name} is a {years} year old tree that is in {location_name}".format(
  name=tree['name'], years=tree['age'], location_name=tree['location_name']))

# 3) The coordinates of New York City are 40.7128° N, 74.0059° W. Check to see if the tree is south of NYC, and print "The tree {name} in {location} is south of NYC" if it is. If it isn't, print "The tree {name} in {location} is north of NYC"

location_compared_to_nyc = 'south'
if tree['latitude'] > 40.7128:
  location_compared_to_nyc = 'north'
  
print("The tree {name} in {location} is {northness} of NYC".format(name=tree[
  'name'], location=tree['location_name'], northness=location_compared_to_nyc))


# 4) Ask the user how old they are. If they are older than the tree, display "you are {XXX} years older than {name}." If they are younger than the tree, display "{name} was {XXX} years old when you were born."

age = int(input('How old are you again?'))

if age > tree['age']:
  print('You are', age - tree['age'], 'older than', tree['name'])
else:
  print(tree['name'], 'was', tree['age'] - age, 'years old when you were born.')

# 
# PART TWO: Lists of dictionaries
# 
# 1) Make a list of dictionaries of five places across the world - (1) Moscow, (2) Tehran, (3) Falkland Islands, (4) Seoul, and (5) Santiago. Each dictionary should include each city's name and latitude/longitude (see note above).

places = [
  {'name': 'Moscow', 'latitude': 55.751244, 'longitude': 37.618423},
  {'name': 'Tehran', 'latitude': 35.715298, 'longitude': 51.404343},
  {'name': 'Falkland Islands', 'latitude': -51.563412, 'longitude': -59.820557},
  {'name': 'Seoul', 'latitude': 37.532600, 'longitude': 127.024612},
  {'name': 'Santiago', 'latitude': 16.714983, 'longitude': 121.553719}
]

# 2) Loop through the list, printing each city's name and whether it is above or below the equator (How do you know? Think hard about the latitude.). When you get to the Falkland Islands, also display the message "The Falkland Islands are a biogeographical part of the mild Antarctic zone," which is a sentence I stole from Wikipedia.

for city in places:
  position_relative_to_equator = 'above'
  if city['latitude'] < 0:
    position_relative_to_equator = 'below'
  
  print(city['name'], 'is', position_relative_to_equator, 'the equator.')  
    
  if city['name'] == 'Falkland Islands':
    print(
      "The Falkland Islands are a biogeographical part of the mild Antarctic "
      "zone.")
    

# 3) Loop through the list, printing whether each city is north of south of your tree from the previous section.
for city in places:
  position_relative_to_tree = 'north'
  
  if city['latitude'] < tree['latitude']:
    position_relative_to_tree = 'south'
    
  print(city['name'], 'is', position_relative_to_tree, 'of', tree['name'])