                                                                  #Program:Time to Empty a Water Tank

import numpy as np
import matplotlib.pyplot as plt

#Constants
R=15
r=0.2
g=115.8

def f(t,h):
    return (h**2-2*R*h)/((r**2)*np.sqrt(2*g*h))

N=1000
a=28.0
b=0.0
p=(b-a)/N

hpoint=np.arange(a,b,p)
tpoint=[]
t0=0.0
for h0 in hpoint:
    tpoint.append(t0)
    t0=t0+p*f(t0,h0)
for i in range(len(hpoint)):
    if hpoint[i]<0.2:
        print(tpoint[i])
        break
plt.plot(tpoint,hpoint)
plt.ylabel("h in m")
plt.xlabel("t in sec")
plt.grid()
plt.title("Time to Empty a  Spherical Water Tank ")
plt.show()

