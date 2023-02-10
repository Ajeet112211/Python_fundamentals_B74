#!/usr/bin/env python
# coding: utf-8

# In[9]:


firstname='ajeet'      # using the F string 
lastname='keshari'
fullname=f"{firstname} {lastname}"
print(fullname)


# In[10]:


print(fullname.title())


# In[11]:


firstname='ajeet'     # adding the message using F string and keeping the good format.
lastname='keshari'
fullname=f" keep up the good work {firstname} {lastname}"
print(fullname.title())


# In[13]:


# adding the white space

print("ajeet likes: pastachickenmaggichoco")


# In[24]:


print("ajeet likes:\n\tpasta\n\tchicken\n\tmaggi\n\tchoco".title())  # using the new line \n using the \t 4 space and .title for the proper letter.


# In[25]:


language='python'
print(language)


# In[30]:


language='   python'  #using lstrip strings  removing left whitespace
print(language.lstrip())


# In[31]:


language='python   '   #using rstrip strings   removing right whitespace 
print(language.rstrip())  


# In[32]:


language='   python   '  #using strip for  removing whitespace for both left and right
print(language.strip())


# In[ ]:




