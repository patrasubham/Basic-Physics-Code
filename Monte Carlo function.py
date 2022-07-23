#Monte Carlo Function

import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return (np.sin(1/(x*(2.0-x))))**2

xp=np.linspace(0.0001,1.9999,10000)

a=0.0
b=2.0
c=0.0
N=0.0
A=0.0
B=0.0
AA=[]
BB=[]

while(N<1e5):
    y=np.random.uniform(0,1)
    x=np.random.uniform(0,2)

    if y<=f(x):
        c+=1
        AA.append(x)
        BB.append(y)

    N+=1

A=(b-a)
B=A*(c/N)
print(c,N,c/N)
print(B)
plt.grid()
plt.scatter(xp,f(xp))
#plt.plot(xp,f(xp))
plt.show()
