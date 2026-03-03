#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##question 3.22 Session Quiz
import numpy as np
import matplotlib.pyplot as plt

#x= np.array(list(range(-5, 6)))
x= np.arange(-5, 6)
y= np.cosh(x)
plt.plot(x, y, linestyle = '-', color='green', label='y = cosh(x)')
plt.title('Catenary = y=cosh(x)')
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.xticks(ticks=range(5, 6))
plt.yticks()
plt.legend()
plt.show()

