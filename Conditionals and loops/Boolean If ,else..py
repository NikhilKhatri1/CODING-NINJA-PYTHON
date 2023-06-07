#!/usr/bin/env python
# coding: utf-8

# ## Boolean Type

# In[3]:


a = True
b = False

c = "Ninjas"
type(b)


# ## Relational Operators (<, >, <=, >=, ==, !=)

# In[2]:


a = 10
b =20
print(a > b)   # a is greater than b
print(a < b)   # a is less than b
print(a >= b)  # a is greter than or equal to b 
print(a <= b)  # a is less than or equal to b 
print(a == b)  # a is equal to b
print(a != b)  # a is not equal to b


# ## Logical Operators (and, or, not)

# In[4]:


c1 = a > 10
c2 = b > 10
r1 = c1 and c2
r2 = c1 or c2
r3 = not(c1)
print(r1)
print(r2)
print(r3)


# ## If Else

# In[5]:


a = True or False
if a:
    print("If Block")
    print("Woohoo!")
else:
    print("Else Block")


# ## Odd or Even

# In[6]:


n = int(input())
if( n%2 == 0):
    print("Even Number")
else:
    print("Odd Number")


# In[ ]:


n = int(input())
if(n & 1):
    print("Odd")
else:
    print("Even")


# ## check the number is small,medium,large, too large

# In[7]:


n = 15
#Check If the number is between 1 to 10
if n>=1 and n<=10:
    print("too low")

#Check If the number is between 11 to 20
elif n>=10 and n<=20:
    print("medium")

#Check If the number is between 21 to 30
elif n>=20 and n<=30:
    print("large")
#Check if the number is greater than 30 
else:
    print("too large")


# In[8]:


x = 5
if x < 6:
    print("Hello")
if x == 5:
    print("Hi")
else:
    print("Hey")


# In[ ]:




