#!/usr/bin/env python
# coding: utf-8

# In[1]:


student={'ajeet','divya','shubham','vipul'}  #
print(student)


# In[2]:


print(student.title()) # using title string method.


# In[14]:


student=['ajeet','divya','shubham','vipul']   #creating the list ( brackets playes the important role)
type(student)  


# In[17]:


print(student[0].title())  #printing the indexing


# In[18]:


print(student[1])


# In[19]:


student.append('aru') # using appent method to add the user in the list, append always add in last


# In[20]:


print(student)


# In[22]:


student.insert(2, 'kayu')  #using insert method adding user in the second index


# In[32]:


print(student)


# In[24]:


student[0]='Hritik'  #modify the index in the list object


# In[29]:


print(student.title())


# In[33]:


del student[5]  # delete the index  from the list


# In[34]:


print(student)


# In[35]:


student.pop(1)  #remove the temporary index from the list


# In[36]:


print(student)


# In[43]:


print(student[-1])  # printing the index in reverse order


# In[45]:


print(student[::-1])   #printing the list in reverse indexingz 


# In[ ]:




