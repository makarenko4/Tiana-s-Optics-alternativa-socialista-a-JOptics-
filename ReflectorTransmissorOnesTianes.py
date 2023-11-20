#Arnau Carnicé Rey (NIUB20550740), exercici 2 d'avaluació continuada. Òptica. Tardor 2023. Codi.

import matplotlib.pyplot as plt
import numpy as np
import math
from math import sin, cos, asin, acos, tan, atan, pi
import matplotlib.animation as animation

print("SIMULADOR DE REFLEXIÓ I TRANSMISSIÓ DE LA LLUM EN MEDIS DIELÈCTRICS ISÒTROPS")

n1 = float(input( ' Índex de reflexió del medi de procedència : ' ))
n2 = float(input( ' Índex de reflexió passada la superfície : ' ))
Th_i = float(input( ' Angle d\'incidència (rad) : ' ))
A1 = float(input( ' Amplitud en el pla d\'incidència : ' ))
A2 = float(input( ' Amplitud en el pla perpendicular : ' ))

print(' Determinació de la polarització de l\'ona incident : ')
print(' Per mitjà de l\'inclinació de l\'el·lipse (1) \n Per mitjà del desfasament entre components (2) ')
tria = int(input( ' : ' ))

if (tria == 1):
    xi = float(input(' Angle d\'inclinació de l\'el·lipse (rad) : '))
    delta = acos( (A1**2-A2**2)*tan(2*xi)/(2*A1*A2) )
else:
    delta = float(input(' Desfasament de la component perpendicular respecte de la paral·lela (rad) : '))
    #xi = atan( (2*A1*A2)*cos(delta)/(A1**2-A2**2) )/2
    
delta1=0
delta2=delta

if (n1>n2):
    lim = asin(n2/n1)

try:
    Th_t = asin(n1*sin(Th_i)/n2)
    overlimit = False
except(ValueError):
    overlimit = True

if not overlimit :
    try:
        r1 = tan( Th_t - Th_i )/tan( Th_t + Th_i )
        r2 = sin( Th_t - Th_i )/sin( Th_t + Th_i )
    except(ZeroDivisionError):
        r1 = (n1 - n2)/(n1 + n2)
        r2 = r1

    try:
        t1 = 2*sin(Th_t)*cos(Th_i)/( sin(Th_t + Th_i)*cos(Th_t - Th_i) )
        t2 = 2*sin(Th_t)*cos(Th_i)/sin(Th_t + Th_i)
    except(ZeroDivisionError):
        t1 = 2*n1/(n1  + n2)
        t2 = t1
        
    Ar1 = r1*A1
    Ar2 = r2*A2
    if (Ar1<0):
        Ar1 = -Ar1
        delta1 += pi
    if (Ar2<0):
        Ar2 = -Ar2
        delta2 += pi

    At1 = t1*A1
    At2 = t2*A2
        
else:
    r1 = -1
    r2 = 1
    
    N=n2/n1
    a = atan((sin(Th_i)**2-N**2)**0.5/(cos(Th_i)*N**2))
    b = atan((sin(Th_i)**2-N**2)**0.5/(cos(Th_i)))
    
    Ar1 = A1
    Ar2 = A2
    delta1 += 2*a+pi
    delta2 += 2*b

    t1 = 0
    t2 = 0
    At1 = 0
    At2 = 0

delta1 = delta1 % (2*pi)
delta2 = delta2 % (2*pi)

print('\nANGLES : ')
print('theta incident = '+str(Th_i))
print('theta reflectida = '+str(Th_i))
if (n1>n2):
    print('angle límit = '+str(lim))
    if (Th_i<=lim):
        print('theta transmesa = '+str(Th_t))
else:
    print('theta transmesa = '+str(Th_t))
print('angle de Brewster = '+str(atan(n2/n1)))

print('\nCOEFICIENTS DE FRESNEL : ')
print('r paral·lela = '+str(r1))
print('r perpendicular = '+str(r2))
print('t paral·lela = '+str(t1))
print('t perpendicular = '+str(t2))

print('\nCÀLCUL DE LES AMPLITUDS : ')
print('A reflectida paral·lela = '+str(Ar1))
print('A reflectida perpendicular = '+str(Ar2))
print('A transmesa paral·lela = '+str(At1))
print('A transmesa perpendicular = '+str(At2))

print('\nFASES : ')
print('Fase paral·lela d\'incidència = '+str(0))
print('Fase perpendicular d\'incidència = '+str(delta))
print('Fase paral·lela de reflexió = '+str(delta1))
print('Fase perpendicular de reflexió = '+str(delta2))
print('Fase paral·lela de transmissió = '+str(0))
print('Fase perpendicular de transmissió = '+str(delta))

print('\nENERGIA (FACTORS DE FRESNEL) : ')
R1=r1**2
R2=r2**2
T1=1-R1
T2=1-R2
print('R paral·lela = '+str(R1))
print('R perpendicular = '+str(R2))
print('T paral·lela = '+str(T1))
print('T perpendicular = '+str(T2))

if not overlimit:
    fig, ax=plt.subplots(2,3)
else:
    fig, ax=plt.subplots(2,2)
plt.tight_layout()

ax[0,0].set_aspect('equal', adjustable='box')
ax[0,0].set_xlim([-5, 5])
ax[0,0].set_ylim([-5, 5])

ax[1,0].set_aspect('equal', adjustable='box')
ax[1,0].set_xlim([-A1, A1])
ax[1,0].set_ylim([-A2, A2])

ax[0,1].set_aspect('equal', adjustable='box')
ax[0,1].set_xlim([-5, 5])
ax[0,1].set_ylim([-5, 5])

ax[1,1].set_aspect('equal', adjustable='box')
ax[1,1].set_xlim([-Ar1, Ar1])
ax[1,1].set_ylim([-Ar2, Ar2])

if not overlimit:
    ax[0,2].set_aspect('equal', adjustable='box')
    ax[0,2].set_xlim([-5, 5])
    ax[0,2].set_ylim([-5, 5])

    ax[1,2].set_aspect('equal', adjustable='box')
    ax[1,2].set_xlim([-At1, At1])
    ax[1,2].set_ylim([-At2, At2])

try:
    factor = 1/tan(Th_i)
except(ZeroDivisionError):
    factor = 1e9

if(n1 != n2):

    X = [ -5 , 0 ]
    S = [ 5*factor , 0 ]
    ax[0, 0].plot(X,S,'r-')
    X = [ 0 , 5 ]
    S = [ 0 , 5*factor ]
    ax[0, 0].plot(X,S,'g-')
        
    X = [ -5 , 0 ]
    S = [ 5*factor , 0 ]
    ax[0, 1].plot(X,S,'g-')
    X = [ 0 , 5 ]
    S = [ 0 , 5*factor ]
    ax[0, 1].plot(X,S,'r-')
    
    if not overlimit:
        X = [ -5 , 0 ]
        S = [ 5*factor , 0 ]
        ax[0, 2].plot(X,S,'g-')
        X = [ 0 , 5 ]
        S = [ 0 , 5*factor ]
        ax[0, 2].plot(X,S,'g-')
    
else:
    X = [ -5 , 0 ]
    S = [ 5*factor , 0 ]
    ax[0, 0].plot(X,S,'r-')
    
    X = [ -5 , 0 ]
    S = [ 5*factor , 0 ]
    ax[0, 1].plot(X,S,'g-')
    
    if not overlimit:
        X = [ -5 , 0 ]
        S = [ 5*factor , 0 ]
        ax[0, 2].plot(X,S,'g-')

if not overlimit:
    try:
        factor = 1/tan(Th_t)
    except(ZeroDivisionError):
        factor = 1e9

    X = [ 0 , 5 ]
    I = [ 0 , -5*factor ]
    ax[0, 0].plot(X,I,'g-')

    X = [ 0 , 5 ]
    I = [ 0 , -5*factor ]
    ax[0, 1].plot(X,I,'g-')

    X = [ 0 , 5 ]
    I = [ 0 , -5*factor ]
    ax[0, 2].plot(X,I,'r-')
    
    X = [-5,5]
    ax[0, 2].plot(X, [0,0], 'k--')
    ax[0, 2].plot([0,0], X, 'k--')

X = [-5,5]
ax[0, 0].plot(X, [0,0], 'k--')
ax[0, 0].plot([0,0], X, 'k--')

X = [-5,5]
ax[0, 1].plot(X, [0,0], 'k--')
ax[0, 1].plot([0,0], X, 'k--')


X1 = []
Y1 = []
X2 = []
Y2 = []
X3 = []
Y3 = []

ax[1,0].plot(0,0)
ax[1,1].plot(0,0)

if not overlimit:
    ax[1,2].plot(0,0)

fr = 100
itv = 1

def update(i):
    ax[1,0].cla()
    X1.append(A1*cos(2*pi*i/fr))
    ax[1,0].arrow(0,0,A1*cos(2*pi*i/fr),0)
    Y1.append(A2*cos(2*pi*i/fr+delta))
    ax[1,0].arrow(0,0,0,A2*cos(2*pi*i/fr+delta))
    ax[1,0].scatter(X1,Y1,s=0.25)
    ax[1,0].arrow(0,0,A1*cos(2*pi*i/fr),A2*cos(2*pi*i/fr+delta))
    
    ax[1,1].cla()
    X2.append(Ar1*cos(2*pi*i/fr+delta1))
    ax[1,1].arrow(0,0,Ar1*cos(2*pi*i/fr+delta1),0)
    Y2.append(Ar2*cos(2*pi*i/fr+delta2))
    ax[1,1].arrow(0,0,0,Ar2*cos(2*pi*i/fr+delta2))
    ax[1,1].scatter(X2,Y2,s=0.25)
    ax[1,1].arrow(0,0,Ar1*cos(2*pi*i/fr+delta1),Ar2*cos(2*pi*i/fr+delta2))
    
    if not overlimit:
        ax[1,2].cla()
        X3.append(At1*cos(2*pi*i/fr))
        ax[1,2].arrow(0,0,At1*cos(2*pi*i/fr),0)
        Y3.append(At2*cos(2*pi*i/fr+delta))
        ax[1,2].arrow(0,0,0,At2*cos(2*pi*i/fr+delta))
        ax[1,2].scatter(X3,Y3,s=0.25)
        ax[1,2].arrow(0,0,At1*cos(2*pi*i/fr),At2*cos(2*pi*i/fr+delta))
    
ani = animation.FuncAnimation(fig=fig, func=update, frames=fr, interval=itv)
plt.show()

Th = np.linspace(0,pi/2 - 1e-9,10000)
X = []

r1 = []
r2 = []
t1 = []
t2 = []

for i in range(0,len(Th)):
    
    try:
        Th_t = asin(n1*sin(Th[i])/n2)
        overlimit = False
    except(ValueError):
        overlimit = True

    if not overlimit :
        try:
            r1.append( tan( Th_t - Th[i] )/tan( Th_t + Th[i] ) )
            r2.append( sin( Th_t - Th[i] )/sin( Th_t + Th[i] ) )
        except(ZeroDivisionError):
            r1.append( (n1 - n2)/(n1 + n2) )
            r2.append( (n1 - n2)/(n1 + n2) )
            
        X.append(Th[i])
        try:
            t1.append( 2*sin(Th_t)*cos(Th[i])/( sin(Th_t + Th[i])*cos(Th_t - Th[i]) ) )
            t2.append( 2*sin(Th_t)*cos(Th[i])/sin(Th_t + Th[i]) )
        except(ZeroDivisionError):
            t1.append( 2*n1/(n1  + n2) )
            t2.append( 2*n1/(n1  + n2) )
    else:
        r1.append(-1)
        r2.append(1)


plt.plot([0,1.6],[-1,-1],'k--', linewidth=1)
plt.plot([0,1.6],[0,0],'k--', linewidth=1)
plt.plot([0,1.6],[1,1],'k--', linewidth=1)
plt.plot([0,1.6],[2*n1/(n1  + n2), 2*n1/(n1  + n2)],'k--', linewidth=1)
plt.plot([0,1.6],[(n1 - n2)/(n1 + n2), (n1 - n2)/(n1 + n2)],'k--', linewidth=1)
if (n1>n2):
    plt.plot([lim, lim],[-1, t1[len(t1)-1]],'k--', linewidth=1)

plt.plot(Th,r1,'y-', label = 'r paral·lel', linewidth=1)
plt.plot(Th,r2,'g-', label = 'r perpendicular', linewidth=1)
plt.plot(X,t1,'b-', label = 't paral·lel', linewidth=1)
plt.plot(X,t2,'r-', label = 't perpendicular', linewidth=1)


d1 = []
d2 = []

for i in range(0,len(Th)):
    
    try:
        Th_t = asin(n1*sin(Th[i])/n2)
        overlimit = False
    except(ValueError):
        overlimit = True

    if not overlimit :
        
        res1 = 0
        res2 = delta
        
        if (r1[i]<0):
            res1 += pi
        if (r2[i]<0):
            res2 += pi
        
        d1.append(res1)
        d2.append(res2)
        
    else:
        N=n2/n1
        a = atan((sin(Th[i])**2-N**2)**0.5/(cos(Th[i])*N**2))
        b = atan((sin(Th[i])**2-N**2)**0.5/(cos(Th[i])))
        d1.append( (2*a + pi)%(2*pi) )
        d2.append( (delta + 2*b)%(2*pi) )

plt.plot(Th,d1, color='pink', label = 'fase refl. para.', linewidth=1)
plt.plot(Th,d2, color='purple', label = 'fase refl. perp.', linewidth=1)

plt.legend()
plt.xlabel('Angle d\'incidència (rad)')
plt.show()