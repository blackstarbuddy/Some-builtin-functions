#!/usr/bin/env python
# coding: utf-8

# ## RANGE FUNCTION

# In[2]:


def myrange(*a):
    a = list(a)
    if len(a) == 1:
        start = 0
        end = a[0]
        while start < end:
            yield start
            start = start + 1
    elif len(a) == 2:
        start = a[0]
        end = a[1]
        while start < end:
            yield start
            start = start + 1
    elif len(a) == 3:
        start = a[0]
        end = a[1]
        step = a[2]
        if step < 0:
            while start > end:
                yield start
                start += step
        else:
             while start < end:
                yield start
                start = start + step
    else: 
        raise ValueError("error")
list(myrange(10))


# ## SORT FUNCTION

# In[3]:


def mysort(a ,b =0):
    if b == 0:
        f = 0
        for i in range (len(a)):
            for j in range(i + 1, len(a)):
                if(a[i] > a[j]):
                    t = a[i]
                    a[i] = a[j]
                    a[j] = t
    elif b==1:
        f = 0
        for i in range (len(a)):
            for j in range(i + 1, len(a)):
                if a[i] < a[j] :
                    t = a[i]
                    a[i] = a[j]
                    a[j] = t
    return a
a = [1,4,2,6,2]
print(mysort(a,1))


# ##  FUNCTION FOR GENERATING OTP (INCLUDING STRING AND INT)

# In[4]:


def otp():
    import string
    d = string.digits + string.ascii_letters
    import random
    o = ""
    for i in range(6):
        o = o + random.choice(d)
    return o
otp()






