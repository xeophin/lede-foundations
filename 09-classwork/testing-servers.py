
# coding: utf-8

# In[8]:
import datetime

import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[9]:


response = requests.get('http://www.nytimes.com')
text = response.text

soup = BeautifulSoup(text, 'html.parser')


# In[10]:


stories = soup.select('.story')


# In[11]:


len(stories)


# - `.story-heading`
# - `.byline`

# In[12]:


list_of_stories = []

for story in stories:
  story_dict = {}
  headline = story.find(class_='story-heading')
  byline = story.find(class_='byline')
  if headline:
    story_dict['headline'] = headline.text.strip()
  if byline:
    story_dict['byline'] = byline.text.strip()
  list_of_stories.append(story_dict)

list_of_stories


# In[13]:


df = pd.DataFrame(list_of_stories)

right_now = datetime.datetime.now()

# actually, don't use isoformat, since it uses : and this seems to confuse 
# the wildcards?
df.to_csv('nyt-stories-{}.csv'.format(right_now.strftime("%Y%m%d%H%M")), 
          index=False)
