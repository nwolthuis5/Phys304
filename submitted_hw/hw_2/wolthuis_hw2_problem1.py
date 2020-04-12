
# coding: utf-8

# In[3]:


#plotting experimental data, problem 1
print("problem 3.1")
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

#pulling in the sunspot data from the directory
ss_data = np.loadtxt("wolthuis_hw2_sunspots.txt",float)


# In[4]:

print("part a")
#assigning variables
x1 = ss_data[:,0]
y1 = ss_data[:,1]

#making a running average
r = 5

x2 = []
y2 = []
#running over the range where the average doesn't run over boundaries
for i in range(5,int(x1[-1]-5)):
    
    #making a list that will be used in the lambda function below
    ysum = []
    
    #looping over to build the afforementioned list
    for m in range(-r,r):
        yr = y1[i+m]
        ysum.append(yr)
        
    #making an added sum using the ysum list built before
    yadd = functools.reduce(lambda k,l: k+l, ysum)
    
    #making the added sum into an actual average by dividing it by (2r+1)
    yavg = yadd/(2*r + 1)
    
    #appending stuff
    y2.append(yavg)
    x2.append(x1[i])


# definitions for the axes
left, width = 0.1, 0.65
bottom, height = 0.1, 0.65
spacing = 0.005

#setting limits
#plt.xlim(0,1000)

#plotting the function
plt.plot(x1,y1 , label = "Sunspots", color = 'k')
#plt.plot(x2,y2, label = "Running Average", color = 'orange')

#Formatting, Labels, & Legends
plt.xlabel('Months Since Jan. 1749')
plt.ylabel('Sunspots')
plt.title('Sunspots as a Function of Time')
plt.legend()

#Line of best fit
#plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))

plt.show()


# In[5]:


print("part b")

#assigning variables
x1 = ss_data[:,0]
y1 = ss_data[:,1]

#making a running average
r = 5

x2 = []
y2 = []
#running over the range where the average doesn't run over boundaries
for i in range(5,int(x1[-1]-5)):
    
    #making a list that will be used in the lambda function below
    ysum = []
    
    #looping over to build the afforementioned list
    for m in range(-r,r):
        yr = y1[i+m]
        ysum.append(yr)
        
    #making an added sum using the ysum list built before
    yadd = functools.reduce(lambda k,l: k+l, ysum)
    
    #making the added sum into an actual average by dividing it by (2r+1)
    yavg = yadd/(2*r + 1)
    
    #appending stuff
    y2.append(yavg)
    x2.append(x1[i])


# definitions for the axes
left, width = 0.1, 0.65
bottom, height = 0.1, 0.65
spacing = 0.005

#setting limits
plt.xlim(0,1000)

#plotting the function
plt.plot(x1,y1 , label = "Sunspots", color = 'k')
#plt.plot(x2,y2, label = "Running Average", color = 'orange')

#Formatting, Labels, & Legends
plt.xlabel('Months Since Jan. 1749')
plt.ylabel('Sunspots')
plt.title('Sunspots as a Function of Time')
plt.legend()

#Line of best fit
#plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))

plt.show()


# In[6]:


print("part c")

#assigning variables
x1 = ss_data[:,0]
y1 = ss_data[:,1]

#making a running average
r = 5

x2 = []
y2 = []
#running over the range where the average doesn't run over boundaries
for i in range(1+r,int(x1[-1]-r)):
    
    #making a list that will be used in the lambda function below
    ysum = []
    
    #looping over to build the afforementioned list
    for m in range(-r,r+1):
        yr = y1[i+m]
        ysum.append(yr)
        
    #making an added sum using the ysum list built before
    yadd = functools.reduce(lambda k,l: k+l, ysum)
    
    #making the added sum into an actual average by dividing it by (2r+1)
    yavg = yadd/(2*r + 1)
    
    #appending stuff
    y2.append(yavg)
    x2.append(x1[i])


# definitions for the axes
left, width = 0.1, 0.65
bottom, height = 0.1, 0.65
spacing = 0.005

#setting limits
plt.xlim(0,1000)

#plotting the function
plt.plot(x1,y1 , label = "Sunspots", color = 'k')
plt.plot(x2,y2, label = "Running Average", color = 'r')

#Formatting, Labels, & Legends
plt.xlabel('Months Since Jan. 1749')
plt.ylabel('Sunspots')
plt.title('Sunspots as a Function of Time')
plt.legend()

#Line of best fit
#plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))

plt.show()

