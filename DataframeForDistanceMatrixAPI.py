
# coding: utf-8

# 
# 
# # Script to generate input for Google Map API
# 
# Python script for creating a dataframe of latitude and longitude to be passed to Distance Matrix API.
# 
# This is for all pair shortest distance problem.
# 
# Points - [a,b,c,d,e,f,g,h]
# 
# This script will give us pairs of 
# [
# 
# (a,b)(a,c)(a,d)(a,e)(a,f)(a,g)(a,h)  = 7
# 
# (b,c)(b,d)(b,e)(b,f)(b,g)(b,h)       = 6
# 
# (c,d)(c,e)(c,f)(c,g)(c,h)            = 5
# 
# (d,e)(d,f)(d,g)(d,h)  = 4
# 
# (e,f)(e,g)(e,h)   = 3
# 
# (f,g)(f,h)  =   2
# 
# (g,h)    = 1
# 
# ]
# 
# Input - Points (n)
# 
# Output - Pairs [(n * n-1 )/ 2]
# 
# 
# # Google API Information :
# 
# If we have 'n' points 
# then, Total Number of Pairs would be 'P' = (n)(n-1)/2
# 
# 
# Total Number of API Calls would be 'P'.
# 
# ### Input/request to API - 
# 
# CSV File
# 
# Lat1, Long1, Lat2, Long2
# 
# ### Output/response from API -
# 
# CSV File and Distance Matrix
# 
# Rajiv Jha
# 31st August 2018
# 

# # Raw Exploration of CSV Input file

# In[25]:



import pandas as pd


# In[26]:


df = pd.read_csv('addressStoresGeoTagged.csv')


# In[27]:


df.head()


# In[28]:


df.shape


# In[29]:


df.accuracy.nunique()


# In[30]:


df.number_of_results.nunique()


# In[31]:


df.number_of_results.unique()


# In[32]:


df.accuracy.unique()


# In[33]:


df.groupby('accuracy').count()


# In[34]:


df.groupby('status').count()


# In[35]:


df.groupby('latitude').count()


# In[36]:


df.latitude.nunique()


# In[37]:


df.longitude.nunique()


# In[38]:


df.shape


# In[39]:


newdf = df[['longitude', 'latitude']].copy()


# In[40]:


newdf.columns = ['long1', 'lat1']


# In[41]:


newdf.head()


# In[42]:


newdf.insert(0, 'New_ID', range(1, 1 + len(newdf)))


# In[43]:


newdf.head()


# In[44]:


newdf.insert(0, 'key', 0)


# In[45]:


result = pd.merge(newdf, newdf,on='key')


# In[46]:


result


# In[47]:


finalresult = result.loc[result['New_ID_x'] < result['New_ID_y']]


# In[48]:


finalresult.shape


# In[49]:


finalresult


# In[50]:


459*458/2


# In[51]:


finalresult = finalresult.drop(['key', 'New_ID_x','New_ID_y'], axis=1)


# In[52]:


finalresult


# In[53]:


finalresult.columns = ['long1', 'lat1','long2','lat2']


# In[54]:


finalresult


# In[55]:


finalresult.to_csv('coordinatematrixStores.csv', index = False )

