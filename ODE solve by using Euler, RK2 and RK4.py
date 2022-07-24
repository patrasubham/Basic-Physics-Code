'''
dx/dt= (-)x^3+sin(t); x=0 at t=0.
Solve using Euler, RK2 & RK4 in the range t= 0 to 10 in 100 steps and plot.
'''
import numpy as np
import matplotlib.pylab as plt

#Using Euler..

T1=[]
X1=[]
def f(x,t):#defining a function
    y=-(x**3.0)+np.sin(t)
    return y

#Initial Values
t=0.0
x=0.0
h=0.1

for i in range (1,100):
    t=h*i
    v=x+h*f(x,t)
    T1.append(t)
    X1.append(x)
    x=v

print(T1,X1)

#Using Runge Kutta2 (RK2)

T2=[]
X2=[]

for i in range(1,100):
    t=h*i
    k1=h*f(x,t)
    k2=h*f((x+(k1/2)),(t+(h/2)))
    x=x+k2
    T2.append(t)
    X2.append(x)
    t=t+h
    i+=1

print(T2,X2)

#Using Runge Kutta 4(RK4)
T3=[]
X3=[]

for i in range (1,100):
    t=h*i
    k1=h*f(x,t)
    k2=h*f((x+(k1/2)),(t+(h/2)))
    k3=h*f((x+(k2/2)),(t+(h/2)))
    k4=h*f((x+k3),(t+h))
    x=x+((1.0/6.0)*(k1+2*k2+2*k3+k4))
    T3.append(t)
    X3.append(x)
    t=t+h
    i+=1

print(T3,X3)

plt.plot(T1,X1,'g',linewidth=2.0)
plt.scatter(T2,X2)
plt.plot(T3,X3,'r')
plt.title('ODE solve by using Euler, RK2 and RK4')
plt.grid()
plt.show()
    
