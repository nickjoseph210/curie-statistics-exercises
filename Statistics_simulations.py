#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


#1 = How likely is it that you roll doubles when rolling two dice?

tosses = np.random.choice([1, 2, 3, 4, 5, 6], size=(10_000, 2))
tosses


# In[5]:


deuces = tosses.sum(axis=1)
deuces


# In[8]:


p_deuces = (deuces == 2).mean()
p_deuces


# In[18]:


#2 = If you flip 8 coins, what is the probability of getting exactly 3 heads? 
# What is the probability of getting more than 3 heads?

flips = np.random.choice([0, 1], size=(10_000, 8))
flips


# In[19]:


flip_results = flips.sum(axis=1)
flip_results


# In[20]:


# The probability of getting exactly 3 heads is...

(flip_results == 3).mean()


# In[21]:


# Now to get the probability of getting more than 3 heads:

(flip_results >= 3). mean()


# In[ ]:


#3 There are approximitely 3 web development cohorts for every 1 data 
# science cohort at Codeup. Assuming that Codeup randomly selects 
# an alumni to put on a billboard, what are the 
# odds that the two billboards I drive past 
# both have data science students on them?

np.random.choic(['webdev1', 'webdev2', 'webdev3', 'datasci'], size=)

