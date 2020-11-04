#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd
import numpy as np
from sklearn import linear_model
from word2number import w2n

# Importing data on to Pandas Dataframes
df=pd.read_csv('hiring.csv')
df


# In[29]:

# Filling all empty cells in a column of the dataframe
df.experience=df.experience.fillna("zero")
df


# In[32]:

# Convert all Textual Numbers into numerics
df.experience=df.experience.apply(w2n.word_to_num)
df


# In[34]:


import math
median_test_score = math.floor(df['test_score(out of 10)'].mean())
median_test_score


# In[35]:


df['test_score(out of 10)'] = df['test_score(out of 10)'].fillna(median_test_score)
df


# In[39]:


reg = linear_model.LinearRegression()
reg.fit(df[['experience','test_score(out of 10)','interview_score(out of 10)']],df['salary($)'])


# In[38]:


reg.predict([[2,9,6]])


# In[40]:


reg.predict([[12,10,10]])


# In[ ]:




