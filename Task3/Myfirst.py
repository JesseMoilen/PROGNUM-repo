#!/usr/bin/env python
# coding: utf-8

# Answers for week 1
# 
# * Name: Jesse van der Meulen 
# * Username: jrhmeulen
# * Student s-number: S6445128
# * Group: AS1

# In[1]:


x=22/7


# $$y=\frac{sin(x)}{x}$$

# In[2]:


pi = 22/7 # Processed on Jupyter Hub


# $$F=G\frac{m_1m_2}{r^2}$$

# In[9]:


from scipy.constants import G

m_1=7.342e22
m_2=5.9722e24
r=385000600

F=G*(m_1*m_2)/(r**2)

print(F)


# In[ ]:




