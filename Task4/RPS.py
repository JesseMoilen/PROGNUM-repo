#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#question 4.3
import numpy as np
Ihand=input("input the desired hand(R, P, S): ")  #first the user inputs their move
if Ihand != 'R' and Ihand!= 'P' and Ihand!= 'S':
    print('Hey there you silly boy, thats not a legal move!') #if their move is non legal, ie not R, P or S, return a funny line telling them so
RNGhand=np.random.randint(-1, 1) #now generate an integer between -1 and 1
N=0 
#assign the random number a move in the game:
if RNGhand == 0:
    N='R'
elif RNGhand > 0:
    N='P'
else:
    N='S'

#give all possible combinations of the user input vs the generated move and generate the consequent conclusion
if N=='R':
    if Ihand == 'R':
        print('The computer chose rock, its a draw :/')
    if Ihand == 'P': 
        print('The computer chose rock, you won! :)')
    if Ihand == 'S':
        print('Womp Womp, the computer chose rock, you lost :(')
        
if N=='P':
    if Ihand == 'R':
        print('Womp Womp, the computer chose paper, you lost :(')
    if Ihand == 'P': 
        print('The computer chose paper, its a draw :/')
    if Ihand == 'S':
        print('The computer chose paper, you won! :)')

if N=='S':
    if Ihand == 'R':
        print('The computer chose scissors, you won! :)')
    if Ihand == 'P': 
        print('Womp Womp, the computer chose scissors, you lose :(')
    if Ihand == 'S':
        print('The computer chose scissors, its a draw :/')

