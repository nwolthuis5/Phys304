
# coding: utf-8

# In[2]:


#plotting experimental data, problem 1
print("problem 3.2")

# importing all the goodies that make this assignment possible
import numpy as np
import matplotlib.pyplot as plt
import functools

#trying to make it the latex font stuff
from matplotlib import rc
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
plt.rc('font',**{'family':'serif','serif':['Times New Roman']})
plt.rc('text', usetex=True)

# In[10]:


print("part a)")
#making lists for the coordinates of stuff
xa = []
ya = []

#setting up a while loop to calculate the values of x and y in terms of theta
theta = 0
while theta < (2*np.pi):
    if True:    
        #setting up the equations to calculate the values
        x = 2*np.cos(theta) + np.cos(2 * theta)
        y = 2*np.sin(theta) - np.sin(2 * theta)
        #print(x)
        #print(y)
        #appending said values to the lists
        xa.append(x)
        ya.append(y)
        
        #updating value for theta
        theta = theta + .01
    else:
        break

#MAKING THE PLOT        
# definitions for the axes
left, width = 0.1, 0.65
bottom, height = 0.1, 0.65
spacing = 0.001


rect_scatter = [left, bottom, width, height]

# start with a rectangular Figure
plt.figure(figsize=(8, 8))

ax_scatter = plt.axes(rect_scatter)
ax_scatter.tick_params(direction='in', top=True, right=True)

# the scatter plot:
ax_scatter.scatter(xa, ya, s = 4)

#Formatting, Labels, & Legends
plt.title('Deltoid Curve')

plt.show()


# In[9]:


print("part b)")
#making lists for the coordinates of stuff
xb = []
yb = []

#setting up a while loop to calculate the values of x and y in terms of theta
theta = 0
while theta < (10*np.pi):
    if True:    
        #setting up the equations to calculate the values
        r = theta ** 2
        x = r*np.cos(theta)
        y = r*np.sin(theta)
        #print(x)
        #print(y)
        #appending said values to the lists
        xb.append(x)
        yb.append(y)
        
        #updating value for theta
        theta = theta + .001
    else:
        break

#MAKING THE PLOT        
# definitions for the axes
left, width = 0.1, 0.65
bottom, height = 0.1, 0.65
spacing = 0.01


rect_scatter = [left, bottom, width, height]

# start with a rectangular Figure
plt.figure(figsize=(8, 8))

ax_scatter = plt.axes(rect_scatter)
ax_scatter.tick_params(direction='in', top=True, right=True)

# the scatter plot:
ax_scatter.scatter(xb, yb, s = 1)

#Formatting, Labels, & Legends
plt.title('Spiral')

plt.show()


# In[7]:


print("part c)")
#making lists for the coordinates of stuff
xc = []
yc = []

#setting up a while loop to calculate the values of x and y in terms of theta
theta = 0
while theta < (24*np.pi):
    if True:    
        #setting up the equations to calculate the values
        r = (np.exp(np.cos(theta))) - (2 * np.cos(4 * theta)) + (np.sin(theta/12))**5
        x = r*np.cos(theta)
        y = r*np.sin(theta)
        #print(x)
        #print(y)
        #appending said values to the lists
        xc.append(x)
        yc.append(y)
        
        #updating value for theta
        theta = theta + .001
    else:
        break

#MAKING THE PLOT        
# definitions for the axes
left, width = 0.1, 0.65
bottom, height = 0.1, 0.65
spacing = 0.01


rect_scatter = [left, bottom, width, height]

# start with a rectangular Figure
plt.figure(figsize=(8, 8))

ax_scatter = plt.axes(rect_scatter)
ax_scatter.tick_params(direction='in', top=True, right=True)

# the scatter plot:
ax_scatter.scatter(xc, yc, s = 1)

#Formatting, Labels, & Legends
plt.title('Fey Function')

plt.show()

