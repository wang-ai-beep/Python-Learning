# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 19:49:10 2020

@author: CharlieGoing
"""

import numpy as np

# In[]

a=np.array([1,2,3,4])
b=np.array([[1,2,3],[4,5,6]])
c=np.array([[1.2,"abc"],[3.4,4.5]])

d=np.array([[1],[2],[3],[4]])

# In[]

print(b.size)
print(b.shape)
print(b.ndim)


# In[]
print(np.arange(20))



# In[]

print(np.linspace(0,9,10))

# In[]

m=np.zeros([5,5])


# In[]

m=np.ones((5,5))



# In[]

m=np.random.rand()


# In[]

m=np.random.randn(3,3)




# In[]

a=np.array([1,2,3])

b=a.copy()

c=a*b

d=np.dot(a,b)

print(d)


# In[]

ax=np.reshape(a,(3,1))
bx=np.reshape(b,(1,3))

# In[]

print(np.dot(ax,bx))


# In[]
m=np.zeros([4,4])

n=np.reshape(m,(3,8))

# In[]


a=np.array([[1,2,3]])

b=np.array([[4,5,6]])


c=np.vstack([c,b])

d=np.hstack([c,b])

# In[]

e=np.concatenate((a,b),axis=1)

# In[]
print(n.T)



# In[]


a=np.array([0,1,2,3,4,5,6,7,8,9])

# In[]

print(a[1:])


# In[]

b=a.reshape(5,2)


# In[]
print(b[3][1])

# In[]
print(b[3,:])

# In[]
print(b[:,0])

# In[]


# In[]

print(np.log(2))

print(np.exp(np.log(2)))
# In[]
print(np.exp(a))



# In[]


print(np.max(a))

print(np.min(a))

print(np.mean(a))

print(np.median(a))

print(np.std(a))


# In[]

print(np.max(b,1))
print(np.min(b,1))
print(np.mean(b,0))
print(np.median(b,0))
print(np.std(b,1))




# In[]



print(np.tan(a))
print(np.abs(-10))



# In[]


print(np.argmax(a))

print(np.argmin(b))
# In[]
# In[]

# In[]

# In[]
# In[]

# In[]
# In[]
# In[]

# In[]

# In[]
# In[]

# In[]
# In[]