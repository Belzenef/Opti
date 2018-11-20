#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 15:15:05 2018
TD4 - Partie 1 
@author: ejacquemet
"""

#Imports from the matplotlib library
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
from  math import sqrt, exp, log
import time
#np.random.seed(10)

################################
## 1 : Fonction de R dans R   ##
################################

print("---------- Définition de f ----------")
def f1(x) :
    return(x**4-x**3-20*x**2+x+1)
print("f(2)= ",f1(2))
print("cf figure")

X = np.arange(-6, 7, 0.1) 
Y = f1(X)

minglob=3.6
minloc=-2.8
'''
# Affichage figure
fig = plt.figure() 
ax = fig.gca() 
ax.set_title('')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.plot(X,Y,color="crimson", label="f(x)",zorder=1)
ax.scatter(minglob,f1(minglob),zorder=2)
ax.scatter(minloc,f1(minloc),zorder=2)
ax.legend()
plt.savefig("fonctionf1.png")
plt.show()
'''

# gradient de f
def gradf1(x) :
    return(4*x**3-3*x**2-40*x+1)

def recuit(x0,k1,k2,tmax) :
    #init
    T=1.0
    X=np.zeros(tmax)
    X[0]=x0
    racine=x0
    t=1
    N=[]
    norme=abs(gradf1(x0))
    N.append(log(norme))
    while( norme>0.001 and t<tmax):
        #deplacement
        D=np.random.normal(0, sqrt(k1*exp(-1.0/(1000*T))))
        new=X[t-1]+D
        #eval
        if f1(new)<f1(X[t-1]) :
            X[t]=new
        else :
            X[t]=X[t-1]
            test=np.random.random()
            if test<k2*exp(-1.0/(1000*T)) :
                X[t]=new
        #critère d'arrêt  
        norme=abs(gradf1(X[t]))
        N.append(log(norme))
        racine=X[t]
        #diminution T
        t+=1
        T=1.0/t
    X[t:]=racine
    print("Solution : ",racine)
    print("Nombre d'iterations : ",t)
    print("Norme gradient : ",norme)
    
    return (X,racine,t,norme,N)

# paramètres :
k1=10
k2=0.5
tmax=100
x01=2
x02=-3
print("\nCalcul des points d'équilibres : ")
print("\nx0=%d, k=%4.2f, k'=%4.2f, tmax=%d :" %(x01,k1,k2,tmax) )
tmps1=time.clock()
res1=recuit(x01,k1,k2,tmax)
tmps2=time.clock()
print ("Temps d'execution : %s secondes --- " %(tmps2-tmps1))
tmax=100000
print("\nx0=%d, k=%4.2f, k'=%4.2f, tmax=%d :" %(x02,k1,k2,tmax) )
tmps1=time.clock()
res2=recuit(x02,k1,k2,tmax)
tmps2=time.clock()
print ("Temps d'execution : %s secondes --- " %(tmps2-tmps1))

# Stats
'''
fichier = open("paramsf.txt", "a")
fichier.write("k1\tk2\tDepart\tSolution\tnbIter\n")
k2=0.5
for k1 in [0.1,1,10] :
    for i in range(200) :
        res=recuit(-3,k1,k2,tmax)
        fichier.write(str(k1)+"\t"+str(k2)+"\t"+"-3\t"+str(res[1])+"\t"+str(res[2])+"\n")
        res=recuit(2,k1,k2,tmax)
        fichier.write(str(k1)+"\t"+str(k2)+"\t"+"2\t"+str(res[1])+"\t"+str(res[2])+"\n")
k1=1
for k2 in [50,5,0.05] :
    for i in range(200) :
        res=recuit(-3,k1,k2,tmax)
        fichier.write(str(k1)+"\t"+str(k2)+"\t"+"-3\t"+str(res[1])+"\t"+str(res[2])+"\n")
        res=recuit(2,k1,k2,tmax)
        fichier.write(str(k1)+"\t"+str(k2)+"\t"+"2\t"+str(res[1])+"\t"+str(res[2])+"\n")
fichier.close()
'''


# trajectoire 
'''
Y1=res1[0]
Y2=res2[0]
racine1=res1[1]
racine2=res2[1]
fig = plt.figure() 
ax = fig.gca() 
ax.set_title("k=1 - k'=0.05")
ax.set_xlabel('x')
ax.set_ylabel('y')

ax.plot(Y1,f1(Y1),label="x0=2",zorder=1)
ax.plot(X,Y,color="crimson", label="f(x)")
#ax.plot(Y2,f1(Y2),label="x0=-3",zorder=2)
ax.scatter(racine1,f1(racine1),color="orange",zorder=3)
#ax.scatter(racine2,f1(racine2))
plt.xlim([-6,7])
plt.ylim([-200,1000])
ax.legend()
plt.savefig("k1k'005.png")
plt.show()
'''

# impact sur itérations
'''
X=np.linspace(0.1,10,5)
Y1=np.zeros(len(X))
Y2=np.zeros(len(X))
for i in range(len(X)) :
    Y1[i] = recuit(2,X[i],k2,tmax)
    Y2[i] = recuit(-3,X[i],k2,tmax)

# Affichage figure

K1=[0.01,0.1,1,10]
K2=[0.05,0.5,5,50]
Y1=[2269,4081,6458,8668]
Y2=[8670,8668,8720,9832]
fig = plt.figure() 
ax = fig.gca() 
ax.set_title("Evolution du nombre d'itération moyen en fonction de k'")
ax.set_xlabel("k'")
ax.set_ylabel('nb iter')
ax.scatter(K2,Y2)
ax.plot(K2,Y2)
#ax.scatter(K2,Y2, label="k'")
ax.legend()
#plt.savefig("fonctionf1.png")
plt.show()
'''
'''
# impact sur l'évolution de la norme
X=np.arange(len(res2[4]))
Y1=res2[4]

# Affichage figure
fig = plt.figure() 
ax = fig.gca() 
ax.set_title("Evolution de la norme - k=%.3f ; k'=%.3f" % (k1,k2) )
ax.set_xlabel("itération")
ax.set_ylabel("log(norme)")
ax.plot(X,Y1)
ax.plot([0,10000],[log(0.001),log(0.001)],color="crimson")
ax.legend()
plt.ylim([-10,12])
#plt.savefig("log_normef1.k10.k'05.png")
plt.show()
'''

##################################
## 2 : Fonction de R^2 dans R   ##
##################################
print("\n---------- Définition de g ----------")
def g1(p) :
    return(f1(p[0])+f1(p[1]))
print("g(1,2)= ",g1([1,2]))
print("cf figure")

x = np.arange(-5, 5, 0.25) # échelle x
y = np.arange(-5, 5, 0.25) # échelle y
z = x**4 - x**3 - 20*x**2 + x + 1 + y**4 - y**3 - 20*y**2 + y + 1
'''
# Affichage figure
fig = plt.figure() # ouverture de la zone graphique
ax = fig.gca(projection='3d') 
x = np.arange(-5, 5, 0.1) # échelle x
y = np.arange(-5, 5, 0.1) # échelle y
x, y = np.meshgrid(x, y) # tracé de la grille
F= x**4 - x**3 - 20*x**2 + x + 1 + y**4 - y**3 - 20*y**2 + y + 1
surf = ax.plot_surface(x, y, F,zorder=3, rstride=1, cstride=1, alpha=0.4, linewidth=0, cmap=cm.PRGn, antialiased=False)
ax.set_title('')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('g(x,y)')
ax.scatter(3,3,g1([3,3])+50, s=100, color="lime",zorder=2)
ax.scatter(-3,3,g1([-3,3])+50, s=100, color="orange",zorder=2)
ax.scatter(-3,-3,g1([-3,-3])+50, s=100,color="orange",zorder=2)
ax.scatter(0,0,g1([0,0])+50, s=100, color="red",zorder=2)
ax.scatter(3,-3,g1([3,-3])+50, s=100,color="orange",zorder=2)
ax.scatter(0,3,g1([0,-3]), s=100,color="blue",zorder=2)
ax.scatter(0,-3,g1([0,-3]), s=100,color="blue",zorder=2)
ax.scatter(-3,0,g1([-3,0]), s=100,color="blue",zorder=2)
ax.scatter(3,0,g1([-3,0]), s=100,color="blue",zorder=2)
fig.colorbar(surf, shrink=0.5, aspect=5)
#plt.savefig("fonctionf1.png")
plt.show()
'''

# gradient de g
def gradg1(p):
    dx=4*p[0]**3 - 3*p[0]**2 - 40*p[0] + 1 
    dy=4*p[1]**3 - 3*p[1]**2 - 40*p[1] + 1
    return [dx,dy]

def recuit2D(p0,k1,k2,tmax) :
    #init
    T=1.0
    P=np.zeros((tmax,2))
    steps=np.zeros((2,tmax))
    P[0]=p0
    steps[0][0]=p0[0]
    steps[1][0]=p0[1]
    racine=p0
    t=1
    grad=gradg1(p0)
    norme=abs(grad[0])+abs(grad[1])
    N=[]
    N.append(log(norme))
    while( norme>0.001 and t<tmax):
        #deplacement
        D=[np.random.normal(0, sqrt(k1*exp(-1.0/(1000*T)))),np.random.normal(0, sqrt(k1*exp(-1.0/(1000*T))))]
        new=P[t-1]+D
        #eval
        if g1(new)<g1(P[t-1]) :
            P[t]=new
        else :
            P[t]=P[t-1]
            test=np.random.random()
            if test<k2*exp(-1.0/(1000*T)) :
                P[t]=new
        #critère d'arrêt  
        grad=gradg1(P[t])
        norme=abs(grad[0])+abs(grad[1])
        N.append(log(norme))
        racine=P[t]
        steps[0][t]=racine[0]
        steps[1][t]=racine[1]
        #diminution T
        t+=1
        T=1.0/t
    P[t:]=racine
    steps[0][t:]=racine[0]
    steps[1][t:]=racine[1]
    '''
    print("Solution : ",racine)
    print("Nombre d'iterations : ",t)
    print("Norme gradient : ",norme)
    '''
    return (steps,racine,t,norme,N)

# paramètres :
e=10^(-3)
k1=10
k2=.1
tmax=20000
x0=[-4,-4]
print("\nCalcul des points d'équilibres : ")
print("\nx0=(%d,%d), k=%4.2f, k'=%4.2f, tmax=%d :" %(x0[0],x0[1],k1,k2,tmax) )
tmps1=time.clock()
res3=recuit2D(x0,k1,k2,tmax)
tmps2=time.clock()
print ("Temps d'execution : %s secondes --- " %(tmps2-tmps1))
'''
# Affichage figure
fig = plt.figure() # ouverture de la zone graphique
ax = fig.gca(projection='3d') 
x = np.arange(-5, 5, 0.1) # échelle x
y = np.arange(-5, 5, 0.1) # échelle y
x, y = np.meshgrid(x, y) # tracé de la grille

F= x**4 - x**3 - 20*x**2 + x + 1 + y**4 - y**3 - 20*y**2 + y + 1
surf = ax.plot_surface(x, y, F, rstride=1, zorder=1,alpha=0.6,cstride=1, linewidth=0, cmap=cm.PRGn, antialiased=False)
#ax.set_title("\nx0=(%d,%d), k=%4.3f, k'=%4.3f, tmax=%d :" %(x0[0],x0[1],k1,k2,tmax) )
ax.plot(res3[0][0], res3[0][1], g1(res3[0]),zorder=2) #plot definition and options 
ax.scatter(res3[1][0],res3[1][1],g1(res3[1]), s=100, color="blue",zorder=3)
ax.scatter(x0[0],x0[0],g1(x0), s=100, color="red",zorder=4)
ax.set_xlim([-6,6])
ax.set_ylim([-6,6])
ax.set_zlim([-100,500])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('g(x,y)')

fig.colorbar(surf, shrink=0.5, aspect=5)
#plt.savefig("fonctionf1.png")
plt.show()
'''

'''
fichier = open("paramsg4.txt", "a")
fichier.write("k1\tk2\tDepart\tX\tY\tnbIter\n")
k2=0.1
for k1 in [0.1,1,10] :
    for i in range(100) :
        res=recuit2D([-4,4],k1,k2,tmax)
        fichier.write(str(k1)+"\t"+str(k2)+"\t-4\t"+str(res[1][0])+"\t"+str(res[1][1])+"\t"+str(res[2])+"\n")
        res=recuit2D([4,4],k1,k2,tmax)
        fichier.write(str(k1)+"\t"+str(k2)+"\t4\t"+str(res[1][0])+"\t"+str(res[1][1])+"\t"+str(res[2])+"\n")
k1=0.01
for k2 in [50,5,0.5] :
    for i in range(100) :
        res=recuit2D([-4,4],k1,k2,tmax)
        fichier.write(str(k1)+"\t"+str(k2)+"\t-4\t"+str(res[1][0])+"\t"+str(res[1][1])+"\t"+str(res[2])+"\n")
        res=recuit2D([4,4],k1,k2,tmax)
        fichier.write(str(k1)+"\t"+str(k2)+"\t4\t"+str(res[1][0])+"\t"+str(res[1][1])+"\t"+str(res[2])+"\n")
fichier.close()
'''
'''
# impact sur l'évolution de la norme
X=np.arange(len(res3[4]))
Y1=res3[4]

# Affichage figure
fig = plt.figure() 
ax = fig.gca() 
ax.set_title("Evolution de la norme - k=%.3f ; k'=%.3f" % (k1,k2) )
ax.set_xlabel("itération")
ax.set_ylabel("log(norme)")
ax.plot(X,Y1)
ax.plot([0,20000],[log(0.001),log(0.001)],color="crimson")
ax.legend()
plt.ylim([-10,12])
plt.savefig("log_normeg1.k01.k'005.png")
plt.show()

'''

########################################
## 4 : Modification de l'algorithme   ##
########################################
print("\n---------- Amélioration ----------")

def recuit2DV2(p0,k1,k2,tmax) :
    #init
    m=5
    T=1.0
    P=np.zeros((tmax,2))
    steps=np.zeros((2,tmax))
    P[0]=p0
    steps[0][0]=p0[0]
    steps[1][0]=p0[1]
    racine=p0
    t=1
    grad=gradg1(p0)
    norme=abs(grad[0])+abs(grad[1])
    while( norme>0.001 and t<tmax):
        s=0
        for i in range(m) :
            D=[np.random.normal(0, sqrt(k1*exp(-1.0/(1000*T)))),np.random.normal(0, sqrt(k1*exp(-1.0/(1000*T))))]
            xi=P[t-1]+D
            s+=(g1(xi)-g1(P[t-1]))
        De=s/m
        #deplacement
        D=[np.random.normal(0, sqrt(k1*exp(-1.0/(1000*T)))),np.random.normal(0, sqrt(k1*exp(-1.0/(1000*T))))]
        new=P[t-1]+D
        #eval
        if g1(new)<g1(P[t-1]) :
            P[t]=new
        else :
            P[t]=P[t-1]
            test=np.random.random()
            if test<k2*exp(-De/(1000*T)) :
                P[t]=new
        #critère d'arrêt  
        grad=gradg1(P[t])
        norme=abs(grad[0])+abs(grad[1])
        racine=P[t]
        steps[0][t]=racine[0]
        steps[1][t]=racine[1]
        #diminution T
        t+=1
        T=1.0/t
    P[t:]=racine
    steps[0][t:]=racine[0]
    steps[1][t:]=racine[1]
    '''
    print("Solution : ",racine)
    print("Nombre d'iterations : ",t)
    print("Norme gradient : ",norme)
    '''
    return (steps,racine,t,norme)


# paramètres :
e=10^(-3)
k1=10
k2=0.1
tmax=20000
x0=[-4,-4]
print("\nCalcul des points d'équilibres : ")
print("\nx0=(%d,%d), k=%4.2f, k'=%4.2f, tmax=%d :" %(x0[0],x0[1],k1,k2,tmax) )
tmps1=time.clock()
res4=recuit2DV2(x0,k1,k2,tmax)
tmps2=time.clock()
print ("Temps d'execution : %s secondes --- " %(tmps2-tmps1))

# impact sur l'évolution de la norme
X=np.arange(len(res3[4]))
Y1=res3[4]

# Affichage figure
fig = plt.figure() 
ax = fig.gca() 
ax.set_title("Evolution de la norme - k=%.3f ; k'=%.3f" % (k1,k2) )
ax.set_xlabel("itération")
ax.set_ylabel("log(norme)")
ax.plot(X,Y1)
ax.plot([0,20000],[log(0.001),log(0.001)],color="crimson")
ax.legend()
plt.ylim([-10,12])
plt.savefig("log_normeg1.k10.k'01.png")
plt.show()



# Affichage figure
fig = plt.figure() # ouverture de la zone graphique
ax = fig.gca(projection='3d') 
x = np.arange(-5, 5, 0.1) # échelle x
y = np.arange(-5, 5, 0.1) # échelle y
x, y = np.meshgrid(x, y) # tracé de la grille

F= x**4 - x**3 - 20*x**2 + x + 1 + y**4 - y**3 - 20*y**2 + y + 1
surf = ax.plot_surface(x, y, F, rstride=1, zorder=1,alpha=0.6,cstride=1, linewidth=0, cmap=cm.PiYG, antialiased=False)
#ax.set_title("\nx0=(%d,%d), k=%4.3f, k'=%4.3f, tmax=%d :" %(x0[0],x0[1],k1,k2,tmax) )
ax.plot(res4[0][0], res4[0][1], g1(res4[0]),zorder=2,color="orange") #plot definition and options 
ax.scatter(res4[1][0],res4[1][1],g1(res4[1]), s=100, color="blue",zorder=3)
ax.scatter(x0[0],x0[0],g1(x0), s=100, color="red",zorder=4)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('g(x,y)')

fig.colorbar(surf, shrink=0.5, aspect=5)
#plt.savefig("fonctionf1.png")
plt.show()

'''
tmax=20000
# stats :
fichier = open("paramsgV2.txt", "a")
fichier.write("version\tk1\tk2\tDepart\tX\tY\tnbIter\n")
for k2 in [0.1]:
    for k1 in [10] :
        for i in range(100) :
            res=recuit2D([-4,-4],k1,k2,tmax)
            fichier.write("1\t"+str(k1)+"\t"+str(k2)+"\t-4\t"+str(res[1][0])+"\t"+str(res[1][1])+"\t"+str(res[2])+"\n")
            res=recuit2DV2([-4,-4],k1,k2,tmax)
            fichier.write("2\t"+str(k1)+"\t"+str(k2)+"\t-4\t"+str(res[1][0])+"\t"+str(res[1][1])+"\t"+str(res[2])+"\n")
            res=recuit2D([2,2],k1,k2,tmax)
            fichier.write("1\t"+str(k1)+"\t"+str(k2)+"\t2\t"+str(res[1][0])+"\t"+str(res[1][1])+"\t"+str(res[2])+"\n")
            res=recuit2DV2([2,2],k1,k2,tmax)
            fichier.write("2\t"+str(k1)+"\t"+str(k2)+"\t2\t"+str(res[1][0])+"\t"+str(res[1][1])+"\t"+str(res[2])+"\n")
            #res=recuit2D([0,0],k1,k2,tmax)
            #fichier.write("1\t"+str(k1)+"\t"+str(k2)+"\t0\t"+str(res[1][0])+"\t"+str(res[1][1])+"\t"+str(res[2])+"\n")
            #res=recuit2DV2([0,0],k1,k2,tmax)
            #fichier.write("2\t"+str(k1)+"\t"+str(k2)+"\t0\t"+str(res[1][0])+"\t"+str(res[1][1])+"\t"+str(res[2])+"\n")
    
fichier.close()
'''
