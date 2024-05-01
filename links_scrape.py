#  -----------------------------Libraries------------------------------

import pandas as pd   # reading csv files
import requests   # making HTTP requests to web servers and working with their responses
from time import sleep  # waiting time
from bs4 import BeautifulSoup # used for web scraping
from datetime import datetime # for date and time
import pytz  # for conversion in of time zone
from random import randint # for random values



urls_dataframe  = pd.read_csv("urls.csv")  # contains lnks of websites and sections


# Selecting set of urls form dataframe


df_news_18 = urls_dataframe["URL"][:6]
df_mint  = urls_dataframe["URL"][6:12]
df_indian_exp = urls_dataframe["URL"][12:16]
df_india_tv = urls_dataframe["URL"][16:22]
df_hindu = urls_dataframe["URL"][22:]



# 1. Scraping the data from mint

# Creating list for storing different types of news_title


world =  []
sports = []
technology = []
companies  = []

# store time of the news_title

world_time = []
sports_timr = []
technology_time = []
companies_time = []

for i in range(6,12):  # loop beteween range where links of url id present

    url = df_mint[i]
    response = requests.get(url)  # requesting the url
    sleep(randint(5,15))   # sleep for taking rest
    soup1 = BeautifulSoup(response.text , "lxml")
    box = soup1.find("section" , class_="mainSec")  # getting a pratular block in website
    title = box.find_all("h2" , class_ ="headline") # extratcing healines of news from HTML tags
    time = box.find_all("span" ,class_ = "fl date") # extracting time of news from HTML tags



    #  appending the text data of news title in list
    try:
        for tag in title:
            if "world" in url:
                world.append(tag.text.strip())
            elif "sports" in url:
                sports.append(tag.text.strip())
            elif "technology" in url:
                technology.append(tag.text.strip())
            elif "companies" in url:
                companies.append(tag.text.strip())
    except:
        print("tag not find ")




    # appending the text data of time , in a list
    try:
        for t in time:
            if "world" in url:
                world_time.append(t.text[10:].strip())
            elif "sports" in url:
                sports_timr.append(t.text[10:].strip())
            elif "technology" in url:
                technology_time.append(t.text[10:].strip())
            elif "companies" in url:
                companies_time.append(t.text[10:].strip())
    except:
        print("Exception Occured :- Tag Not Found")




# Handling the Nan values

if len(technology) > len(technology_time):
    technology_time.append(None)
if len(world) > len(world_time):
    world_time.append(None)
if len(companies) > len(companies_time):
    companies_time.append(None)


# creating final list that will have  each type of news title
data = []
news_type =  []
time = []


# appending every news_tile type in a single list

for i1 in world:
  data.append(i1)
  news_type.append("world")

for i1 in technology:
  data.append(i1)
  news_type.append("technology")

for i1 in companies:
  data.append(i1)
  news_type.append("companies")

# appending all the time data in single list called time

time = []

for i in world_time:
  time.append(i)

for i in technology_time:
  time.append(i)

for i in companies_time:
  time.append(i)

news_source = []

for i in data:
  news_source.append("mint")

import pandas as pd


#  Creating Final DataFrame

mint = pd.DataFrame({
    "news":data,
    "time":time,
    "news_type":news_type,
    "news_source":news_source

})


# 2. Scraping from india tv

world1 =  []
sports1 = []
technology1 = []
business1  = []


w_t1 = []
s_t1 = []
t_t1 = []
b_t1 = []

for i in range(16,22):

    url = df_india_tv[i]
    response = requests.get(url)
    sleep(randint(5,15))
    soup1 = BeautifulSoup(response.text , "lxml")
    box = soup1.find("div" , class_ = "lhs mb30")
    title = box.find_all("h3" , class_ ="title")
    time = box.find_all("span" ,class_="deskTime")

    try:
        for tag in title:
            if "world" in url:
                world1.append(tag.text.strip())
            elif "sports" in url:
                sports1.append(tag.text.strip())
            elif "technology" in url:
                technology1.append(tag.text.strip())
            elif "business" in url:
                business1.append(tag.text.strip())
    except:
        print("Exception Occured , Tag Not found")


    try:
        for t in time:
            if "world" in url:
                w_t1.append(t.text.strip())
            elif "sports" in url:
                s_t1.append(t.text.strip())
            elif "technology" in url:
                t_t1.append(t.text.strip())
            elif "business" in url:
                b_t1.append(t.text.strip())
    except:
        print("Tag Not found")



if len(sports1) > len(s_t1):
    s_t1.append(None)
if len(technology1) > len(t_t1):
    t_t1.append(None)
if len(world1) > len(w_t1):
    w_t1.append(None)
if len(business1) > len(b_t1):
    b_t1.append(None)

data1 = []
news_type1 =  []
for i in sports1:
  data1.append(i)
  news_type1.append("sports")
  time.append(s_t1)


for i1 in world1:
  data1.append(i1)
  news_type1.append("world")

for i1 in technology1:
  data1.append(i1)
  news_type1.append("technology")

for i1 in business1:
  data1.append(i1)
  news_type1.append("buisness")


time1 = []
for i in s_t1:
  time1.append(i)

for i in w_t1:
  time1.append(i)

for i in t_t1:
  time1.append(i)

for i in b_t1:
  time1.append(i)

news_source1 = []

for i in data1:
  news_source1.append("indiaTV")



indiaTV = pd.DataFrame({
    "news":data1,
    "time":time1,
    "news_type":news_type1,
    "news_source":news_source1

})


df_m_itv = pd.concat([mint, indiaTV], axis=0)

# Scraping from News 18

