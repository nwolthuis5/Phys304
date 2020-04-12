
# coding: utf-8

# In[1]:


#Huge collaboration points to Katharine Bancroft
print("problem 6.16")
#defining constants
accuracy = 10
G = 6.674 * 10 ** (-11) #m**3 kg **(-1) * s ** (-2)
M = 5.974 * 10 ** 24 #kg
m = 7.348 * 10 ** 22 #kg
R = 3.844 * 10 ** 8 #m
Rearth = 6.371 * 10 **6
Rmoon = 1.7371 * 10 **6
omega = 2.662 * 10 ** (-6) #s ** (-1)


# In[2]:


#setting up the function
def f(r):    
    val = (G*M)/(r**2) - (G*m)/((R-r)**2) - (r * omega ** 2)
    return val


# In[9]:


r1 = R - Rearth - Rmoon
r2 = Rearth
    
delta = 100
while abs(delta)>accuracy:
    #derivative of f
    delta = f(r2)*(r2-r1)/(f(r2)-f(r1))
    #moving values along
    r1 = r2
    r2 -= delta
print(" the lagrange point is",r2 * 10**(-8),"* 10^(8) meters")

