print("problem 3.6")

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

#making initial lists
xcs = []
rcs = []

#setting initial constants
i = 1
r = 0
rmax = 4

#making a for loop for the r value
while r < rmax:
    #initializing the list for x
    x = []

    #making a loop for the iterative chaos function
    for i in range(0,2002):
        #if True:
        if i == 0:
            x.append(.5)
        else:
            #making the iterative function
            xnext = (r * x[i-1]) * (1 - x[i-1])
            x.append(xnext)

            #appending values
            if i > 1000:
                rcs.append(r)
                xcs.append(xnext)

    #updating the value for r
    #print(r)
    r = r + .01

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
ax_scatter.scatter(rcs, xcs, alpha = .01, color = 'k', s = 4)

#limits
ax_scatter.set_xlim(1, rmax)

#Formatting, Labels, & Legends
plt.xlabel('r value')
plt.ylabel('x value')
plt.title('Chaos Function')

plt.show()