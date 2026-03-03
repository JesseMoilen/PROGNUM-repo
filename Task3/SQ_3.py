#!/usr/bin/env python
# coding: utf-8

# In[25]:


masses = [1.9891e+30, 1.8986e+27, 
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23, 
          3.3022e+23, 7.349e+22, 1.25e22]

Slasses = slice(6, 11)
Massies = masses[Slasses]

MM=7.349e+22 #mass of the moon
for M in masses:
    if M/MM < 1:
        masses.remove(M)
for M in masses:
    if M/MM == 1:
        masses.remove(M)
print(masses)
print()
Slasses = slice(6, 11)
print(Massies)

ObiMass = sum(Massies)
Lenght= len(Massies)
Amass = ObiMass / Lenght
print(Amass)


# In[ ]:




