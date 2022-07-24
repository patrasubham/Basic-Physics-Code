#D-dimensional volume of a sphere from 3 to 15

import numpy as np
import matplotlib.pyplot as plt
import random as rd

def f(n,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15):
    if (n==2):
        return x1**2+x2**2
    if (n==3):
        return x1**2+x2**2+x3**2
    if (n==4):
        return x1**2+x2**2+x3**2+x4**2
    if (n==5):
        return x1**2+x2**2+x3**2+x4**2+x5**2
    if (n==6):
        return x1**2+x2**2+x3**2+x4**2+x5**2+x6**2
    if (n==7):
        return x1**2+x2**2+x3**2+x4**2+x5**2+x6**2+x7**2
    if (n==8):
        return x1**2+x2**2+x3**2+x4**2+x5**2+x6**2+x7**2+x8**2
    if (n==9):
        return x1**2+x2**2+x3**2+x4**2+x5**2+x6**2+x7**2+x8**2+x9**2
    if (n==10):
        return x1**2+x2**2+x3**2+x4**2+x5**2+x6**2+x7**2+x8**2+x9**2+x10**2
    if (n==11):
        return x1**2+x2**2+x3**2+x4**2+x5**2+x6**2+x7**2+x8**2+x9**2+x10**2+x11**2
    if (n==12):
        return x1**2+x2**2+x3**2+x4**2+x5**2+x6**2+x7**2+x8**2+x9**2+x10**2+x11**2+x12**2
    if (n==13):
        return x1**2+x2**2+x3**2+x4**2+x5**2+x6**2+x7**2+x8**2+x9**2+x10**2+x11**2+x12**2+x13**2
    if (n==14):
        return x1**2+x2**2+x3**2+x4**2+x5**2+x6**2+x7**2+x8**2+x9**2+x10**2+x11**2+x12**2+x13**2+x14**2
    if (n==15):
        return x1**2+x2**2+x3**2+x4**2+x5**2+x6**2+x7**2+x8**2+x9**2+x10**2+x11**2+x12**2+x13**2+x14**2+x15**2

a=[]
d=np.arange(2,16,1)
n=1000000

for i in range(2,16,1):
    s=0.0
    c=0.0
    for j in range(n):
        rx1=rd.uniform(0,1)
        rx2=rd.uniform(0,1)
        rx3=rd.uniform(0,1)
        rx4=rd.uniform(0,1)
        rx5=rd.uniform(0,1)
        rx6=rd.uniform(0,1)
        rx7=rd.uniform(0,1)
        rx8=rd.uniform(0,1)
        rx9=rd.uniform(0,1)
        rx10=rd.uniform(0,1)
        rx11=rd.uniform(0,1)
        rx12=rd.uniform(0,1)
        rx13=rd.uniform(0,1)
        rx14=rd.uniform(0,1)
        rx15=rd.uniform(0,1)

        if (f(i,rx1,rx2,rx3,rx4,rx5,rx6,rx7,rx8,rx9,rx10,rx11,rx12,rx13,rx14,rx15)<1.0):
            c+=1
    s=2.0**i*c/n
    a.append(s)
plt.scatter(d,a)
#plt.plot(d,a)
plt.grid()

plt.show()
        
    


