# Kaspar Manz
# 2018-05-23
# Homework 2, Part 1
import statistics

# Lists
# Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48
numbers = [22, 90, 0, -10, 3, 22, 48]
# Display the number of elements in the list.
print('Number of elements:', len(numbers))
# Display the 4th element of this list.
print('4th element:', numbers[3])
# Display the sum of the 2nd and 4th element of the list.
print('Sum of some elements', numbers[1] + numbers[3])
# Display the 2nd-largest value in the list.
sorted_numbers = sorted(numbers)
print('Second largest:', sorted_numbers[-2])
# Display the last element of the original unsorted list
print('Last element:', numbers[-1])
# Display the sum of all of the numbers divided by two.
print('Sum:', sum(numbers) / 2)
# Print whether the median or the mean of the numbers is higher
mean = sum(numbers) / len(numbers)
median = statistics.median(numbers)
print('mean' if mean > median else 'median', 'is the higher value')


# PART ONE: Dictionaries
# 
# 1) Sometimes dictionaries are used to describe multiple aspects of a single object. Like, say, a movie. Define a dictionary called movie that works with the following code.
# 
# print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])

movie = {
  'title': 'Avalon',
  'year': 2001,
  'director': 'Mamoru Oshii',
  'budget': 8000000,
  'revenue': 8826094
}

# 
# 2) On the lines after that, add keys to the movie dictionary for budget and revenue (you'll use code like movie['budget'] = 1000), and print out the difference between the two.

print('Budget:', movie['budget'], 'Revenue:', movie['revenue'])

# 
# 3) If the movie cost more to make than it made in theaters, print "That was a bad investment". If the film's revenue was more than five times the amount it cost to make, print "That was a great investment." Otherwise print "That was an okay investment."

rating = 'okay'
if movie['budget'] > movie['revenue']:
  rating = 'bad'
elif movie['revenue'] >= movie['budget'] * 4:
  rating = 'great'
  
print('That was a', rating, 'investment.')

# 
# 4) Sometimes dictionaries are used to describe the same aspects of many different objects. Make ONE dictionary that describes the population of the boroughs of NYC. Manhattan has 1.6 million residents, Brooklyn has 2.6m, Bronx has 1.4m, Queens has 2.3m and Staten Island has 470,000. (Tip: keeping it all in either millions or thousands is a good idea)
# 

boroughs = {
  'Manhattan': 1600,
  'Brooklyn': 2600,
  'Bronx': 1400,
  'Queens': 2300,
  'Staten Island': 470
}

# 5) Display the population of Brooklyn.

print('Population of Brooklyn in thousands:', boroughs['Brooklyn'])

# 
# 6) Display the combined population of all five boroughs.

print('Overall population in thousands is:', sum(boroughs.values()))

# 7) Display what percent of NYC's population lives in Manhattan.
print('{:.2%} live in Manhattan'.format(boroughs['Manhattan'] / sum(
  boroughs.values())))