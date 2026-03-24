#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Question 6.14
import numpy as np

class Fibonacci:
    
    def __init__(self):
        self.a = 0
        self.b = 1
        
    def bolleN(self, n):
        a = self.a
        b = self.b
        for _ in range(2, n):
            a, b = b, a+b
        return b
    
    def watdebal(self, n, m):
        a = self.a
        b = self.b
        resultje=[]
        for _ in range(2, n):
            if b % m == 0:
                resultje.append(b)
            a, b = b, a+b
        return resultje
n=int(input('input n: '))
m=int(input('input m: '))
bibi = Fibonacci()

print(f'The Nth term in the fibonacci sequence: {bibi.bolleN(n)}')
print(f'All terms below the Nth divisible by m: {bibi.watdebal(n, m)}')

