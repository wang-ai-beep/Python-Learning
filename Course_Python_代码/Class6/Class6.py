# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 10:42:46 2020

@author: CharlieGoing
"""


import requests


    
# In[]:

data=requests.get("https://www.csdn.net")
    
        
# In[]:

# data.encoding="gb2312"
data.encoding="utf-8"
print(data.text)   
    
        
# In[]:
data=requests.get("http://www.csdn.com")
    
     
print(data.status_code ) 
        
# In[]:
    
url="https://so.csdn.net/so/search/s.do?q=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&t=&u= "

data=requests.get(url=url)
    
     



# In[]:
    
header={"user-agent":"Mozilla/5.0"}


prox={"http":"http://1.1.10.102:88"}



data=requests.get(url=url,headers=header,timeout=2,proxies=prox)

print(data.status_code)


    
# In[]:
    
    
        
# In[]:
    
sample_text='''

<html>
    <div>
        <ul>
            <li class="123"><a href="abc.html">hello</a></li>
            <li class="123"><a>world</a></li>
            <li class="abc"><a href="123.html">asdf</a></li>

        </ul>
    </div>
</html>'''   
    
        
# In[]:
    
from bs4 import BeautifulSoup 
        
# In[]:
    
soup=BeautifulSoup(sample_text,"lxml")   
        
temp=soup.find(name="ul")
print(temp.text)
# In[]:
    
temp=soup.find_all(name="li")  
for tmp in temp:
    print(tmp.text)
# In[]:
temp=soup.find_all(name="li",attrs={"class":"123"})  
for tmp in temp:
    print(tmp.text)    
        
# In[]:
    
temp=soup.find(name="li",attrs={"class":"abc"})  
print(temp.text)  
    
        
# In[]:
    
url="https://so.csdn.net/so/search/s.do?q=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&t=&u=" 
 
header={"user-agent":"Mozilla/5.0"}

data=requests.get(url=url,headers=header)

html=data.text
       
# In[]:

soup=BeautifulSoup(html,"lxml")

lis=soup.find_all(name="dl",attrs={"class":"search-list J_search"})

for li in lis:
    temp=li.find(name="div",attrs={"class":"limit_width"})
    temp=temp.find(name="a")
    print(temp.text)
    # print(lis)
    
        
# In[]:
    
    
    
# In[]:
    
    
        
# In[]:
    
    
    
        
# In[]:
    
    
        
# In[]:
    
    
        
# In[]:
    
    
    
# In[]:
    
    
        
# In[]:
    
    
    
        
# In[]:
    
    
        
# In[]:
    
    
        
# In[]:
    
    
    
# In[]:
    
    
        
# In[]:
    
    
    
        
# In[]:
    
    
        
# In[]:
    
    
        
# In[]: