#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


# In[7]:


driver = webdriver.Firefox()
url = driver.get("https://www.indiavotes.com/pc/party_list/0/17")


# In[8]:


page_source = driver.page_source


# In[9]:


soup = BeautifulSoup(page_source, 'html.parser')


# In[10]:


main = soup.find('div', class_='bodyBg').find('div', class_ = 'main').find('div', class_ = 'mianContent').find('div', class_ = 'mapTabData').find('div', class_='dataTables_wrapper')


# In[11]:


t1 = main.find_all('th')


# In[12]:


header = [title.text.strip() for title in t1]


# In[13]:


header = header[13:]


# In[14]:


print(header)


# In[15]:


df = pd.DataFrame(columns = header)
df.insert(0, 'Sr. No.', '')
df


# In[16]:


t2 = main.find_all('tr', class_ = {'odd', 'even'})


# In[17]:


for row in t2:
    r = row.find_all('td')
    ind_row = [data.text.strip() for data in r]
    #print(ind_row)
    length = len(df)
    df.loc[length] = ind_row
    


# In[19]:


df.to_csv('Election_2019_Partywise.csv', index=False)


# In[ ]:




