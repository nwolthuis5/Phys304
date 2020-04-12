
# coding: utf-8

# In[5]:


#importing goodies
import functools
import numpy as np
import math
import matplotlib.pyplot as plt
from wolthuis_hw4_gaussxw import gaussxw

#trying to make it the latex font stuff
from matplotlib import rc
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
plt.rc('font',**{'family':'serif','serif':['Times New Roman']})
plt.rc('text', usetex=True)

print("Problem 5.12")

#units are a social construct
#defining some constants for future use
hbar = 1.054 * 10 ** (-34) #units of not! eV
c = 2.998 * 10 ** 8 #meters per second
kb = 1.381 * 10 ** (-23) #units of boltzmann's constant


# In[6]:


#defining the fuction so that I can integrate it later
def f(x):
    val = x**3 / (np.exp(x) - 1)
    return val

#using Z substitution to deal with the 0 to inf range, allowing us to modify it to be from 0 to 1 later
def fz(z):
    
    #defining x in terms of z so that we can call back to the non Z sub function
    x = z / (z - 1)
    
    #shenanigans
    val = (1/((1 - z)**2) * f(z / (1 - z)))
    return val


# In[7]:


#Using Gaussian Quadrature to integrate the function
def W(T):
    #defining parameters of integration
    N = 50
    a = 0.0
    b = 1.0
    
    #calculating sample points and weights then mapping them onto the domain
    x , w  = gaussxw(N)
    xp = 0.5*(b-a)*x + 0.5*(b+a)
    wp = 0.5*(b-a)*w
    
    #performing gaussian integration with the 
    s = 0.0
    for i in range(N):
        s += wp[i]*fz(xp[i])
    
    #using the previously calculated integral with the other non-integrated factors to get our output
    val = (kb**4)*(T**4)/(4*(np.pi**2)*(c**2)*(hbar**3))*s
    return val


# In[8]:


T = float(input("please choose a positive real number for the temperature in Kelvin: "))

#defining parameters of integration
N = 150
a = 0.0
b = 1.0
    
#calculating sample points and weights then mapping them onto the domain
x , w  = gaussxw(N)
xp = 0.5*(b-a)*x + 0.5*(b+a)
wp = 0.5*(b-a)*w
    
#performing gaussian integration with the Z substitution function made above
s = 0.0
for i in range(N):
    s += wp[i]*fz(xp[i])
    
#using the previously calculated integral with the other non-integrated factors to get our output
val = (kb**4)*(T**4)/(4*(np.pi**2)*(c**2)*(hbar**3))*s
    
#trying to determine the stefan-boltzmann constant
stefbolt = ((kb**4)/(4*(np.pi**2)*(c**2)*(hbar**3)))*s
    
#returning the output values we want
print("The total rate for which energy is dispersed per unit area for all frequencies is", val)
print("The Stefan-Boltzmann constant is determined to be approximately", stefbolt)

