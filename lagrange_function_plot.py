#%%
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import lagrange

x = np.linspace(-5,5,1000)
ax = plt.subplot()

ax.plot(x,1/(1+x**2),label="f(x)")
for n in [2,4,8,10]:
    x_n=[-5+(10/n)*i for i in range (n+1)]
    y_n=[1/(1+x**2) for x in x_n]
    lag=lagrange(x_n,y_n)
    ax.plot(x,lag(x),label="n={0}".format(n))
ax.grid()
ax.legend()
plt.show()