india = []
world = []
business = []
politics  = []

i_t = []
w_t = []
b_t = []
p_t = []



for i in range(0,6):

  url = df_news_18[i]
  response = requests.get(url)
  sleep(randint(1,2))
  soup2 = BeautifulSoup(response.text , "lxml")
  box2 = soup2.find("div" , class_ = "jsx-4088862090 blog_list")
  title2 = box2.find_all("h4" , class_ = "jsx-4088862090")
  time = box2.find_all("sub" , class_ = "jsx-4088862090 story_date")

  try:
      for tag in title2:
          if "india" in url:
              india.append(tag.text.strip())
          elif "business" in url:
              business.append(tag.text.strip())
          elif "politics" in url:
              politics.append(tag.text.strip())
          elif "world" in url:
              world.append(tag.text.strip())
  except:
      print("Excrption Ocuured")

  try:
      for t in time:
          if "india" in url:
              i_t.append(t.text.strip())
          elif "business" in url:
              b_t.append(t.text.strip())
          elif "politics" in url:
              p_t.append(t.text.strip())
          elif "world" in url:
              w_t.append(t.text.strip())
  except:
      print("Exception occured, Tag not Found")


if len(india) > len(i_t):
    i_t.append(None)
if len(business) > len(b_t):
    b_t.append(None)
if len(politics) > len(p_t):
    p_t.append(None)
if len(world) > len(w_t):
    w_t.append(None)


data = []
news_type =  []
for i in india:
  data.append(i)
  news_type.append("india")
  # time.append(i_t)


for i1 in business:
  data.append(i1)
  news_type.append("business")

for i1 in politics:
  data.append(i1)
  news_type.append("politics")

for i1 in world:
  data.append(i1)
  news_type.append("world")



time = []
for i in i_t:
  time.append(i)

for i in b_t:
  time.append(i)

for i in p_t:
  time.append(i)

for i in w_t:
  time.append(i)

news_source = []

for i in data:
  news_source.append("news18")



news18 = pd.DataFrame({
    "news":data,
    "time":time,
    "news_type":news_type,
    "news_source":news_source

})


df_m_itv_18 = pd.concat([df_m_itv, news18], axis=0)


# Scraping from Indian Express

india =  []
sports = []
politics = []
entertainment   = []


i_t = []
s_t = []
p_t = []
e_t = []

for i in range(12,16):

    url = df_indian_exp[i]
    response = requests.get(url)
    sleep(randint(5,15))
    soup1 = BeautifulSoup(response.text , "lxml")
    box = soup1.find("div",class_ = "nation")
    title = box.find_all("h2" , class_ ="title")
    time = box.find_all("div" ,class_ = "date")

    try:
        for tag in title:
            if "sports" in url:
                sports.append(tag.text.strip())
            elif "political" in url:
                politics.append(tag.text.strip())
    except:
        print("Exception Occured")



    try:
        for t in time:
            if "sports" in url:
                s_t.append(t.text[10:].strip())
            elif "political" in url:
                p_t.append(t.text[10:].strip())
    except:
        print("Exception Occured Tag Not Found")



if len(sports) > len(s_t):
    s_t.append(None)
if len(politics) > len(p_t):
    p_t.append(None)

data = []
news_type =  []
for i in sports:
  data.append(i)
  news_type.append("sports")
  time.append(s_t)



for i1 in politics:
  data.append(i1)
  news_type.append("politics")



time = []
for i in s_t:
  time.append(i)


for i in p_t:
  time.append(i)


news_source = []

for i in data:
  news_source.append("Indian Express")

import pandas as pd

indian_exp = pd.DataFrame({
    "news":data,
    "time":time,
    "news_type":news_type,
    "news_source":news_source

})

df_m_itv_18_ixp = pd.concat([df_m_itv_18, indian_exp], axis=0)





ist = pytz.timezone('Asia/Kolkata')
current_time = datetime.now(ist).strftime("%I:%M %p IST")


# Scraping from The Hindu

nation = []
world = []
sports = []
business = []
entertainment = []
tech = []



wt = []
nt = []
st = []
bt =[]



for i in range(22,28):
  url = df_hindu[i]
  response = requests.get(url)
  soup = BeautifulSoup(response.text , "lxml")
  box = soup.find("div" , class_ ="col-xl-6 col-lg-4 col-md-12 col-sm-12 col-12 result")
  title = box.find_all("h3" , class_ = "title big")

  try:
      for i in title:
          if "international" in url:
              world.append(i.text)
              wt.append(current_time)
          elif "national" in url:
              nation.append(i.text)
              nt.append(current_time)
          elif "football" in url:
              sports.append(i.text)
              st.append(current_time)
          elif "business" in url:
              business.append(i.text)
              bt.append(current_time)
          elif "technology" in url:
              tech.append(i.text)
  except:
      print("Exceotion Occured")



data = []
news_type = []

for i in world:
  data.append(i)
  news_type.append("world")

for i in nation:
  data.append(i)
  news_type.append("nation")

for i in sports:
  data.append(i)
  news_type.append("sports")

for i in business:
  data.append(i)
  news_type.append("business")

for i in tech:
  data.append(i)
  news_type.append("technology")


time = []
press = []

for i in data:
  time.append(current_time)
  press.append('The Hindu')



the_hindu = pd.DataFrame({
    "news":data,
    "time":time,
    "news_type":news_type,
    "news_source":press
})




df_m_itv_18_ixp_hindu= pd.concat([df_m_itv_18_ixp, the_hindu], axis=0)



df_m_itv_18_ixp_hindu.to_csv('sample.csv', mode='a', header= True, index= False, encoding = "utf-8")







