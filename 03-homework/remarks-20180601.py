# Kaspar Manz
# 2018-06-01
# Homework

# Create a new list of URLs using list comprehensions
cantons = ["ZH", "BE", "LU", "UR", "SZ", "OW", "NW", "GL", "ZG", "FR", "SO",
           "BS", "BL", "AR", "AI", "SG", "GR", "AG", "TG", "TI", "VD", "VS",
           "NE", "GE", "JU"]

base_url = 'http://important-swiss-things.ch/docs/download/'

new_urls = [base_url + canton for canton in cantons]

###############################################################################

keys = ['qq7lthm',
        'jemsqhg',
        'O6itcke',
        'cp4Iua0',
        'bkijcmo',
        'ctoyjrm',
        'z8wc6xy',
        'zk4Bmm0', ]

base = 'www.top-secret-pdfs.com/content/secrets/'

for key in keys:
  for page in range(1, 13):
    print('{}{}/page/{:03}.pdf'.format(base, key.upper(), page))

###############################################################################
# Reading in CSVs

import csv

csvfile = open('countries.csv', 'r')
reader = csv.DictReader(csvfile)
countries = list(reader)
csvfile.close()
print("The data looks like", countries)

# Getting the keys
print(countries[0].keys())

# get the population of the world
all_the_population = [int(country['Population'], 10) for country in countries]
print('All the population is', sum(all_the_population))

# calculate the 75th percentile of gdp
# Apparently numpy is cool
import numpy

gdp = [int(country['GDP_per_capita']) for country in countries]
print(numpy.percentile(gdp, 75, interpolation='midpoint'))
# cool cool cool

