#!/usr/bin/env python
# coding: utf-8

# In[3]:


from bs4 import BeautifulSoup as bs


# In[12]:


import requests as rs


# In[76]:


link="https://www.flipkart.com/caya-warrior-26-army-green-dual-disc-triple-alloy-rims-front-shocker-26-t-fat-tyre-cycle/p/itm5252241845235?pid=CCEG68EWU72G7ZJ2&lid=LSTCCEG68EWU72G7ZJ2DAS3TO&marketplace=FLIPKART&q=cycle+adult&store=abc%2Fulv%2Fixt&srno=s_1_1&otracker=search&otracker1=search&fm=neo%2Fmerchandising&iid=2dbec056-9904-4266-a462-35f4ac6527b6.CCEG68EWU72G7ZJ2.SEARCH&ppt=sp&ppn=sp&ssid=ve5b8fj9v40000001668251840605&qH=6747b270b4a0ba11"


# In[77]:


page= rs.get(link)


# In[78]:


page.content


# In[79]:


soup=bs(page.content,"html.parser")
soup


# In[80]:


print(soup.prettify())


# In[81]:


title=soup.title
title


# In[82]:


print(title.string)


# In[89]:


price=soup.find_all("div",class_="_30jeq3 _16Jk6d")
print(price)


# In[94]:


product_price=[]
for i in range(0,len(price)):
    product_price.append(price[i].get_text())
product_price


# In[91]:


names=soup.find_all("p",class_="_2sc7ZR _2V5EHH")
names


# In[98]:


grahaknam=[]
for i in range(0,len(names)):
    grahaknam.append(names[i].get_text())
grahaknam


# In[99]:


comment=soup.find_all("div",class_="t-ZTKy")
comment


# In[103]:


cust_comment=[]
for i in range(0,len(comment)):
    cust_comment.append(comment[i].get_text())
cust_comment


# In[104]:


review=soup.find_all("p",class_="_2-N8zT")
print(review)


# In[106]:


review__=[]
for i in range(0,len(review)):
    review__.append(review[i].get_text())
review__


# In[107]:


ratings=soup.find_all("div",class_="_3LWZlK _1BLPMq")
print(ratings)


# In[108]:


ratings__=[]
for i in range(0,len(ratings)):
    ratings__.append(ratings[i].get_text())
ratings__


# In[113]:


quality=soup.find_all("text",class_="_2Ix0io")
print(quality)


# In[114]:


quality__=[]
for i in range(0,len(quality)):
    quality__.append(quality[i].get_text())
quality__


# In[115]:


stars=soup.find_all("div",class_="omG9iE")
print(stars)


# In[116]:


stars__=[]
for i in range(0,len(stars)):
    stars__.append(stars[i].get_text())
stars__


# In[117]:


hstr=soup.find_all("div",class_="_1uJVNT")
print(hstr)


# In[119]:


hstr__=[]
for i in range(0,len(hstr)):
    hstr__.append(hstr[i].get_text())
hstr__


# In[120]:


import pandas as pd


# In[126]:


Dataset=pd.DataFrame()

Dataset["Customer_Names"]=grahaknam
Dataset["Comments"]=cust_comment
Dataset["Ratings"]=ratings__
Dataset["Review"]=review__
Dataset["Stars"]=hstr__
Dataset["SStars"]=stars__
Dataset["Quailty of product"]=quality__



# In[ ]:




