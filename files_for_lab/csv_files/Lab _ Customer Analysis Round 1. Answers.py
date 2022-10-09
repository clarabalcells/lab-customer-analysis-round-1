#!/usr/bin/env python
# coding: utf-8

# In[53]:


import pandas as pd
import numpy as np
import glob


# In[54]:


pd.read_csv('file1.csv')


# In[55]:


pd.read_csv('file2.csv')


# In[56]:


pd.read_csv('file3.csv')


# In[64]:


# Reading data files into a DataFrame
pd.read_csv('file3.csv')
pd.read_csv('file2.csv')
pd.read_csv('file1.csv')
file1 = pd.read_csv('file1.csv')
file2 = pd.read_csv('file2.csv')
file3 = pd.read_csv('file3.csv')


# In[67]:


df1 = pd.DataFrame(file1)
display(df1)
df1.shape

df2 = pd.DataFrame(file2)
display(df2)
df2.shape

df3 = pd.DataFrame(file3)
display(df3)
df3.shape


# In[71]:


display("file 1")
df1 = pd.DataFrame(file1)
display(df1)
df1.shape

display("file 2")
df2 = pd.DataFrame(file2)
display(df2)
df2.shape

display("file 3")
df3 = pd.DataFrame(file3)
display(df3)
df3.shape     


# In[72]:


file1_coloumns = file1.columns
display(file1_coloumns)

file1_coloumns2 = file2.columns
display(file1_coloumns2)
file1_coloumns3 = file3.columns
display(file1_coloumns3)


# In[73]:


print (df1.shape)
print (df2.shape)
print (df3.shape)


# In[87]:


df1 = df1.rename(columns={"ST": "State"})
df1

df2 = df2.rename(columns={"ST": "State"})
df2

df1 = df1.rename(columns={"GENDER": "Gender"})
df1

df2 = df2.rename(columns={"GENDER": "Gender"})
df2


# In[88]:


df1
df2
df3


# In[22]:


data = pd.concat([df1,df2,df3], axis=0)
print(data.shape)


# In[18]:


pd.concat([df1, df2, df3]) 


# In[13]:


newdata = data.drop(columns="Education")


# In[14]:


duplicates = data[data.duplicated()]
duplicates


# In[24]:


df = pd.concat(map ['df1''df2', 'df2])


# In[ ]:


data.value_counts(dropna=True) 
data


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




