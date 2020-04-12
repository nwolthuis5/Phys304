
# coding: utf-8

# In[6]:


print('8.2')
#importing stuff
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt

#trying to make it the latex font stuff
from matplotlib import rc
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
plt.rc('font',**{'family':'serif','serif':['Times New Roman']})
plt.rc('text', usetex=True)


# In[15]:


alpha = 1
beta  = .5
gamma = beta
delta = 2


def f(r,t):
    #setting up intial values
    x  = r[0]
    y  = r[1]
    fx = (alpha * x) - (beta * x * y)
    fy = (gamma * x * y) - (delta * y)
    return np.array([fx , fy],float)
    
a =  0.0
b = 30.0
N = 10000

#the larger the step size, the faster the plot envelopes and goes to zero
h = (b-a)/N

tpoints = np.arange(a,b,h)
xpoints = []
ypoints = []

#rungee kutta
r = np.array([2,2],float)
for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1, t+0.5*h)
    k3 = h*f(r+0.5*k2, t+0.5*h)
    k4 = h*f(r+k3, t+h)
    r += (k1 + 2*k2 + 2*k3 + k4)/6
pl.plot(tpoints, xpoints, label = 'rabbits')
pl.plot(tpoints, ypoints, label = 'foxes')
pl.legend()
pl.xlabel( "t")
pl.ylabel("population in thousands")
pl.title("The Fox and the Hou-are")
pl.show()

