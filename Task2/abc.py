#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##
import math
# first input the wanted values for a, b and c
a = float(input("The assigned value for a = ")) 
b = float(input("The assigned value for b = "))
c = float(input("The assigned value for c = "))
#next calculate D
D = int(b**2 - 4 * a * c)
print(f"The corresponding discriminant value = {D}")

#Give all combinations of D
if D > 0:
    x_1 = (-b + math.sqrt(D)) / (2*a)
    x_2 = (-b - math.sqrt(D)) / (2*a)
    print(f"The first solution: x1 = {x_1}")
    print(f"The second solution: x2 = {x_2}")

elif D==0:
    x_3= (-b)/(2*a)
    print(f"The solution: x = {x_3}")

else:
    print(f"The discriminant is smaller than zero, thus there are no real solutions")

