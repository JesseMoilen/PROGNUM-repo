#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def Gaus(x, A, x0, sigma, z0):
    return A * np.exp(-(x - x0)**2 / (2 * sigma**2)) + z0

# User Inputs
A = float(input("Enter desired amplitude: "))
x0 = float(input("Enter desired x0: "))
sig = float(input("Enter desired width: "))
z0 = float(input("Enter Y-offset z0: "))
low = float(input("Enter lower bound: "))
up = float(input("Enter upper bound: "))

# Calculate area
area, _ = quad(Gaus, low, up, args=(A, x0, sig, z0))

# Plotting
x = np.linspace(x0 - 5*sig, x0 + 5*sig, 500)
y = Gaus(x, A, x0, sig, z0)

plt.plot(x, y, 'b-', label='Gaussian')
X = np.linspace(low, up, 200)
Y = Gaus(X, A, x0, sig, z0)
plt.fill_between(X, Y, color='red', alpha=0.3, label=f'Area: {area:.4f}')

plt.legend()
plt.title(f"Integration Result: {area:.4f}")
plt.show()

