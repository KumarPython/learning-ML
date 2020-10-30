#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn import linear_model
df=pd.read_csv('canada_per_capita_income.csv')
df


# In[11]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.pyplot.xlabel("Year")
plt.pyplot.ylabel("Per Capita Income")
plt.pyplot.scatter(df.year,df.percapitaincome,color='red',marker='+'


# In[17]:


reg=linear_model.LinearRegression()
reg.fit(df[['year']],df[['percapitaincome']])

reg.predict(2020)
# In[19]:


reg.coef_


# In[20]:


reg.intercept_


# In[23]:


reg.predict([2020])


# In[26]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.pyplot.xlabel("Year")
plt.pyplot.ylabel("Per Capita Income")
plt.pyplot.scatter(df.year,df.percapitaincome,color='red',marker='+')
plt.pyplot.plot(df.year,reg.predict(df[['year']]),color='blue')


# In[ ]:




