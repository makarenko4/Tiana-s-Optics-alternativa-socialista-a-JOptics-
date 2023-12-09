import matplotlib.pyplot as plt
import numpy as np
import math
from math import sin, cos, asin, acos, tan, atan, pi
import matplotlib.cm as cm
import matplotlib.animation as animation
import fileinput

print("*** Interferòmetre de Young ***")



fig = plt.figure()
ax = fig.add_subplot(projection='3d')

u, v = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))

x = 15
y = u
z = v

ax.plot_surface(x, y, z, color='blue')
ax.text(16, -5, -4, "pantalla", color='red')

t = np.linspace(0,15,100)
x = t
y = 0*t
z = 0*t

ax.plot(x,y,z, color='cyan')

u, v = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))

x = 7.5
y = u
z = v

ax.plot_surface(x, y, z, color='blue')
ax.text(4.5, -5, -5, "pla d'obertures", color='red')

t = np.linspace(-5,5,100)
x = 0*t
y = t
z = 0*t
ax.plot(x,y,z,color='orange')
x = 0*t
y = 0*t
z = t
ax.plot(x,y,z,color='green')
ax.text(0, 5, 0, "eix Y", color='orange')
ax.text(0, 0, 5, "eix Z", color='green')

ax.text(5, -8, -8, "eix X", color='cyan')
ax.text(16, 6, -13, "eix Y", color='orange')
ax.text(17, 5, 6, "eix Z", color='green')

ax.set_aspect('equal')
ax.set_title("Referència per a l'orientació : ")

plt.show()



nF = int(input("Nombre de fonts : "))
lamda = []
Fx = []
Fy = []
Fz = []
EFx = []
EFy = []
EFz = []
for i in range(0,nF):
    print("\n")
    lamda.append( float(input("Longitud d'ona de la font "+str(i+1)+" : ")) )
    Fx.append( float(input("Posició x : ")) )
    Fy.append( float(input("Posició y : ")) )
    Fz.append( float(input("Posició z : ")) )
    EFx.append( float(input("Extensió en x ( 0 = puntual ) : ")) )
    EFy.append( float(input("Extensió en y ( 0 = puntual ) : ")) )
    EFz.append( float(input("Extensió en z ( 0 = puntual ) : ")) )

print("\n")
Ox = float(input("Posició x del pla d'obertures ( vigileu que quedi a la dreta de les fonts ! ) : "))
Oy = []
Oz = []
for i in range (0, 2):
    print("\n")
    Oy.append( float(input("Posició y de l'obertura "+str(i+1)+" : ")) )
    Oz.append( float(input("Posició z de l'obertura "+str(i+1)+" : ")) )
    
print("\n")
pant = float(input("Posició x de la pantalla ( vigileu que quedi a la dreta del pla d'obertures ! ) : "))
ampl = float(input('Amplada de la pantalla : '))
alca = float(input('Alçada de la pantalla : '))

if (ampl<20 and alca<20):
    res = 0.01
elif (ampl<100 and alca<100):
    res = 0.05
elif (ampl<250 and alca<250):
    res = 0.1
elif (ampl<500 and alca<500):
    res = 0.5
else:
    res = 1

AMPLADA = np.linspace(-ampl/2, ampl/2, int(ampl/res) )
ALCADA = np.linspace(-alca/2, alca/2, int(alca/res) )
Val = np.zeros((len(AMPLADA), len(ALCADA)))
Dist0 = np.zeros((len(AMPLADA), len(ALCADA)))
Dist1 = np.zeros((len(AMPLADA), len(ALCADA)))

FX = np.linspace(Fx[0] - EFx[0]/2 , Fx[0] + EFx[0]/2 , int(EFx[0]/res)+1 )
FY = np.linspace(Fy[0] - EFy[0]/2 , Fy[0] + EFy[0]/2 , int(EFy[0]/res)+1 )
FZ = np.linspace(Fz[0] - EFz[0]/2 , Fz[0] + EFz[0]/2 , int(EFz[0]/res)+1 )

for x in range (0,len(FX)):
    for y in range (0,len(FY)):
        for z in range(0,len(FZ)):
            
            L0 = ( (Ox-FX[x])**2 + (Oy[0]-FY[y])**2 + (Oz[0]-FZ[z])**2 )**0.5
            L1 = ( (Ox-FX[x])**2 + (Oy[1]-FY[y])**2 + (Oz[1]-FZ[z])**2 )**0.5
            
            for j in range(0,len(AMPLADA)):
                for k in range(0,len(ALCADA)):

                    Dist0[j, k] = ( ( (pant-Ox)**2 + (AMPLADA[j]-Oy[0])**2 + (ALCADA[k]-Oz[0])**2 )**0.5 )
                    Dist1[j, k] = ( ( (pant-Ox)**2 + (AMPLADA[j]-Oy[1])**2 + (ALCADA[k]-Oz[1])**2 )**0.5 )
                    
                    L0P = Dist0[j, k]
                    L1P = Dist1[j, k]
                    
                    DL = abs( (L1-L0) + (L1P-L0P) )
                    
                    Val[j, k] += ( 1 + cos( (2*pi/lamda[0])*DL ) )

for i in range (1, nF):
        FX = np.linspace(Fx[i] - EFx[i]/2 , Fx[i] + EFx[i]/2 , int(EFx[i]/res)+1 )
        FY = np.linspace(Fy[i] - EFy[i]/2 , Fy[i] + EFy[i]/2 , int(EFy[i]/res)+1 )
        FZ = np.linspace(Fz[i] - EFz[i]/2 , Fz[i] + EFz[i]/2 , int(EFz[i]/res)+1 )
        
        for x in range (0,len(FX)):
            for y in range (0,len(FY)):
                for z in range(0,len(FZ)):
                    
                    L0 = ( (Ox-FX[x])**2 + (Oy[0]-FY[y])**2 + (Oz[0]-FZ[z])**2 )**0.5
                    L1 = ( (Ox-FX[x])**2 + (Oy[1]-FY[y])**2 + (Oz[1]-FZ[z])**2 )**0.5
                    
                    for j in range(0,len(AMPLADA)):
                        for k in range(0,len(ALCADA)):
                            
                            L0P = Dist0[j, k]
                            L1P = Dist1[j, k]
                            
                            DL = abs( (L1-L0) + (L1P-L0P) )
                            
                            Val[j, k] += ( 1/(L0+L0P)**2 )**2 + ( 1/(L1+L1P)**2 )**2 + 2*( 1/(L0+L0P)**2 )*( 1/(L1+L1P)**2 )*cos( (2*pi/lamda[i])*DL )

ax = plt.gca()
ax.set_aspect('equal', adjustable='box')
plt.pcolormesh(ALCADA, AMPLADA, Val, cmap = cm.gray)
plt.show()