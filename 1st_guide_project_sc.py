#!/usr/bin/env python
# coding: utf-8

# This is the first guided project that we are going to implement. Again here we use *autos.csv* dataset. Where some of the column name are dataCrawled, name, seller, offerType, price, abtest, vehicleType etc.

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


autos = pd.read_csv('autos.csv', encoding = 'Latin-1')


# In[29]:


autos


# Here DataFrame.head() print or indicate first some rows from the *autos.csv* file. Here we print 5 rows.

# In[4]:


#df = pd.DataFrame()
autos.head(5)


# Here DataFrame.info() method give us the total overview about our dataset *autos.csv*. 

# In[5]:


autos.info(5)


# In[6]:


col = list(autos.columns)
print(col)


# Here in this section we try to find out the columns name using 
# DataFrame.columns attribute. Then we change some of the columns name such as *yearOfRegistration* to *registration_year* etc. After that we assigned the changed columns name to the original list. Using DataFrame.head() attribute we examined the changed stuff.

# In[7]:


i = -1
for row in col:
    i += 1
    if row == 'yearOfRegistration':
        col[i] = 'registration_year'
    elif row == 'monthOfRegistration':
        col[i] = 'registration_month'
    elif row == 'notRepairedDamage':
        col[i] = ' unrepaired_damage'
    elif row == 'dateCreated':
        col[i] = 'ad_created'
    
print(col)        


# In[8]:


autos.columns = col
print(list(autos.columns))


# In[9]:


autos.head(5)


# Here *DataFrame.describe()* method is used to view some basic statistical details like percentile, mean, std etc. of a data frame.

# In[10]:


autos.describe(include = 'all')


# Removing any non-numeric characters from *price* column

# In[11]:


# for row in autos[][:

#     row = re.sub("[^0-9]", "", row)

p = list(autos['price'])

for index,row in enumerate(p):
   
    numeric_filter = filter(str.isdigit, row)
    numeric_string = "".join(numeric_filter)

    row = numeric_string
   
    p[index] = row
autos['price'] = p
print(autos['price'])



# Removing any non-numeric character from *odometer* column

# In[12]:


q = list(autos['odometer'])

for index,row in enumerate(q):
   
    numeric_filter = filter(str.isdigit, row)
    numeric_string = "".join(numeric_filter)

    row = numeric_string
   
    q[index] = row
autos['odometer'] = q
print(autos['odometer'])


# Converting the column to a numeric dtype

# In[13]:


autos['price'] = autos['price'].apply(pd.to_numeric)
# autos['price'] = autos['price'].astype(int)


# In[14]:


autos['odometer'] = autos['odometer'].apply(pd.to_numeric)


# Renaming the *odometer* to *odometer_km*

# In[15]:


autos.rename(columns = {'odometer' : 'odometer_km'}, inplace = True)
autos.head(5)


# In[16]:


max_price = max(autos['price'])
print(max_price)
min_price = min(autos['price'])
print(min_price)


# In[17]:


max_odo = max(autos['odometer_km'])
print(max_odo)
min_odo = min(autos['odometer_km'])
print(min_odo)


# In[18]:


autos['price'].unique().shape


# In[19]:


autos['price'].describe()


# In[20]:


autos['price'].value_counts()


# In[21]:


autos['price'].sort_index(ascending = True).head(50)


# 2.1.7.5:  Exploring the Date columns. *dateCrawled*

# In[26]:


autos['dateCrawled'].value_counts(normalize = True, dropna = False)


# In[28]:


autos['dateCrawled'].sort_index(ascending =True)


# 2.1.7.5:   Exploring the date columns *last_seen*

# In[31]:


autos['ad_created'].value_counts(normalize = True, dropna =False)


# In[32]:


autos['ad_created'].sort_index(ascending = True)


# 2.1.7.5: Exploring the date columns *last_seen*

# In[34]:


autos['lastSeen'].value_counts(normalize = True, dropna = False)


# In[ ]:


autos['lastSeen'].sort_index(ascending = True)


# In[36]:


autos['registration_year'].describe()


# Here in the *registration_year* column we see that the maximum value or year is 9999 and the min value or year is 1000. Which seems to look impractical. Because 9999's is too far from the present day. And again in 1000's car was not invented.

# 2.1.7.6: Dealing with Incorrect Registration year Data

# In[46]:


ots = []
for row in autos['registration_year']:
    if row > 2016 or row <1900:
        ots.append(row)

print(ots)        
# num_ots = ots.count()
print(len(ots))


# Here from above column we see that there are **1972** columns or car that fall outside the **1900-2016** interval.

# 2.1.7.7: Exploring Price by Brand

# In[50]:


autos['brand'].value_counts()


# In[54]:


vc = autos['brand'].value_counts(normalize = True)
print(vc)


# In[58]:


# top_20 = []
# for row in vc:
#     if row > .05:
#         top_20.append(row)
# print(top_20)        
top_20 = vc > 0.05
print(top_20)


# In[63]:


per_5 = vc[top_20]
print(per_5)


# Here from above we see that total **six car band** have over a percentage over 5%.
# 
# 
# volkswagen       0.21374
# opel             0.10922
# bmw              0.10858
# mercedes_benz    0.09468
# audi             0.08566
# ford             0.06958

# In[ ]:


agg_data = {}
for row in top_20:
    per_5 = vc[top_20]
    if per_5 in agg_data:
        agg_data[per_5]
    
        


# 2.1.7.9: 

# In[ ]:




