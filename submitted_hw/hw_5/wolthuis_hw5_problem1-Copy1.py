
# coding: utf-8

# In[1]:


print("Problem 6.4")
#importing goodies
from numpy import array,empty
from numpy.linalg import inv,solve
from numpy import copy,dot


# In[4]:


#building an array for the resistors
A = array([ [ 4,-1,-1,-1],
            [-1, 3, 0,-1],
            [-1, 0, 3,-1],
            [-1,-1,-1, 4]], float)

#building an array for the output of Ax
v = array([ 5, 0, 5, 0],float)
#N = len(v)

#B=copy(A)
#vold=copy(v)

## Gaussian elimination
#for m in range(N):

#    # Divide by the diagonal element
#    div = A[m,m]
#    A[m,:] /= div
#    v[m] /= div

#    # Now subtract from the lower rows
#    for i in range(m+1,N):
#        mult = A[i,m]
#        A[i,:] -= mult*A[m,:]
#        v[i] -= mult*v[m]

# Back Substitution Stuff
#x = empty(N,float)
#for m in range(N-1,-1,-1):
#    x[m] = v[m]
#    for i in range(m+1,N):
#        x[m] -= A[m,i]*x[i]
#
#print(x)


# In[6]:


Answer = solve(A,v)
print("V1 was determined to be",Answer[0], "Volts")
print("V2 was determined to be",Answer[1], "Volts")
print("V3 was determined to be",Answer[2], "Volts")
print("V4 was determined to be",Answer[3], "Volts")

