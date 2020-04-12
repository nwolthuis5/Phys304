
# coding: utf-8

# In[10]:


#Catalan Numbers, Problem 2.13 a
n = int(input("pick an integer to find the n value for C_n: "))
def Cn(n):
    #providing the base value
    if n == 0:
        return 1
    #providing the compounding value thingamajig
    else:
        return int(((4*n -2)/(n+1)) * Cn(n-1))

#Cn(100)
print("Here's the float form:   ",float((Cn(n))))
print("Here's the integer form: ",Cn(n))

