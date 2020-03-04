#!/usr/bin/env python
# coding: utf-8

# In[1]:


# RUN THIS CODE ONCE AND UPLOAD THE RESULTING CSV TO GITHUB FOR FUTURE REUSE


# In[2]:


import pandas as pd
from langdetect import detect


# In[3]:


# path to your file
df = pd.read_csv('../data/london/london_reviews.csv')


# In[4]:


df2 = df[df.comments.str[:34] != "The host canceled this reservation"]
df2 = df2.copy()


# In[5]:


df3 = df2['comments']


# In[ ]:





# In[ ]:


langs = []
for i in df3:
    try:
        langs.append(detect(i))
    except:
        langs.append('Nan')
        continue


# In[ ]:


# In[ ]:


# change the name of the resulting file
df_en.to_csv(r'../data/en_reviews/london_en.csv', index = False)


# In[ ]:
