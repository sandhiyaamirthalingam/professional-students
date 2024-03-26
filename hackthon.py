#!/usr/bin/env python
# coding: utf-8

# In[3]:


import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


df=pd.read_csv('ElectricCarData_Clean.csv')
df.head(6)


# In[7]:


df['TopSpeed_KmH'].unique()


# In[12]:


df1=df.loc[(df['TopSpeed_KmH']=='150')]


# In[7]:


df1.head()


# In[1]:


df1=df.loc[(df['brand']=='honda')]


# In[14]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
df=pd.read_csv('ElectricCarData_Clean.csv')
df.head(6)


# In[15]:


df['Brand'].unique()


# In[11]:


df1=df.loc[(df['brand']=='honda')]


# In[8]:


import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('ElectricCarData_Clean.csv')
df.head()


# In[9]:


df['Brand'].unique()


# In[16]:


df.plot(kind='bar',figsize=(16,10))


# In[ ]:




