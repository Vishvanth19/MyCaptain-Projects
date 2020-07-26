#!/usr/bin/env python
# coding: utf-8

# In[16]:


# Importing dependencies
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
get_ipython().run_line_magic('matplotlib', 'inline')


# In[17]:


# Using pandas to read the database stored in the same folder
data = pd.read_csv('mnist_train.csv')
data2 = pd.read_csv("mnist_test.csv")


# In[18]:


# View column heads
data.head()


# In[19]:


data2.head()


# In[20]:


# Extracting data from the dataset and viewing them upclose
a = data2.iloc[3,1:].values


# In[21]:


# Reshaping the extracted data
a=a.reshape(28,28).astype('uint8')
plt.imshow(a)


# In[22]:


# Preparing the data
# Seperating labels and data values
df_x = data2.iloc[:,1:]
df_y = data2.iloc[:,0]


# In[23]:


# creating test and train size 
x_train, x_test , y_train, y_test = train_test_split(df_x,df_y,test_size=0.2,random_state=4)


# In[24]:


# Check data
y_train.head()


# In[27]:


# Call classifier
rf= RandomForestClassifier(n_estimators=100)


# In[28]:


#Fit the model
rf.fit(x_train, y_train)


# In[29]:


# Prediction on test data
pred = rf.predict(x_test)


# In[30]:


pred


# In[31]:


# Check prediction accuracy
a = y_test.values

# Calculate number of correctly predicted values
count=0
for i in range(len(pred)):
    if pred[i]==a[i]:
        count=count+1


# In[32]:


count


# In[33]:


# check total values to be predicted
len(pred)


# In[34]:


# Accuracy value
1898/2000


# In[ ]:




