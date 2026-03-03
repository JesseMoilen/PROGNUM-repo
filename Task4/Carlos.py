#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#question 4.6
import numpy as np
def integ(func, a, b, n=10000000):
    x=np.random.uniform(a, b, n)
    fx=eval(func)
    inty=(b-a)*np.mean(fx)
    return inty

func = input('Input the desired function: ')
a = float(input('Lower boundary: '))
b = float(input('upper boundary: '))
area = integ(func, a, b)
print(f'The solution of the integral from the given bounds and function = {area}')

