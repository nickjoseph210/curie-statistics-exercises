#!/usr/bin/env python
# coding: utf-8

# In[34]:


import numpy as np
import pandas as pd


# In[3]:


#1 = How likely is it that you roll doubles when rolling two dice?

tosses = np.random.choice([1, 2, 3, 4, 5, 6], size=(10_000, 2))
tosses


# In[4]:


deuces = tosses.sum(axis=1)
deuces


# In[5]:


p_deuces = (deuces == 2).mean()
p_deuces


# In[6]:


#2 = If you flip 8 coins, what is the probability of getting exactly 3 heads? 
# What is the probability of getting more than 3 heads?

flips = np.random.choice([0, 1], size=(10_000, 8))
flips


# In[7]:


flip_results = flips.sum(axis=1)
flip_results


# In[20]:


# The probability of getting exactly 3 heads is...

(flip_results == 3).mean()


# In[21]:


# Now to get the probability of getting more than 3 heads:

(flip_results >= 3). mean()


# In[8]:


#3 There are approximitely 3 web development cohorts for every 1 data 
# science cohort at Codeup. Assuming that Codeup randomly selects 
# an alumni to put on a billboard, what are the 
# odds that the two billboards I drive past 
# both have data science students on them?

faces = np.random.choice(['webdev1', 'webdev2', 'webdev3', 'datasci'], size=(100_000, 4))
faces


# In[9]:


# Try to get them into a 1-D array.  Can't b/c as such, will get an error.
# So, give them numbers:
# webdev1 = 1
# webdev2 = 2
# webdev3 = 3
# datasci = 4
# rewrite the above

faces = np.random.choice([1, 2, 3, 4], size=(100_000, 4))
faces


# In[7]:


# Now we can make all of this into a 1-D array
billboard_total = faces.sum(axis=1)
billboard_total


# In[10]:


# apply now the final aggregation to get probability
smug_mug = np.random.choice([1, 2, 3, 4], size=100_000, p=[1/4, 1/4, 1/4, 1/4])
smug_mug


# In[11]:


p_smug_mug = (smug_mug == 4).mean() * .5
p_smug_mug


# In[12]:


# Let me try that billboard one again:
faces = np.random.choice([1, 2, 3, 4], size=(100_000, 4))
faces


# In[13]:


# make it 1-D
faces_1D = faces.sum(axis=1)
faces_1D


# In[14]:


((faces == 4).sum(axis=1) >= 1).mean()*.25


# In[44]:


#4. Poptarts
n_trials = n_rows = 100_000
n_pops = ncols = 17

eatz = np.random.choice([1, 2, 3, 4, 5], n_trials * n_pops)
eatz


# In[77]:


happy_eatz = pd.DataFrame(np.random.uniform(low=0.0, high=17.0, size=(100_000, 5)))
happy_eatz


# In[78]:


total_eaten_by_friday = (happy_eatz.sum(axis=1))

happy_eatz["AnyLeft?"] = total_eaten_by_friday

happy_eatz


# In[ ]:





# In[ ]:




