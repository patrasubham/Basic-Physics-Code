import numpy as np
import pylab as py
import scipy.optimize as op
import scipy.stats as st
data=np.loadtxt('quasar2.dat')
lum=data[:,0]
mass=data[:,2]
print(len(lum))
lum_v=[]
mass_v=[]
py.show()
for i in range(len(lum)):
    if(lum[i]>=44 and lum[i]<=49):
        lum_v.append(lum[i])
lum_v.sort()
for i in range(len(mass)):
    if(mass[i]>=7 and mass[i]<=11):
        mass_v.append(mass[i])

mass_v.sort()
py.hist(lum_v,bins=100,histtype='step',color='black')
py.xlim(44.5,48.5)
py.title("Binned Luminosity Data",fontsize=15)
py.xlabel(r'Luminosity in log$\frac{\mathrm{L}}{\mathrm{L}_{sun}}$',fontsize=15)
py.ylabel("Frequency",fontsize=15)
py.grid('true')
py.show()
py.hist(mass_v,bins=100,histtype='step',color='black')
py.xlim(7,11)
py.title("Binned Mass Data",fontsize=15)
py.xlabel(r'Mass in log$\frac{\mathrm{M}}{\mathrm{M}_{sun}}$',fontsize=15)
py.ylabel("Frequency",fontsize=15)
py.grid('true')
py.show()
ylum,lum_ival=np.histogram(lum_v,bins=100)
luminosity= lum_ival[:-1]+np.diff(lum_ival)/2
ymass,mass_ival=np.histogram(mass_v,bins=100)
mass_f= mass_ival[:-1]+np.diff(mass_ival)/2

def f(x,my,mx,r):
    return(my+r*(x-mx))
py.plot(mass_f,luminosity,'k.')
pa,pa1=op.curve_fit(f,mass_f,luminosity)
y=f(mass_f,*pa)
print(pa)
py.plot(mass_f,y)
py.title("Mass-Luminosity Relation",fontsize=15)
py.ylabel(r'Mean of Binned Luminosity in log$\frac{\mathrm{L}}{\mathrm{L}_{sun}}$',fontsize=15)
py.xlabel(r'Mean of Binned Mass in log$\frac{\mathrm{M}}{\mathrm{M}_{sun}}$',fontsize=15)
py.grid('true')
py.ylim(44,49)
py.xlim(7,11)
py.show()
co = np.stack((mass_f,luminosity), axis=0)
cov_val=np.cov(co)
print(cov_val)
var_mass=cov_val[0,0]
var_lum=cov_val[1,1]
cov_ml=cov_val[1,0]

r=cov_ml/(np.sqrt(var_mass*var_lum))
print(r)
corr, _ = st.pearsonr(mass_f,luminosity)
print(corr)
mass_v=[]
lum_v=[]
for i in range (len(mass_f)):
    mass_v.append(np.power(10,mass_f[i]))
    lum_v.append(np.power(10,luminosity[i]))

def fitfunc(x,A,m):
    return A*np.power(x,m)

params,par_c=op.curve_fit(fitfunc,mass_v,lum_v,p0=[10e36,2.0])
print(params)
py.loglog(mass_v,lum_v,'k.')
c=np.mean(luminosity)-r*var_lum*np.mean(mass_f)/var_mass
y=np.power(10,c)*np.power(mass_v,r*var_lum/var_mass)
py.loglog(mass_v,y)
y=fitfunc(mass_v,*params)
py.loglog(mass_v,y)
py.show()

print(c)
print(np.mean(luminosity))
print(np.mean(mass_f))
print(r*var_lum/var_mass)
print(r*var_mass/var_lum)
print(np.power(10,36.25)*3.828*10e26/(1.989*10e30))