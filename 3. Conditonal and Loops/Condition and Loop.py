#!/usr/bin/env python
# coding: utf-8

# ### Print All the prime Number.

# In[8]:


n = int(input())    # Taking User Input
k = 2              # Looping variable starting from 2
while k < = n:     # Loop will check all numbers till n
    
    d = 2               # The inner loop also checks all numbers starting from 2
    isPrime = False
    while d < k:         #Inside loop k value will repeat until d = k to check the k is prime or not.
        
        if (k % d == 0 ):
            isPrime = True
        d = d + 1
    
    if ( not (isPrime)):
        print(k)
    k = k + 1


# ### Check the number is prime or not.

# In[12]:


n = int(input())
isprime = True

if n > 1:
    k = 2

    while k < n:
    
        if n % k == 0:
            isprime = False
            break
        k = k+1
if (n <= 1):
    print("not Prime")
elif (isprime):
    print("Prime")
else:
    print("not Prime")


# In[ ]:




