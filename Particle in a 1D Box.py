#Particle in a 1D Box
import numpy as np
import matplotlib.pyplot as plt

#Wavefunction
def psi(x,n,L):
    return np.sqrt(2.0/L)*np.sin(n*np.pi*x/L)


n = int(input("Enter the value for the quantum number n = "))
L = float(input("Enter the size of the box in Angstroms = "))


x = np.linspace(0, L, 1000)
fig= plt.subplots()

plt.plot(x, psi(x,n,L),'--r') 
plt.grid()


plt.xlabel('L')
plt.ylabel(r'$\psi_n(x)$')
plt.title('Wavefunction')

#Probability density 
fig= plt.subplots()
plt.plot(x, psi(x,n,L)*psi(x,n,L))

plt.xlabel('L')
plt.ylabel(r'$|\psi_n|^2(x)$')
plt.title('Probability Density')
plt.grid()

plt.show()
