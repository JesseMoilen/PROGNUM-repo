#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#2.21
f1 = 1
f2 = 2

for i in range(99):
    f1 += f2
    f3 = f1
    f1 = f2
    f2 = f3

print(f1)

