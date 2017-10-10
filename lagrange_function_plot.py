#%%
import matplotlib.pyplot as plt 
import numpy as np 
from scipy.interpolate import lagrange

x = np.arange(-5,5,0.001)
x1 = [-5,0,5]
x2 = [-5,-2.5,0,2.5,5]
x3 = [-5,-3.75,-2.5,-1.25,0,1.25,2.5,3.75,5]
x4 = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
y1=y2=y3=y4=[]
for a in x1 :
    y1.append(1/(1+a*a))
p1 = lagrange(x1,y1)
for a in x2 :
    y2.append(1/(1+a*a))
p2 = lagrange(x2,y2)
for a in x3 :
    y3.append(1/(1+a*a))
p3 = lagrange(x3,y3)
for a in x4 :
    y4.append(1/(1+a*a))
p4 = lagrange(x4,y4)



fig, ax = plt.subplots()
ax.plot(x, p1(x))
ax.plot(x, p2(x))
ax.plot(x, p3(x))
ax.plot(x, p4(x))
ax.plot(x,1/(1+x*x))
plt.show()

fig2,ax2=plt.subplots()
ax2.plot(x,1/(1+x*x))
ax2.grid()


ax.grid()
plt.show()
