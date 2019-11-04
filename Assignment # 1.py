#!/usr/bin/env python
# coding: utf-8

# In[1]:


line1 = ("Twinkle, twinkle, little star,")
line2 = ("How I wonder what you are!")
line3 = ("Up above the world so high,")
line4 = ("Like a diamond in the sky.")
line5 = ("Twinkle, twinkle, little star,")
line6 = ("How I wonder what you are")

print (
       line1 + '\n \t' + 
       line2 + '\n \t \t' + 
       line3 + '\n \t \t'+
       line4 + '\n'+
       line5 + "\n \t"+
       line6 + "\n" 
      )


# In[2]:


from platform import python_version
print("Python Version : " + python_version())


# In[3]:


import datetime
now = datetime.datetime.now()
print ("Current date and time :" + '\n', now)


# In[4]:


from math import pi
radius = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(radius) + " is: " + str(pi * radius**2))


# In[5]:


f_name = input("Enter First Name : ")
l_name = input("Enter Last Name : ")
print ("Hello  " + l_name + " " + f_name)


# In[6]:


num1 = int (input ("Enter First No: "))
num2 = int (input ("Enter Second No: "))
result = (num1 + num2)
print ('Result: ', result)


# In[ ]:




