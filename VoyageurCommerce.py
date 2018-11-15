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

def aff(villes,trajet,L):
	colors=["purple","blue","green","orange","red"]
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

L=10
n=5
print("Dimention du carré :",L)
print("Nombre de villes :",n)

'''
Génère n villes aux positions aléatoires dans un carré de LxL
'''
def geneVilles(n,L):
	villes=[]
	for ville in range(n):
		villes.append(np.random.randint(L+1,size=2))
	return villes

villes=geneVilles(n,L)
print("Position des villes : ",villes)


################################
## 1 : Distance Euclidienne   ##
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
print("trajet : ",trajet)
print("longueur du trajet : %.2f m" % d)

aff(villes,trajet,L)
