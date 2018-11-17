#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
x = np.linspace(-4, 4, 200)
y=(1-np.e**x)/(1+np.e**x)
plt.plot(x, y)


# In[11]:


p1 = x < -np.pi/2
p2 = np.abs(x) < np.pi/2
p3 = x > np.pi/2
y=np.tan(x)
plt.plot(x[p1], y[p1])
plt.plot(x[p2], y[p2])
plt.plot(x[p3], y[p3])


# In[44]:


x = np.linspace(-4, 4, 5000)

y = 1/((x-4)**2*(x-1))

b1 = x < 1
b2 = [(b > 1 and b < 4) for b in x]
b3 = x > 4

plt.plot(x[b1], y[b1])
plt.plot(x[b2], y[b2])
plt.plot(x[b3], y[b3])
plt.axis(ymin=-40, ymax=40)


# In[55]:


A = np.array([[np.random.rand() for n in range(5)] for n in range(5)])
B = np.array([[np.random.rand() for n in range(5)] for n in range(5)])

A@B-B@A


# In[58]:


C = A@B-B@A
C = C.flatten()
C


# In[66]:


C = C.reshape(1, 25)
C


# In[67]:


C = C.flatten().reshape(25, 1)
C


# In[76]:


x = np.linspace(0, 1, 200)
f1 = np.array([0.5*(1+(k/1)) for k in x])
f2 = np.array([0.5*(f1[k]+(x[k]/f1[k])) for k in range(len(x))])
f3 = np.array([0.5*(f2[k]+(x[k]/f2[k])) for k in range(len(x))])
sr = np.sqrt(x)

plt.plot(x, f1, label="$f_1(x)$")
plt.plot(x, f2, label="$f_2(x)$")
plt.plot(x, f3, label="$f_3(x)$")
plt.plot(x, sr, label="$\sqrt{x}$")
plt.title("Babylonisches Wurzelziehen")
plt.legend();


# In[116]:


A = np.array([n**2 for n in range(1, 17)]).reshape(4, 4)
v = [[22, -67, 67, -22]]
w = []
for n in range(10):
    w.append([])
    w[n] = A @ np.array(v[n])
    v.append([])
    v[n+1] = list((1/w[n][3]) * w[n])
print(str(np.array(v)) + "\n")
print(np.array(w)[:,3])


# In[ ]:





# In[ ]:




