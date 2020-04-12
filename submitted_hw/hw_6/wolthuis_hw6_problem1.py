
# coding: utf-8

# In[18]:


print('problem 6.13')
import numpy as np
#defining the constants we want to use
kB = 1.380649 * 10 ** (-23)
c  = 2.997924 * 10 ** (8.0)
h  = 6.626070 * 10 ** (-34)

#defining the nonlinear function we will solve for
def f(x):
    val = 5 * np.exp(-x) + x - 5
    return val


# In[7]:


#defining the accuracy
accuracy = 10 ** (-6)
r1 = 2.
r2 = 5.

#setting up the while loop
delta = np.abs(r1 - r2)
while abs(delta)>accuracy:
    rp = (r1 + r2)/2
    if f(rp) > 0:
        r2 = rp
        delta = np.abs(r1 - r2)
    else:
        r1 = rp
        delta = np.abs(r1 - r2)
root1 = .5*(r1 + r2)
print('the binary search method gives x = ', root1, 'as a root of the function')


# In[8]:


r2 = 10
    
delta = 1
while abs(delta)>accuracy:
    #derivative of f
    delta = f(r2)*(-5 * np.exp(-r2) + 1)
    #moving values along
    r2 -= delta
root2 = r2
print('the Newton method gives x =',root2, 'as a root of the function')


# In[17]:


print("the difference between the binary and Newton search methods is",root1-root2, ", which is lower than our epsilon value")


# In[21]:


x =4.965114
b = (h * c) / (kB * x)
print("the calculated value for Wien's Displacement Constant, b, is:", b * 10**(3)," x 10^(-3)")

