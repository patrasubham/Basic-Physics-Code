#Coupled Differential Equation

from math import sin
from numpy import array,arange
import pylab as plt
x=-1
y=-1
def f(r,t):
    x=r[0]
    y=r[1]
    fx=16*x-36*y
    fy=6*x-14*y

    return array([fx,fy],float)
#Constant
a=0.0
b=10.0
N=1000
h=(b-a)/N
tpoints=arange(a,b,h)
xpoints=[]
ypoints=[]

r=array([10,10],float)
for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
#RK4
    k1=h*f(r,t)
    k2=h*f((r+(k1/2)),(t+h/2))
    k3=h*f((r+(k2/2)),(t+h/2))
    k4=h*f((r+(k3)),(t+h))
    r=r+(k1+2*k2+2*k3+k4)

plt.plot(tpoints,xpoints,'b-')
plt.plot(tpoints,ypoints,'r--')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.title('RK4-''Plot:Y vs X')
plt.show()

     
