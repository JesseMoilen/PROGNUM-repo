#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Julian date calculator 

D = float(input("input a day: "))
M = float(input("input a month: "))
Y = float(input("input a year: "))

J = 367*Y -7*(Y+(M+9)/12)/4 - 3*((Y+(M-9)/7)/100 + 1)/4 + (275*M)/9 + D + 1721029-0.5

print(f"converted to a julian date this yields: {J}")

