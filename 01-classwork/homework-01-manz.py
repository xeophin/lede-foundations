# Kaspar Manz
# 2018-05-21
# Homework 1

# When run from the command line, this file should
# 1. Prompt the user for their year of birth, and tell them (approximately):
def ask_for_year_of_birth():
  yearOfBirth = input('What is your year of birth? ')
  yearOfBirth = int(yearOfBirth)
  
  if yearOfBirth > 2018:
    return False
  else:
    return yearOfBirth

def calculate_yearly_heartbeats(heartrate: int, years: int) -> int:
  return heartrate * 60 * 24 * 365 * years

year_of_birth = ask_for_year_of_birth()

while not year_of_birth:
  print('That sounds implausible.')
  year_of_birth = ask_for_year_of_birth()

# 2. How old the user is
how_old = 2018 - year_of_birth
print('You are approximately', how_old, 'years old.')

# 3. How many times the user's heart has beaten
normal_human_heartrate = 60
print('Your heart has beaten so far', calculate_yearly_heartbeats(
  normal_human_heartrate, how_old), 'times.')

# 4. How many times a blue whale's heart has beaten
whale_heartrate = 9
print('In the same time, a blue whale\'s heart has beaten', 
      calculate_yearly_heartbeats(whale_heartrate, how_old), 'times.')

# 5. How many times a rabbit's heart has beaten
rabbit_heartrate = 135
rabbit_heartbeats = calculate_yearly_heartbeats(rabbit_heartrate, how_old)
print('While a rabbit\'s has beaten', rabbit_heartbeats, 'times.')

# 6. If the answer to (5) is more than a million, say "XXX million" instead of the very long raw number
if rabbit_heartbeats >= 1000000:
  print('That\'s', rabbit_heartbeats / 1000000, 'million times.')

# 7. How old they are in Venus years
venus_factor = 356 / 224.7
print('In Venus years, you would already be', venus_factor * how_old, 'years '
                                                                    'old.')

# 8. How old they are in Neptune years
neptune_factor = 1 / 164.8
print('In Neptune years, though, it would just be', neptune_factor * how_old, 
      'years.')

# 9. Whether they are the same age as you, older or younger
# 10. If older or younger, how many years difference
MY_YEAR = 1982
if year_of_birth == MY_YEAR:
  print('Cool, you\'re the same age I am!')
elif year_of_birth > MY_YEAR:
  print('You are younger than I am, by', year_of_birth - MY_YEAR, 'years.')
else:
  print('You are older than I am, by', MY_YEAR - year_of_birth, 'years.')
  
# 11. If they were born in an even or odd year
print ('You were born in an', 'even' if year_of_birth % 2 == 0 else 'odd', 
         'year.')

# 12. Which US President was in office when they were born (1935 onward)-
president = '– what\'s his name again? I don\'t remember, I\'m afraid'

if year_of_birth > 2016:
  president = 'Trump'
elif year_of_birth > 2008:
  president = 'Obama'
elif year_of_birth > 2000:
  president = 'Bush (the second one)'
elif year_of_birth > 1992:
  president = 'Clinton'
elif year_of_birth > 1988:
  president = 'Bush (the first one)'
elif year_of_birth > 1980:
  president = 'Reagan'
elif year_of_birth > 1976:
  president = 'Carter'
elif year_of_birth > 1973:
  president = 'Ford'
elif year_of_birth > 1968:
  president = 'Nixon'
elif year_of_birth > 1962:
  president = 'Johnson'
elif year_of_birth > 1960:
  president = 'Kennedy'
elif year_of_birth > 1952:
  president = 'Eisenhower'
elif year_of_birth > 1944:
  president = 'Truman'
elif year_of_birth > 1932:
  president = 'Roosevelt'
  
print('You have been born during the reign of President', president, '.' )