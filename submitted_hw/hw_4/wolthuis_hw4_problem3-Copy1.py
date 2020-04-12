
# coding: utf-8

# In[9]:


import numpy as np
import pylab as pl
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import dblquad


#trying to make it the latex font stuff
from matplotlib import rc
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
plt.rc('font',**{'family':'serif','serif':['Times New Roman']})
plt.rc('text', usetex=True)


print("problem 5.21")
eps0 = 8.854 * 10 ** (-12) #in units of epsilon naught


# In[11]:


#thanks to Katharine Bacroft for collaborating and showing me how to mesh
seperation = 0.1
side = 1
N = 100
h = side / N
k_vac = 1/(4*np.pi*eps0)
q = 1 #in units of charge

#defining a function for potential
def V(r):
    val = k_vac * q/r
    return val

#making a meshgrid because meshgrid superiority apparently
x = np.linspace(-0.5, 0.5, 100)
y = np.linspace(-0.5, 0.5, 100)

X, Y = np.meshgrid(x,y)

#defining the radii for the positive and negative charges
R_pos = ((X - 0.05)**2 + (Y)**2) ** (1/2)
R_neg = ((X + 0.05)**2 + (Y)**2) ** (1/2)

#making the potentials
v_pos = V(R_pos)
v_neg = -V(R_neg)
v_tot = v_pos + v_neg

pl.imshow(v_tot, origin ="lower", extent = [-.5,.5,-.5,.5], vmin=-10**(10), vmax = 10**10)
cbar = plt.colorbar()
cbar.set_label("Intensity")
pl.title("Potential at distance from charges")
pl.hot()
pl.show()


# In[12]:


#getting the derivative using numpy's gradient function
dx, dy = np.gradient(v_tot)

#setting them equal to their negatives, because that is how E fields work
dx = -dx
dy = -dy

plt.streamplot(X,Y,dy,dx,density = 2)
pl.title("E Field at Distance from Charges")
plt.show()


# In[13]:


def sig(y,x):
    L = .1 #m
    q0 = 100 #(C/m**2)
    val = q0 * np.sin((2*np.pi*x)/L) * np.sin((2*np.pi*y)/L)
    return val


# In[14]:


L = .1 #m
q0 = 100 #(C/m**2)

#defining the integrand
def sig(y,x):
    val = q0 * np.sin((2*np.pi*x)/L) * np.sin((2*np.pi*y)/L)
    return val
    
#defining limits of y integration
def ylower(x):
    return -0.05
def yupper(x):
    return 0.05

nt, error = dblquad(sig,-0.05,-0.05,ylower,yupper)
    
#retrieving the value for the function output    
val = nt
return val


# In[15]:


#defining the integrand
def sig(x,y):
    val = q0 * np.sin((2*np.pi*x)/L) * np.sin((2*np.pi*y)/L)
    return val

#making a meshgrid because of meshgrid superiority apparently
x = np.linspace(-0.05, 0.05, 100)
y = np.linspace(-0.05, 0.05, 100)

X, Y = np.meshgrid(x,y)

#making the potentials
pl.imshow(sig(X,Y), origin ="lower", extent = [-0.05,.05,-0.05,0.05])
cbar = plt.colorbar()
cbar.set_label("Intensity")
pl.title("Charge Per Area")
pl.hot()
pl.show()


# In[21]:


#SUPER HUGE COLLABORATION POINTS FOR KATHARINE BANCROFT AND NATHAN M. PLEASSSSEEEE

#defining what we're going to integrate
side = 1 #meter
def Vc(x,y,x1,y1):
    if x ==0 and y ==0:
        return 0
    else:
        val = k_vac * sig(x,y)/((x-x1)**2 + (y-y1)**2)**(1/2)
        return val

#setting up the sheet thing
def V_area(x1,y1):
    nt, err = dblquad(Vc, -0.05, 0.05, lambda x: -0.05, lambda x: 0.05, args=[x1,y1], epsrel = 10**5)
    return nt

#setting up potential plots through for loops and blank lists and stuff
Potential = np.zeros((100,100))

for x1 in range(0,100):
    for y1 in range(0,100):
        v = V_area(-0.5 + x1/100, -0.5 + y1/100)
        Potential[x1,y1] = v
        
#defining vectors for the e field
y_sq, x_sq = np.gradient(Potential)
plt.xlim(-.05,.05)
plt.ylim(-.05,.05)
plt.streamplot(X,Y, -x_sq, -y_sq, density = 2)
plt.title("E Field Around a Plane of Oscillating Charge Density")
plt.show()

