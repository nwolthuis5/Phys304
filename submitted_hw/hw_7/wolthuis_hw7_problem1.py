
# coding: utf-8

# In[2]:


print('8.4a')
#collaboration with Shufan Xia, Katharine Bancroft, and Helena Frisbie-Firsching

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


# In[3]:


#setting up constants
l = .10 #meters
g = 9.81 #meters per second ^2

#defining the equation of motion for the problem
def f(r1,t1):
    theta = r1[0]
    omega = r1[1]
    ftheta = omega
    fomega = -(g/l)*np.sin(theta)
    return np.array([ftheta,fomega],float)


# In[4]:


#implementing a Rungee-Kutta
a1 =  0.0
b1 = 100.0
N1 = 10000

#the larger the step size, the faster the plot envelopes and goes to zero
h1 = (b1-a1)/N1

tpoints1 = np.arange(a1,b1,h1)
xpoints1 = []
ypoints1 = []

#rungee kutta
r1 = np.array([3.124,0],float)
for t1 in tpoints1:
    xpoints1.append(r1[0])
    ypoints1.append(r1[1])
    k1 = h1*f(r1,t1)
    k2 = h1*f(r1+0.5*k1, t1+0.5*h1)
    k3 = h1*f(r1+0.5*k2, t1+0.5*h1)
    k4 = h1*f(r1+k3, t1+h1)
    r1 += (k1 + 2*k2 + 2*k3 + k4)/6
pl.plot(tpoints1, xpoints1)
#pl.plot(tpoints1, ypoints1)
pl.xlabel( "t")
pl.title("Theta Over Time")
pl.show()


# In[5]:


print('8.5 a')


# In[6]:


#setting up constants
l = 0.10 #meters
g = 9.81 #meters per second ^2
C = 2 #seconds ^ (-2)
Omega = 5 #seconds ^ (-1)

#defining the equation of motion for the problem
def f2(r2,t2):
    theta = r2[0]
    omega = r2[1]
    ftheta = omega
    fomega = -(g/l)*np.sin(theta) + C*np.cos(theta)*np.sin(Omega*t2)
    return np.array([ftheta,fomega],float)


# In[10]:


#implementing a Rungee-Kutta
a2 =  0.0
b2 = 100.0
N2 = 10000
h2 = (b2-a2)/N2

#setting up lists
tpoints2 = np.arange(a2,b2,h2)
xpoints2 = []
ypoints2 = []

#making a blank array
r2 = np.array([0,0],float)

#setting up a for loop to fill the array
for t2 in tpoints2:
    xpoints2.append(r2[0])
    ypoints2.append(r2[1])
    k1 = h2*f2(r2,t2)
    k2 = h2*f2(r2+0.5*k1, t2+0.5*h2)
    k3 = h2*f2(r2+0.5*k2, t2+0.5*h2)
    k4 = h2*f2(r2+k3, t2+h2)
    r2 += (k1 + 2*k2 + 2*k3 + k4)/6
pl.plot(tpoints2, xpoints2)
#pl.plot(tpoints2, ypoints2)
pl.xlabel( "t")
pl.title("Theta Over Time")
pl.show()


# In[11]:


#changing the omega to the natural frequency
Omega = (g/l)**(1/2) #seconds ^ (-1)

#implementing a Rungee-Kutta
a2 =  0.0
b2 = 100.0
N2 = 10000
h2 = (b2-a2)/N2

#setting up lists
tpoints2 = np.arange(a2,b2,h2)
xpoints2 = []
ypoints2 = []

#making a blank array
r2 = np.array([0,0],float)

#setting up a for loop to fill the array
for t2 in tpoints2:
    xpoints2.append(r2[0])
    ypoints2.append(r2[1])
    k1 = h2*f2(r2,t2)
    k2 = h2*f2(r2+0.5*k1, t2+0.5*h2)
    k3 = h2*f2(r2+0.5*k2, t2+0.5*h2)
    k4 = h2*f2(r2+k3, t2+h2)
    r2 += (k1 + 2*k2 + 2*k3 + k4)/6
pl.plot(tpoints2, xpoints2)
#pl.plot(tpoints2, ypoints2)
pl.xlabel("t")
pl.title("Theta Over Time")
pl.show()

