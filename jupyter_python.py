#!/usr/bin/env python
# coding: utf-8

# # Import Pandas

# In[1]:


import pandas as pd


# # Import Data

# In[10]:


names= ['id', 'title', 'year','rating', 'votes', 'length', 'genres']
data= pd.read_csv('imdb_top_10000.txt', sep="\t", names=names,index_col=0)


# # Exploring our Data

# In[12]:


data.head()


# In[13]:


data.head(1)


# In[14]:


data.tail()


# In[15]:


data.info()


# In[16]:


data.describe()


# # Exporting Data

# In[18]:


data.to_csv('test.csv', header=True, index=True, sep=',')


# # Sorting Data

# In[19]:


data.sort_values(by='rating')


# In[20]:


data.sort_values(by='rating', ascending=False)


# # Creating Data Frames From Scratch

# In[21]:


sample_data={
    'tv': [230, 34, 17],
    'radio':[37, 39, 45],
    'news':[69, 45, 69],
    'sales':[22, 10, 39]
}


# In[23]:


data2 = pd.DataFrame(sample_data)


# In[24]:


data2


# In[25]:


data['title']


# In[26]:


data[['title', 'year']]


# In[27]:


data['rating'].mean()


# In[28]:


data['rating'].max()


# In[29]:


data['rating'].min()


# In[30]:


data['genres'].unique()


# In[32]:


data['rating'].value_counts()


# In[34]:


data['rating'].value_counts().sort_index()


# In[36]:


data['rating'].value_counts().sort_index(ascending=False)


# # Plotting

# In[37]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[39]:


data.plot()


# In[40]:


data.plot(kind='scatter', x= 'rating', y='votes')


# In[41]:


data.plot(kind='scatter', x= 'rating', y='votes', alpha=0.3)


# In[42]:


data['rating'].plot(kind='hist')


# In[44]:


import seaborn as sns


# In[45]:


sns.lmplot(x='rating', y='votes', data=data)


# In[47]:


sns.pairplot(data)


# # Ordinary least square Regression

# In[49]:


import statsmodels.api as sm


# In[51]:


results = sm.OLS(data['votes'], data['rating']).fit()


# In[52]:


results.summary()


# # Advance Data Selection

# In[53]:


data['year']


# In[54]:


data[data['year']>1995]


# In[56]:


data['year']>1995


# In[57]:


data[data['year']==1966]


# In[59]:


data[(data['year'] > 1995) & (data['year']<2000)]


# In[60]:


data[(data['year'] > 1995) | (data['year']<2000)]


# In[63]:


data[(data['year'] > 1995) & (data['year'] < 2000)].sort_values(by='rating', ascending=False).head(10)


# # Grouping

# In[64]:


data.groupby(data['year'])['rating'].mean()


# In[65]:


data.groupby(data['year'])['rating'].min()


# # Challenges

# 1. What was the highest scoring movie in 1996?
# 2. In what year was the highest rated movie of all time made?
# 3. What five movies have the most votes ever?
# 4. What year in the 1960s had the highest movie rating?

# In[80]:


data[data['year']==1996].sort_values(by='rating', ascending=False).head()


# In[81]:


data[data['year']< 2011].sort_values(by='rating', ascending=False).head()


# In[72]:


data[data['year']< 2016].sort_values(by='votes', ascending=False).head(5)


# In[84]:


data[(data['year'] > 1959) & (data['year'] < 1970)].groupby(data ['year'])['rating'].mean()


# # Cleaning Data

# In[87]:


data['formatted title']= data['title'].str[:-7]


# In[88]:


data.head()


# In[94]:


data['formatted title'] = data['title'].str.split('\(').str[0]


# In[95]:


data.head()


# In[112]:


data['formatted title']= data['title'].str.split('\(').str[0]


# In[113]:


data.head()


# In[116]:


data['length'].str.split().str.get(0).astype('int') 


# In[117]:


sns.pairplot(data)


# In[118]:


data[data['formatted length']==0]


# In[ ]:




