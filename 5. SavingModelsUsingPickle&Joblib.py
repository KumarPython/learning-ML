#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pickle


# In[22]:


with open ("TESTING",'wb')as f:
    pickle.dump(model,f)


# In[20]:


with open ("TESTING",'rb')as f:
    mod=pickle.load(f)


# In[24]:


from sklearn.externals import joblib
joblib.dump("TESTING_JOBLIB",model)


# In[ ]:


joblib.load('TESTING_JOBLIB')

