#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 17:52:16 2018
TD4 - Partie 2
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

# --- PARAMETRES ---
L=50
n=10
k=0.01
tmax=10000

def couleurs(n) :
	cols=[]
	for i in range(n):
		a=np.random.random()
		b=np.random.random()
		c=np.random.random()
		cols.append((a,b,c))
	return cols
	
def aff(villes,trajet,L):
	colors=couleurs(len(villes))
	fig = plt.figure() 
	ax = fig.gca() 
	ax.set_title('')
	ax.set_xlabel('x')
	ax.set_ylabel('y')
	ax.plot([0,L],[0,0],color="crimson",zorder=1)
	ax.plot([0,L],[L,L],color="crimson",zorder=1)
	ax.plot([0,0],[0,L],color="crimson",zorder=1)
	ax.plot([L,L],[0,L],color="crimson",zorder=1)
	for i in range(len(villes)-1) :
		ax.scatter(villes[trajet[i]][0],villes[trajet[i]][1],zorder=2,color=colors[i],s=100)
		ax.plot([villes[trajet[i]][0],villes[trajet[i+1]][0]],[villes[trajet[i]][1],villes[trajet[i+1]][1]],color=colors[i],zorder=1)
	ax.scatter(villes[trajet[i+1]][0],villes[trajet[i+1]][1],zorder=2,color=colors[i+1],s=100)
	#plt.savefig("fonctionf1.png")
	plt.show()
	

################################
## 1 : Générateur de villes   ##
################################
print("\n *** 1 : Générateur de villes  ***")

print("Dimention de la carte : %d m" %L)
print("Nombre de villes : %d m" %n)

'''
Génère n villes aux positions aléatoires dans un carré de LxL
'''
def geneVilles(n,L):
	return L*np.random.rand(n,2)

villes=geneVilles(n,L)
print("Position des villes : ")
print(villes)


################################
## 2 : Distance Euclidienne   ##
################################
print("\n *** 2: Distance Euclidienne ***")

'''
renvoie la distance euclidienne séparant 2 villes
'''
def dist(ville1,ville2):
	return sqrt((ville2[0]-ville1[0])**2 + (ville2[1]-ville1[1])**2)
	
'''
Pour une liste de n villes (liste des positions) donné
et un trajet (ordre de parcours des n villes) :
renvoie la distance parcourue
'''
def distTotale(villes,trajet):
	total=0.0
	for i in range(len(trajet)-1) :
		total+=dist(villes[trajet[i]],villes[trajet[i+1]])
	return total

trajet=np.random.permutation(n)
d=distTotale(villes,trajet)
print("Trajet : ")
print(trajet)
print("Longueur du trajet : %.2f m" % d)

#aff(villes,trajet,L)

################################
## 3: Permutation aléatoire   ##
################################
print("\n *** 3: Permutation aléatoire ***")

def permute(array) :
	n=len(array)
	i1=np.random.randint(n)
	i2=np.random.randint(n)
	(array[i1],array[i2])=(array[i2],array[i1])
	return array

print("Permutation aléatoire de deux éléments du trajet : ")
trajet=permute(trajet)
print(trajet)

#########################################
## 4: Implémentation de l'algorithme   ##
#########################################
print("\n *** 4: Implémentation de l'algorithme ***")

def recuit(villes,trajetInit,k,tmax) :
    #init
    T=1.0
    X=[]
    D=[]
    X.append(trajetInit)
    D.append(distTotale(villes,trajetInit))
    t=1
    while(t<tmax):
		s=0.0
		for i in range(5):
			new=permute(X[-1])
			s+=(distTotale(villes,new)-distTotale(villes,X[-1]))
		De=s/5.0
		#deplacement
		new=permute(X[-1])
		#eval
		if (distTotale(villes,new) <= D[-1]) :
			X.append(new)
			D.append(distTotale(villes,new))
		else :
			test=np.random.random()
			if test<(k*exp(-De/(1000.0*T))) :
				X.append(new)
				D.append(distTotale(villes,new))                
			else : 
				X.append(X[-1])
				D.append(D[-1])
			'''
			X.append(X[-1])
			D.append(D[-1])
			'''
		#diminution
		t+=1
		T=1.0/(log(t))
		
    return (X[-1],distTotale(villes,X[-1]),t,X,D)

tmps1=time.clock()
res1=recuit(villes,trajet,k,tmax)
tmps2=time.clock()
print("\n--- Trajet optimal : ")
print(res1[0])
print("Longueur du trajet : %.2f m" % res1[1])
print("Nombre d'itérations : %d" % res1[2])
print ("Temps d'execution : %s secondes --- " %(tmps2-tmps1))

aff(villes,res1[0],L)

# Evolution de la distance 
	
X=np.arange(0,tmax,1)

fig = plt.figure() 
ax = fig.gca() 
ax.set_title("Evolution de la distance")
ax.set_xlabel('iteration')
ax.set_ylabel('distance')
ax.plot(X,res1[4],color="teal")
#plt.savefig("fonctionf1.png")
plt.show()

