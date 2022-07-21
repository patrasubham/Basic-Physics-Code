import numpy as np
import matplotlib.pylab as plt

t=[50,100,250,480,770]
p=6.0e28
V=1.0e-5
k=1.38e-23
a=0.0
T=5.0
T_f=500
A=np.zeros(int(T_f-T))
B=np.zeros(int(T_f-T))

x0=0.0
x1=0.538469
x3=0.906180

def f(x):
    y=((x**4)*np.exp(x))/((np.exp(x)-1.0)**2)
    return(y)

for j in range (len(t)):
    T=5.0
    for i in range (int(T_f-T)):
        x0=0.0
        x1=0.538469
        x3=0.906180
        b=t[j]/T
        x0=(b-a)*0.5*x0+(b+a)*0.5
        x1=(b-a)*0.5*x1+(b+a)*0.5
        x2=-x1
        x3=(b-a)*0.5*x3+(b+a)*0.5
        x4=-x3

        w0=0.568890*(b-a)*0.5
        w1=0.478629*(b-a)*0.5
        w2=w1
        w3=0.236927*(b-a)*0.5
        w4=w3

       # print(b-a)
       # print(b+a)

        S=w0*f(x0)+w1*f(x1)+w2*f(x2)+w3*f(x3)+w4*f(x4)

        C=9.0*V*p*k*((T/t[j])**3.0)*S
        A[i]=T
        B[i]=C
        T=T+1.0
    plt.plot(A,B)
plt.grid()
plt.show()
