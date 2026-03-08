#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from numpy import sin, cos, e, pi
from scipy.integrate import quad

def Inty():
    expr=input('enter desired functoin f(x): ')
    a, b = 0, pi
    
    def f(x):
        try:
            return eval(expr, {"x": x, "sin": sin, "cos": cos, "e": e, "pi": pi}) 
        except NameError as er: 
            raise NameError(f"Unknown function or variable: {er}") 
        except SyntaxError: 
            raise SyntaxError("Invalid syntax in expression.")
        except Exception as er: 
            raise Exception(f"Evaluation error: {er}")  
    try:
        sq_res, _ = quad(f, a, b)
        N=100000
        X=np.random.uniform(a, b, N)
        F=np.array([f(val) for val in X])
        MC=(b-a)*np.mean(F)
        print(f"SciPy Result: {sq_res}")
        print(f"Monte Carlo Result: {MC}")
    except (NameError, SyntaxError, Exception) as er:
        print(f'error: {er}')
if __name__=="__main__":
    Inty()

