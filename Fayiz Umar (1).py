#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import time


# In[3]:


start_time = time.time()
data_set=pd.read_csv("C:/Users/DELL/Downloads/bike_data_new.csv")
data_set


# In[4]:


data_set_1 = data_set[data_set['started_at'] != data_set['ended_at']]


# In[5]:


data_set_1


# In[6]:


data_set_2 = data_set[data_set['started_at'] == data_set['ended_at']]


# In[7]:


data_set_2


# In[8]:


data_set_1


# In[9]:


data_set_1['started_at'] = pd.to_datetime(data_set_1['started_at'])
data_set_1['ended_at'] = pd.to_datetime(data_set_1['ended_at'])


# In[10]:


data_set_1['duration'] = (data_set_1['ended_at'] - data_set_1['started_at']).astype('timedelta64[m]')


# In[11]:


data_set_1


# In[12]:


max_duration = data_set_1['duration'].max()
print("maximum duration of trip is = ",max_duration,"minutes")


# In[13]:


type(max_duration)


# In[14]:


min_duration = data_set_1['duration'].min()
print("minimum duration of trip is = ",min_duration,"minutes")


# In[15]:


min_no = data_set_1['duration'].value_counts().min()
min_no


# In[16]:


cir_data = data_set_1[(data_set_1['start_lat'] == data_set_1['end_lat']) & (data_set_1['start_lng'] == data_set_1['end_lng']) & 
                      data_set_1['start_lat'].notna() & 
                      data_set_1['start_lng'].notna() & 
                      data_set_1['end_lat'].notna() & 
                      data_set_1['end_lng'].notna() ]


# In[17]:


cir_data


# In[18]:


total_trips = len(data_set_1)
circular_trips = len(cir_data)
percentage = circular_trips / total_trips * 100
print(f"Percentage of circular trips: {percentage:.2f}%")


# In[19]:


end_time = time.time()
total_runtime = end_time - start_time
total_runtime


# In[20]:


start_time


# In[21]:


end_time


# In[22]:


#making it as a function


# In[23]:


def intern(data_set):
    start_time = time.time()
    data_set_1 = data_set[data_set['started_at'] != data_set['ended_at']]
    
    data_set_1['started_at'] = pd.to_datetime(data_set_1['started_at'])
    data_set_1['ended_at'] = pd.to_datetime(data_set_1['ended_at'])
    data_set_1['duration'] = (data_set_1['ended_at'] - data_set_1['started_at']).astype('timedelta64[m]')
    max_duration = data_set_1['duration'].max()
    print("maximum duration of trip is = ",max_duration,"minutes")
    
    min_duration = data_set_1['duration'].min()
    print("minimum duration of trip is = ",min_duration,"minutes")
    min_no = data_set_1['duration'].value_counts().min()
    print("count is = ",min_no)
    
    cir_data = data_set_1[(data_set_1['start_lat'] == data_set_1['end_lat']) & (data_set_1['start_lng'] == data_set_1['end_lng']) & 
                      data_set_1['start_lat'].notna() & 
                      data_set_1['start_lng'].notna() & 
                      data_set_1['end_lat'].notna() & 
                      data_set_1['end_lng'].notna() ]
    
    total_trips = len(data_set_1)
    circular_trips = len(cir_data)
    percentage = circular_trips / total_trips * 100
    print(f"Percentage of circular trips: {percentage:.2f}%")
    
    end_time = time.time()
    total_runtime = end_time - start_time
    print(f"Total runtime for the function: {total_runtime:.2f} seconds")
    
    return data_set

    
    
    


# In[24]:


data_set=pd.read_csv("C:/Users/DELL/Downloads/bike_data_new.csv")
data_set


# In[25]:


data_set = intern(data_set)


# In[26]:


data_set['started_at'] = pd.to_datetime(data_set['started_at'])
data_set


# In[28]:


start_time= (data_set['started_at'].dt.hour >= 6) & (data_set['started_at'].dt.hour <= 17)
d2 = data_set.loc[start_time]
d2


# In[ ]:


feasible_pairs = 0
for i in range(len(d2)-1):
    print(f"i = {i}")
    end_loc = d2.iloc[i]['end_lng']
    end_time = pd.to_datetime(d2.iloc[i]['ended_at'])
    for j in range(i+1, len(d2)):
        print(f"j = {j}")
        start_loc = d2.iloc[j]['start_lng']
        start_time = pd.to_datetime(d2.iloc[j]['started_at'])
        if end_loc == start_loc and start_time >= end_time:
            feasible_pairs += 1
print(f"feasible_pairs = {feasible_pairs}")


# In[ ]:


print("Total number of feasible pairs of trips: ", feasible_pairs)
print("Runtime: ", end_time - start_time)


# In[ ]:




