#Semi Emperical mass formula
import numpy as np
import matplotlib.pyplot as plt

Z=float(input('Proton no.Z:'))
A=np.arange(Z,3*Z,1.0)
B=0.0
C=0.0
#Different Constant Coefficient
a1=15.8
a2=18.3
a3=0.714
a4=23.2
    
for j in A:
    if j%2.0!=0.0:
        a5=0.0
    elif j%2.0==0.0 and Z%2.0==0.0:
        a5=12.0
    elif j%2.0==0.0 and Z%2.0!=0.0:
        a5=-12.0

#Formula of Binding Energy formula           
B=a1*A -a2*A**(2.0/3.0)-a3*(Z**2.0/A**(1.0/3.0))-a4*(A-2.0*Z)**2/A+a5*A**(-0.5)
C=B/A
plt.plot(A,C)
'''
d=106
T=np.zeros(d)
M=np.zeros(d)
N=np.zeros(d)
L=np.zeros(d)

for i in range(d):
    n=int(3.0*Z-Z)
    m=n+1
    p=Z
    A=np.zeros(m)
    B=np.zeros(m)
    C=np.zeros(m)

    #Different Constant Coefficient
    a1=15.8
    a2=18.3
    a3=0.714
    a4=23.2
    
    for j in range(m):
        A[j]=p
        if A[j]%2.0!=0.0:
            a5=0.0
        elif A[j]%2.0==0.0 and Z%2.0==0.0:
            a5=12.0
        elif A[j]%2.0==0.0 and Z%2.0!=0.0:
            a5=-12.0

        #Formula of Binding Energy formula
            
        B[j]=a1*A[j] -a2*A[j]**(2.0/3.0)-a3*(Z**2.0/A[j]**(1.0/3.0))-a4*(A[j]-2.0*Z)**2/A[j]+a5*A[j]**(-0.5)

        C[j]=B[j]/A[j]
        p+=1
    x=max(C)
    for k in range(m):
        if C[k]==x:
            T[i]=Z
            M[i]=A[k]
            N[i]=B[k]
            L[i]=C[k]
            Z+=1
print (T,M)

'''
plt.xlabel('A')
plt.ylabel('B/A(MeV)')
plt.title('Graph(B/A) Vs A')
#plt.plot(T,L)
plt.show()

            
        

