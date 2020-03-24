#!/usr/bin/env python
# coding: utf-8

# ## Assignment:
# 
# For each of the following questions:
# 
# - formulate a null and alternative hypothesis (be as specific as you can be); 
# - then give an example of what a true positive; 
# - true negative;
# - type I; and
# - type II errors  
# 
# Note that some of the questions are intentionally phrased in a vague way. It is your job to reword these as more precise questions that could be tested.
# 

# ## Q1:
# Has the network latency gone up since we switched internet service providers?

# In[1]:


# define what is network latency

# Latency is a time delay.  Network latency is the time it takes for a command
# to go from the client to the server and back.  You want it to be as close to 0
# as possible


# In[2]:


# Now we take a look at the correlation between ISPs and network latency, and
# why switching ISPs would increase latency.

# new isp may not have hardware strong enough to quickly process packets
# isp servers may be out of date
# new isp may not have enough bandwidth


# In[3]:


# Null hypothesis:


# $H_0$ = There's been no change in the network latency since we switched ISPs.

# In[4]:


# Alternate hypothesis:


# $H_a$ = Out network latency has increased because our new ISP has outdated servers

# In[5]:


# True positive


# - Our new ISP's last server upgrade was in 2010

# In[6]:


# True negative


# - Our network latency has not changed at all; the new ISP is as
#   powerful and up-to-date as our last ISP's.

# In[7]:


# Type 1 error = False Positive


# - All the data we sampled for this came from our business segments, where our last
#   samplings were from individual users

# In[10]:


# Type 2 error = False Negative


# - We conducted our study on a Saturday, when less people were at work

# ## Q2:
# Is the website redesign any good?

# In[11]:


# First find out what makes a good website redesign
# Was it delivered on time and under budget?
# Are people talking about it on social media?
# What kind of feedback are visitors leaving us?
# How busy has our customer support sector been?

# Null Hypothesis


# $H_0$ = The website redesign was just fine.  

# In[12]:


# Alternate Hypothesis


# $H_a$ = The website redesign has been a complete disaster.  Dogs and cats, living     together... MASS HYSTERIA!!

# In[13]:


# True Positive


# - We surveyed 1,000 visitors, and 950 of the surveys came back as satisfactory

# In[14]:


# True Negative


# - Our customer service has been inundated with emails and phone calls complaining about how everything on the new website is hard to find and the font is too small.

# In[15]:


# Type 1 error = False Positive


# - Our Head of Purchasing reviewed it, and they love it!

# In[ ]:


# Type 2 error = False Negative


# - We conducted the surveys after two weeks of Corona-19 lockdown, and everyone said they hated it.

# ## Q3:
# Is our television ad driving more sales?

# In[16]:


# First determine how a TV ad drives sales:

# Are people talking about it / has it gone viral?
# When you compare the sales since time the ad ran, have they gone up?
# Are salespeople giving you feedback about customers calling them all of the sudden?

# Null Hypothesis:


# - Since the TV spot ran, our sales have increased.

# In[17]:


# Alternative Hypothesis:


# - The sales have remained stagnant since the ad ran.

# In[18]:


# True Positive


# - We sent out sales surveys the day the ad ran.  Three months later, we sent surveys back to the same distributors to check sales, and they all came back as sales markedly increased.

# In[19]:


# True Negative


# - We discovered the ad had little to no effect on the sales of Product X because even after adjusting the numbers, all dealerships reported almost no growth between quarters.

# In[20]:


# Type 1 error = False Positive


# - We checked all the major social media outlets the day after the ad ran, and people were loving it!

# In[21]:


# Type 2 error = False Negative


#  - Despite the highly stylized ad, our Eskimo line of jackets has not sold any more jackets in August than it had in May.

# In[ ]:




