# There is nothing in this file.
import statistics

ages = [1, 3, 5, 12, 4]
print(statistics.stdev(ages))

# Dictionaries
smush:dict = {'name': 'Smush', 'age': 8}

abby = {
  'name': 'Boy Abby',
  'age': 14
}

print('The cat\'s name is', abby['name'], 'and he is', abby['age'], 'years old')

populations = {
  'Brooklyn': 3
}

print(populations['Brooklyn'])

cityname = input('city?')

if cityname in populations.keys():
  print('Population:', populations[cityname])