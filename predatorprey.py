#PREDATOR PREY CURVE :

import numpy as np
import matplotlib.pylab as plt

a=1.0
b=0.5
c=0.5
d=2.0

r=np.array([2.0,2.0],float)

def f(r,t):
     x=r[0]
     y=r[1]
     fx=a*x-b*x*y
     fy=c*x*y-d*y
     return np.array([fx,fy],float)
    
#Constant:   
A=0.0 #lower limit
B=10.0 #upper limit
N=1000 #no.of steps
h=(B-A)/N  #Step length

X=[]
Y=[]

#Runge Kutta 4th order:
T=np.arange(A,B,h)
for t in T:
    X.append(r[0])
    Y.append(r[1])
    
    k1=h*f(r,t)
    k2=h*f((r+k1/2),(t+h/2))
    k3=h*f((r+k2/2),(t+h/2))
    k4=h*f((r+k3/2),(t+h))
    r+=(1.0/6.0)*(k1+2*k1+2*k3+k4)
    
plt.title('PREDATOR AND PREY INTEGRATION CURVE:')
plt.plot(T,X,'r--',label='PREY')
plt.plot(T,Y,'g',label='PREDATOR')
plt.xlabel('Time (s)')
plt.ylabel('X & Y (m)')
plt.legend()
plt.grid()
plt.show()
