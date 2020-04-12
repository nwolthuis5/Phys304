
# coding: utf-8

# In[7]:


import numpy as np
print('problem 2.2')

#Some Gravitational Physics, Problem 2.2
T = float(input("please input a time for the satalite's orbital period in minutes: "))

#assigning values to constants, SI units
M = 5.97 * 10 ** (24)
G = 6.67 * 10 ** (-11)
R = 6371* 10 ** (3) #meters

#derived equation for  above earth's surface
h = ((G*M*(T*60)**2)/(4*np.pi**2))**(1/3) - R

#printing the height
print("the height of the satelite is", h, "meters")

