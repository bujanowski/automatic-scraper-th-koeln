#!/usr/bin/env python
# coding: utf-8

# Building an automated scraper https://columbia.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=3752384e-1b59-4429-b30d-ad6301262733

# Scraping BBC website https://columbia.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=aeff3d16-0b3c-4ab7-a84c-ad5d0133d80b

# Soma's github - https://github.com/jsoma/autoscraper-changes

# Soma, scraping review - https://columbia.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=aeff3d16-0b3c-4ab7-a84c-ad5d0133d80b

# In[146]:


import requests


# In[147]:


from bs4 import BeautifulSoup


# In[148]:


import pandas as pd


# In[149]:


response = requests.get('https://www.th-koeln.de/en/academics/web-science-masters-program--for-students_7219.php') 
doc = BeautifulSoup(response.text, 'html.parser')


# In[150]:


doc.select('.jsCheck4Intern')


# In[151]:


schedule = doc.select('.jsCheck4Intern')


# In[152]:


rows = []


# In[153]:


for new in schedule:
    print('----------')
    row = {}
    print (new.text.strip())
    row['link'] = new.text.strip()
    rows.append(row)


# In[155]:


print(rows)


# In[161]:


df = pd.DataFrame(rows)


# In[164]:


df


# In[166]:


df.to_csv("th-koeln_update.csv", index=False)


# In[ ]:





# In[ ]:





# In[ ]:




