
# coding: utf-8

# In[26]:


#importing goodies
import functools
import numpy as np
import math
import matplotlib.pyplot as plt
from pylab import *
from scipy.integrate import dblquad


#trying to make it the latex font stuff
from matplotlib import rc
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
plt.rc('font',**{'family':'serif','serif':['Times New Roman']})
plt.rc('text', usetex=True)

print("Problem 5.14")

#defining some constants for future use
G = 6.71 * 10 ** (-11)


# In[52]:


#computing the force on an object as a function of vertical distance from the center of the plate
def F(z):
    
    #defining the integrand
    def f(y, x):
        val = 1 / ((x**2 + y**2 + z**2)**(3/2))
        return val
    
    #defining limits of y integration
    def ylower(x):
        return -5
    def yupper(x):
        return 5

    nt, error = dblquad(f,-5,5,ylower,yupper)
    
    #defining mass and area
    m = 10**4
    A = 10 **2
    sig = m / A
    
    #retrieving the value for the function output    
    val = G* z * sig* nt
    return val


# In[57]:


#making lists for the purpose of plotting the function
y = []
x = []

#looping through the necessary values
for i in np.linspace(0, 10,100):
    val = F(i)
    y.append(val)
    x.append(i)
    
# definitions for the axes
left, width = 0.1, 0.65
bottom, height = 0.1, 0.65
spacing = 0.005

#plotting the function
plt.plot(x,y , label = "Gravitational Force Exerted on a Mass", color = 'k')


#Formatting, Labels, & Legends
plt.xlabel('Distance in Meters')
plt.ylabel('Force in Newtons')
plt.title('Force as a Function of Distance from a Plate')
plt.legend()

#Line of best fit
#plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 2))(np.unique(x)))

plt.show()

