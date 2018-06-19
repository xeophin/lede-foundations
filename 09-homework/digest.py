
# coding: utf-8

# In[55]:


# Using Scraping
# Scrape the front page of some always-updating website, such as
# 
# https://www.slickdeals.net/ (Links to an external site.)Links to an external site.
# https://www.reddit.com (Links to an external site.)Links to an external site./
# https://www.washingtonpost.com (Links to an external site.)Links to an external site./
# https://finance.yahoo.com/industries (Links to an external site.)Links to an external site.
# anything else, really
# Note that some of these won't work with BeautifulSoup!
# Send yourself an email with as much information as possible from the site, such as:
# 
# The title of the thing (the sale, the article, whatever)
# A URL for it
# Upvotes/thumbs ups/subreddits/prices/links to images/etc
# Save this as a CSV, and send it as an attachment to your email address every 6 hours. The email headline should say something like "Here is your 6PM briefing." The CSV file should be timestamped with the current date and time, e.g. briefing-2018-06-18-3PM.csv
# 
# BONUS: Have the content actually be the body of the email, not just an 
# attachment. I don't mean like a CSV or whatever, I mean it should actually 
# look like nice lists and stuff, a real email.


# In[56]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
from apikeys import mailgun_api_key
import datetime


# In[57]:


comic_list = []


# In[58]:


# Get Sinfest Comic Strip


SINFEST_URL = 'http://www.sinfest.net/'

try:
  sinfest_doc = BeautifulSoup(requests.get(SINFEST_URL).text,
                              'html.parser')
  img_element = sinfest_doc.select_one('center > table tbody.style5 tr > td > '
                                       'img')
  img_src = SINFEST_URL + img_element['src']
  img_title = img_element['alt']

  sinfest = {
    'comic': 'Sinfest',
    'src': img_src,
    'title': img_title,
    'url': SINFEST_URL + 'view.php?date={:%Y-%m-%d}'.format(
      datetime.datetime.now())
  }

  comic_list.append(sinfest)
except Exception as e:
  print('[Sinfest]: Scraping failed, due to', e)


# In[59]:


comic_list


# In[60]:


# Get newest Scandinavia and the World comic strip

SATW_URL = 'https://satwcomic.com/'
INDEX_PAGE = 'the-world'

try:
  satw_doc = BeautifulSoup(requests.get(SATW_URL + INDEX_PAGE).text, 
                           'html.parser')
  last_comic_url = satw_doc.select_one('.card a')['href']
  
  satw_comic_doc = BeautifulSoup(requests.get(last_comic_url).text, 'html.parser')
  
  img_element = satw_comic_doc.select_one('.btn-group-justified + center img')
  img_src = img_element['src']
  img_title = img_element['title']
  
  satw = {
    'comic': 'Scandinavia and the World',
    'src': img_src,
    'title': img_title,
    'url': last_comic_url
  }
  
  comic_list.append(satw)
except Exception as e:
  print('[Scandinavia and the world]: Scraping failed, due to', e)
  


# In[61]:


# Okay, so we push that into a data frame purely so we can take advantage of 
# the CSV export
comic_df = pd.DataFrame(comic_list)
comic_df


# In[62]:


now = datetime.datetime.now()
comic_df.to_csv(
  'comics-{:%Y%m%d%H%M}.csv'.format(now),
  index=False
)


# In[63]:


# Okay, now for the sake of the exercise, go and scrape metafilter as will 
# and pull the first few popular headlines. Of course, there would be an RSS 
# feed already, but since it's an exercise ...
import re

MF_BASE = 'https://www.metafilter.com'
MF_POPULAR = MF_BASE + '/home/popularfavorites'
try: 
  mf_doc = BeautifulSoup(requests.get(
    'https://www.metafilter.com/home/popularfavorites').text, 'html5lib')
  
  post_titles = mf_doc.select('#posts .posttitle')
  
  metaposts_list = []
  
  for title in post_titles:
    post = {}
    post['title'] = title.text
    post['url'] = MF_BASE + title.select_one('a')['href']
    summary_raw = list(title.select_one('+ .copy.post').stripped_strings)
    post['favourites'] = summary_raw[-2]
    post['summary'] = ' '.join(summary_raw[0:-10])
    
    metaposts_list.append(post)
except Exception as e:
  print('[Metafilter] Scraping failed due to', e)
  


# In[64]:


df_mf = pd.DataFrame(metaposts_list)
df_mf.to_csv('metafilter-{:%Y%m%d%H%M}.csv'.format(now), index=False)


# In[65]:


# Let's set up the mail

def get_comic_html(comic):
  return '''
  <div style="max-width: 600px; margin: 1em auto 2em; border-radius: 1em; 
  box-shadow: 0 0 1em rgba(0,0,0,0.3); overflow: hidden;">
    <img style="display: block; max-width: 100%;" src="{src}" />
    <div style="padding: 1em">
      <p style="margin-bottom: 0;">
        <strong style="color: rgba(0,0,0,0.45);">{comic}</strong>
      </p>
      <h2 style="margin-top: 0;"><a href="{url}">{title}</a></h2>
    </div>
  </div>
  '''.format(**comic)

def get_metafilter_html(mf_post):
  return '''
  <div style="max-width: 600px; margin: 1em auto 2em; border-radius: 1em; 
  box-shadow: 0 0 1em rgba(0,0,0,0.3); overflow: hidden; padding: 1em;">
    <h2><a href="{url}">{title}</a></h2>
    <div>{summary}</div>
    <div style="margin: 1em -1em -1em -1em; padding: 1em; 
    background-color: rgba(0,0,0,0.2); color: rgba(0,0,0,0.33)">
      <small>{favourites}</small>
    </div>
  </div>
  '''.format(**mf_post)


complete_html = '''
<html style="font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", 
Roboto, Helvetica, Arial, sans-serif, \"Apple Color Emoji\", \"Segoe UI 
Emoji\", \"Segoe UI Symbol\";">
<h1>Your Daily Comics</h1>
{comics}

<h1>Popular MetaFilter Discussions</h1>
{metafilter}
</html>
'''.format(
  comics=''.join(map(get_comic_html, comic_list)),
  metafilter=''.join(map(get_metafilter_html, metaposts_list))
)


# In[66]:


subject = '[Daily Briefing] {:%A, %x, %X}'.format(now)

requests.post(
  "https://api.mailgun.net/v3/sandbox89536ea6abb24b7495d37dbb678fdac4.mailgun.org/messages",
  auth=("api", mailgun_api_key),
  data={
    "from": "Mailgun Sandbox <postmaster@sandbox89536ea6abb24b7495d37dbb678fdac4.mailgun.org>",
    "to": "Kaspar <xeophin@gmail.com>",
    "subject": subject,
    "html": complete_html
  })

