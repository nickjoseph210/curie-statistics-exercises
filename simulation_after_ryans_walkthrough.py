#!/usr/bin/env python
# coding: utf-8

# ## Notes for Q1:
# 
#  - In math, certainty = 1, impossibility = 0
#  - probability is all the numbers that are between certainty and possibility
#  - TRIAL = the action of doing the experiment
#  - EVENTS = the outcomes of doing the experiment
#  
#  - use random seed 42 to match Ryan's results
#  - p(e) = the pROBABILITY OF AN eVent
#  - in our case, the event is rolling doubles on 2 dice:
#      p(rolling doubles on two dice)
#  - Recall: an array is a collection of variables of the same type
#  - Recall: a one-dimensional array is linear
#  - Recall: np.random.choice() = selects random options from a list 
#  

# In[60]:


import numpy as np
import pandas as pd


# In[61]:


np.random.seed(42)


# ## #1.
# How likely is it that you roll doubles when rolling two dice?

# In[5]:


rolls = np.random.choice([1, 2, 3, 4, 5, 6], size=(2, 100_000))
rolls


# In[6]:


rolls[0].size # lets us know that there's a 100,000 rolls for each die


# In[9]:


# Here, the array of values at each index is the trial, the event of rolling
# two dice
die1 = rolls[0]
die2 = rolls[1]

print(die1[1]) # the second roll of the first die, check against Out[5]
print(die2[1]) # the second roll of the second die, check against Out[5]


# In[10]:


# Thanks to numpy's vectorization capabilities, we don't have to worry
# about the indexes like we do in regular Python:

(die1 == die2).mean() # sum of all the doubles we roll divided by 100,000 rolls
# a double means die1 = die2, so this is literally "give me the mean of all the 
# numbers where the number on die1 is the same as the number on die2"


# In[14]:


# check the above:
# >>>(die1 == die2).sum()
# 16591
# >>>16591 / 100000
# 0.16591


# In[21]:


# using pandas for this same problem:
rolls = rolls.T # 'T' means transpose; we write rows as columns and columns as rows
df = pd.DataFrame(rolls)
df.head(5)


# In[22]:


# create a third column called 'doubles' that returns bool of whether or not
# you rolled a double, where the row in col1 and col2 have the same number

df["doubles"] = df[0] == df[1]
df


# In[23]:


df.doubles.mean() # total all the numbers where doubles = 'True' and divide by 100,000


# ## Q2. 
# If you flip 8 coins, what is the probability of getting exactly 3 heads? What is the probability of getting more than 3 heads?

# In[37]:


# The TRIAL is actually flipping 8 coins.  You have to flip all 8 coins to make
# one single TRIAL
# So, flip 8 coins:

n_coins = 8

# 1 simulation means you've flipped 8 coins.
# set the simulation to 100,000 - that's flipping 8 coins 100,000 times

n_simulations = 100_000

# "Heads" is set to 1, "Tails" to 0.  I could make this any number I want, but 1 
# and 0 are easy

flips = np.random.choice([0,1], size=(100_000, 8))


# In[38]:


flips # shows me the results of 8 coins that were flipped 100,000 times
    # each row is a set of 8 flips


# In[39]:


# Take a look at the first row of results:
flips[0]


# In[33]:


# I got ([heads, heads, tails, tails, tails, tails, tails, heads])


# In[40]:


#.sum(axis=1) sums up each row.  .sum(axis=0) would sum up each column

results = flips.sum(axis=1)
results


# In[ ]:


# now we have the sum of each row in a single row.  
# at each index is the sum of the entire row at that index in the original array


# In[41]:


# What is the probability of getting exactly 3 heads?

(results == 3) # says, 'Go get me all the indexes that equal three (b/c 1 = 'heads')''


# In[42]:


(results == 3).mean() # sum up all the 3's you find, and divide by 100,000


# In[43]:


# What's the probability of getting all 'heads'?
(results == 8).mean()


# In[44]:


# What's the probability of getting more than three heads?
(results > 3).mean()


# ## Q3:
# There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup. Assuming that Codeup randomly selects an alumni to put on a billboard, what are the odds that the two billboards I drive past both have data science students on them?

# In[46]:


# Like coin flipping, there are only 2 outcomes: 'Web_Dev' or 'Data_Science'

outcomes = np.random.choice(["Web_Dev", "Data_Science"], size=(100_000, 2), p=[.75, .25])

# above line says 2 outcomes, 100,000 trials of looking at 2 billboards
# 'p' = 'probability', must have the same # of arguments as there are outcomes
# AND p must = 1.

outcomes


# In[49]:


df = pd.DataFrame(outcomes)
df.columns = ["First_Billboard", "Second_Billboard"] # assigns the df's column headings


# In[50]:


# now create a column where we get a bool for when the first and second billboards
# are the same:
df["Both"] = (df.First_Billboard == "Data_Science") & (df.Second_Billboard == "Data_Science")


# In[51]:


df.head(5) # show me the first five rows


# In[54]:


both = df.Both.mean() # True = 1, False = 0; add up all the Trues and divide by 100,000
print(f"The probability of both billboards being Data Science is {both}.")


# In[57]:


# probabilities of Falses and Trues
# in other words, it is WAY more likely they are NOT both Data_Science billboards

df.Both.value_counts(normalize=True) 


# ## Q4:
# Codeup students buy, on average, 3 poptart packages (+- 1.5) a day from the snack vending machine. If on monday the machine is restocked with 17 poptart packages, how likely is it that I will be able to buy some poptarts on Friday afternoon?

# In[58]:


# 1st, you have to round the poptart values b/c you can't buy fractions or decimal 
# values of poptarts.  Not in a sane society, anyway.

# Note: now we use random.normal(), not random.choice().  
# format for random.normal():
# np.random.normal(mean (or, center of distribution), scale, size)

poptarts = np.round(np.random.normal(3, 1.5, size=(100_000, 5)))

# so that's mean of 3, the scale of 1.5, and the size of 100,000 samples for 5 days.


# In[62]:


print(f"Standard deviation is {poptarts.std()}.")
print(f"Mean is {poptarts.mean()}.")


# In[63]:


poptarts.min() # give me the lowest number on the scale


# In[64]:


poptarts.max() # give me the highest number on the scale


# In[65]:


# So the least amount of poptarts bought was -4.0, and the most was 10.  
# That means our scale ranges from -4 to 10.


# In[66]:


# Now for the eating up of the poptarts:

# Each row simulates one week of observing students eating poptarts,
# where each column is a day of that week.
# The values in the columns are the number of poptarts that were eaten that day

poptarts[0] # show me the first week of poptart consumption


# In[67]:


# this means that the Monday, 4 poptarts were bought, Tuesday, 4 more, etc.
# now combine this week's total into one value for the axis summation

weekly_demand = poptarts.sum(axis=1)
weekly_demand


# In[68]:


# Now we have to find how many weeks have less than the 17 poptarts they restock

(weekly_demand < 17).mean() # add up all the totals less than 17, and divide by 100,000


# In[ ]:




