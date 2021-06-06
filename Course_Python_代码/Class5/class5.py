# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 13:05:15 2020

@author: CharlieGoing
"""



import numpy as np

# In[]

m=np.ones([10,10])

m[1:9,1:9]=0



# In[]


a=np.random.rand(5,3)
b=np.random.randn(3,2)

c=np.dot(a,b)



# In[]

print(np.max(c))
print(np.min(c))
print(np.mean(c))
print(np.std(c))




# In[]

x=np.linspace(0,10,10000)

y=x**np.exp(x/3)


diff=np.abs(y-10)

print(np.argmin(diff))

print(x[np.argmin(diff)])




# In[]



# In[]




# In[]


import pandas as pd



# In[]


data=pd.DataFrame([1,"abc",3,4.5],columns=["number"],index=["a","b","c","d"])


# In[]



# In[]



# In[]



# In[]



# In[]

data1=pd.read_csv("data.csv")

data.to_csv("data_first.csv")


# In[]

print(data1.index)


# In[]

print(data1.columns)

# In[]
print(data1.head())


# In[]

print(data1["Age"])

# In[]

print(data1.loc[5,"Age"])


# In[]

print(data1.iloc[3:5,0:])

# In[]

pd.concat([data,data1])


# In[]


data2=pd.read_csv("data.csv")

# In[]

data3=pd.concat([data1,data2])

# In[]

data4=data3.append([data1,data])

# In[]


print(data1.isnull())


# In[]

data3=data1.dropna()

# In[]

data4=data1.fillna(0)

# In[]


# In[]

temp=data.drop(2)

# In[]


print(data1["Age"].argmin())

# In[]

print(data1.sort_values(by="Job"))

# In[]
print(data1["Age"].unique())

# In[]

temp=data3["Age"].values



# In[]
print(data3["Job"].describe())

# In[]



# In[]

import matplotlib.pyplot as plt


import numpy as np
# In[]

x=np.linspace(0,10,100)
y=np.sin(x)




# In[]

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("asdf123")
plt.grid(True)
plt.show()

# In[]


y1=np.sin(x)
y2=np.exp(x)


# In[]

plt.figure()

plt.subplot(1,2,1)
plt.plot(x,y1,"r")

plt.subplot(1,2,2)
plt.plot(x,y2,"g")






# In[]

plt.figure()


plt.plot(x,y1,"r.")


plt.plot(x,y2,"g--")

plt.ylim(-2,10)
plt.xlim(0,4)
# In[]


# In[]



# In[]
m=np.zeros([100,100,3])

m[10:20,:,:]=255

m[:,30:50,0:2]=255

plt.imshow(m)
# In[]



# In[]






# In[]



# In[]





# In[]



