
# coding: utf-8

# In[1]:


#importing goodies
import functools
import numpy as np
import math
import matplotlib.pyplot as plt
import pylab as pl

#trying to make it the latex font stuff
from matplotlib import rc
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
plt.rc('font',**{'family':'serif','serif':['Times New Roman']})
plt.rc('text', usetex=True)

#letting grader know what problem we're doing
print("problem 5.4")

#using the integral made from the previous problem
print("the integral is given as the function nw_simp_int(f,a,b,N) if you wish to call it in the future")
def nw_simp_int(f,a,b,N):
    
    #defining the number of bins for future looping stuff
    h = (b-a)/N
    
    #making lists for even and odd  values
    evnval = []
    oddval = []
    
    
    #beginning the loop with a for - if statement
    for i in range(a+1,N):
        #setting up an if statement to get seperate odd and even summations
        if (i%2) == 0:
            evn = float(f(a+(i*h)))
            evnval.append(evn)
        else:
            odd = float(f(a+(i*h)))
            oddval.append(odd)
    
    #using lambda functions to get the summation of the even and the odd values
    sumodd = functools.reduce(lambda k,l: k+l, oddval)
    sumevn = functools.reduce(lambda k,l: k+l, evnval)
    
    #getting the final integral values
    integral = (h/3)*(f(a) + f(b) + (2*sumodd) + (4*sumevn))
    return integral


# In[2]:


#starting to make a Bessel function
def J(m,x):
    N = 1000   
    #function to be integrated later on in the function
    def f(theta):
        val = np.cos(m*theta - (x * np.sin(theta)))
        return val
    
    #making an integrating function
    val = nw_simp_int(f,0,np.pi,N) / np.pi
    return val


# In[3]:


#initializing lists and stuff
J0 = []
x0 = []
J1 = []
x1 = []
J2 = []
x2 = []

#making a loop for the values of J0 and x0
for i in np.linspace(0,20,):
    val = J(0,i)
    J0.append(val)
    x0.append(i)

#making a loop for the values of J1 and x1
for i in np.linspace(0,20):
    val = J(1,i)
    J1.append(val)
    x1.append(i)

#making a loop for the values of J2 and x2
for i in np.linspace(0,20):
    val = J(2,i)
    J2.append(val)
    x2.append(i)

#MAKING MY PLOT
    
# definitions for the axes
left, width = 0.1, 0.65
bottom, height = 0.1, 0.65
spacing = 0.005

#plotting the function
plt.plot(x0,J0 , label = "J0", color = 'k')
plt.plot(x1,J1 , label = "J1", color = 'r')
plt.plot(x2,J2 , label = "J2", color = 'c')

#Formatting, Labels, & Legends
plt.xlabel('x value')
plt.ylabel('J value')
plt.title('J vs X')
plt.legend()

#Line of best fit
#plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))

plt.show()


# In[4]:


#set up constants and whatnot
lmda = 5 * 10 ** (-7)
k = (2 * np.pi) / lmda
N = 25
width = 2*10 ** (-6)
h = 10 ** (-6) / (2*N)
#I0 = J(1,0)**2

#making the offset so that we see more than a quarter of the plot
x0 = width/2
y0 = width/2

#making an array to put things in later
Ir = np.empty([4*N+1,4*N+1],float)

#calculating values for the array
for i in range(4*N+1):
    y = h * i
    
    for j in range(4*N+1):
        x = h * j
        
        #radial distance from the previously defined offset
        r = (((x-x0)**2) + ((y-y0)**2))**(1/2)
        
        #putting stuff into that array we made
        Ir[i,j] = (J(1,(k*r))/(k*r)) ** 2
#making the plot, ~yay~
plt.xlim(0,4*N)
plt.ylim(0,4*N)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Intensity of Circular Diffraction Through Point')
pl.imshow(Ir, origin = 'lower',vmax=.01)
cbar = plt.colorbar()
cbar.set_label("Intensity")
pl.hot()
pl.show()


# In[5]:


#doing stuff to check Bessel against recursion Bessel
def Jn(n,x):
    if n == 0:
        return J(0,x)     
    elif n == 1:
        return J(1,x) 
    else:
        return ((2*(n-1))/x)*(Jn(n-1,x)) - Jn(n-2,x)


# In[6]:


#initializing lists and stuff
J2 = []
x2 = []
J3 = []
x3 = []
J4 = []
x4 = []

#making a loop for the values of J2 and x2
for i in np.linspace(1,20,100):
    val = np.abs((J(2,i) - Jn(2,i))/Jn(2,i))
    J2.append(val)
    x2.append(i)

#making a loop for the values of J3 and x3
for i in np.linspace(1,20,100):
    val = np.abs((J(3,i) - Jn(3,i))/Jn(3,i))
    J3.append(val)
    x3.append(i)
    
#making a loop for the values of J4 and x4
for i in np.linspace(1,20,100):
    val = np.abs((J(4,i) - Jn(4,i))/Jn(4,i))
    J4.append(val)
    x4.append(i)
#MAKING MY PLOT
    
# definitions for the axes
left, width = 0.1, 0.65
bottom, height = 0.1, 0.65
spacing = 0.005

#plotting the function
plt.plot(x2,J2 , label = "J2 Error Fraction", color = 'k')
plt.plot(x3,J3 , label = "J3 Error Fraction", color = 'r')
plt.plot(x4,J4 , label = "J4 Error Fraction", color = 'c')

#Formatting, Labels, & Legends
plt.xlabel('x value')
plt.ylabel('J value')
plt.title('Error Fraction of J vs X')
plt.legend()

#Line of best fit
#plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))

plt.show()

