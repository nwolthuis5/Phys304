
# coding: utf-8

# In[1]:


import numpy as np
print("for problem 2.10, ")


# In[10]:


#Semi-Empiracal Mass Formula, Problem 2.10 a
print("problem 2.10 a)")
A = int(input("please provide a positive integer value for A: "))
Z = int(input("please provide a positive integer value for Z: "))

#set up inital values
a1 = 15.8
a2 = 18.3
a3 = 0.714
a4 = 23.2
#set up value for a5 as a function of A and Z
if A%2 == 0:
    a5 = 12.0
else:
    a5 = 0
if Z%2 == 0:
    a5 = a5
else:
    a5 = a5 * (-1)
    
#Set up function for B
B = (a1*A) - (a2*(A**(2/3))) - a3*(Z**2)/(A**(1/3)) - (a4*((A-2*Z)**2)/A) + a5/(A**(1/2))
#Release the Krak- ... B value
print("the total binding energy is",B, "MeV")


# In[7]:


#Semi-Empiracal Mass Formula, Problem 2.10 b
print("problem 2.10 b)")
A = int(input("please provide a positive integer value for A: "))
Z = int(input("please provide a positive integer value for Z: "))

#set up inital values
a1 = 15.8
a2 = 18.3
a3 = 0.714
a4 = 23.2
    
#set up value for a5 as a function of A and Z
if A%2 == 0:
    a5 = 12.0
else:
    a5 = 0
if Z%2 == 0:
    a5 = a5
else:
    a5 = a5 * (-1)
    
#Set up function for B
B = (a1*A) - (a2*(A**(2/3))) - a3*(Z**2)/(A**(1/3)) - (a4*((A-2*Z)**2)/A) + a5/(A**(1/2))
    
#show binding energy per nucleon
print("the binding energy per nucleon is", B/A, "MeV")


# In[8]:


#Semi-Empiracal Mass Formula, Problem 2.10 c
print("problem 2.10 c)")
Z = int(input("please provide a positive integer value for Z: "))

#set up values for constants
a1 = 15.8
a2 = 18.3
a3 = 0.714
a4 = 23.2
    
A_list = []
b_list = []
#set up a loop for the value of A
for A in range(Z, 3*Z):
        
    #set up value for a5 as a function of A and Z in the loop
    if A%2 == 0:
        a5 = 12.0
    else:
        a5 = 0
    if Z%2 == 0:
        a5 = a5
    else:
        a5 = a5 * (-1)
        
    #Set up function for B in the loop
    B = (a1*A) - (a2*(A**(2/3))) - a3*(Z**2)/(A**(1/3)) - (a4*((A-2*Z)**2)/A) + a5/(A**(1/2))
        
    #Making lists for the A and associated B values
    A_list.append(A)
    b_list.append(B/A)
    
#determing the index for the maximum B value for a given Z
b_max_index = b_list.index(max(b_list))
    
#Pick out and print the A value with the most stable B value
print("The most stable value for A is", A_list[b_max_index], 'with a binding energy per nucleon of', max(b_list), "MeV")


# In[9]:


print("problem 2.10 d)")
Zmax = int(input("please provide a maximum positive integer value for Z to loop through: "))

#making the lists for the b and Z value
high_b = []
Z_list = []
    
#starting the Z loop
for Z in range(1,Zmax + 1):
    #set up values for constants
    a1 = 15.8
    a2 = 18.3
    a3 = 0.714
    a4 = 23.2
    
    #make lists for values
    A_list = []
    b_list = []
    
    #set up a loop for the value of A
    for A in range(Z, 3*Z):
        
        #set up value for a5 as a function of A and Z in the loop
        if A%2 == 0:
            a5 = 12.0
        else:
            a5 = 0
        if Z%2 == 0:
            a5 = a5
        else:
            a5 = a5 * (-1)
        
        #Set up function for B in the loop
        B = (a1*A) - (a2*(A**(2/3))) - a3*(Z**2)/(A**(1/3)) - (a4*((A-2*Z)**2)/A) + a5/(A**(1/2))
        
        #Making list for B values
        b_list.append(B/A)
        A_list.append(A)
    
    #Pick out the high B values-
    high_b.append((max(b_list)))
        
    #Making list for Z values
    Z_list.append(Z)
    
    #Giving the stable A values for each value of Z
    print("for Z equals", Z_list[-1], "the most stable value for A is", A_list[b_list.index(max(b_list))])

#Determine Index number for the maximum binding energy for the Z value
max_index = high_b.index(max(high_b))

#adding a space between the A values for Z's and the most stable Z value for ease of reading
print()

#Delivering the final answer, after much blood sweat and tears, not actually because gross
print("the value of Z with the most stable binding energy is", Z_list[max_index])

