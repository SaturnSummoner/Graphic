# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 18:06:38 2015

@author: juli6_000
"""

# "magnitud" de las estrellas cefeidas versus el logaritmo de su período
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
# store data in NumPy arrays 
y = np.array([-47,-189,-109,-199,-96,-120,-63,-32,26,514,-18,97,-23,186,18,136,37,180,229,-85,75,90,16,29,47,65,-55,31,63,60,71,52,274,112,45,19,25,64,83,37,28,46,43,69,-28,38,67,-38,89,-34,-17,56,150,23,-40,58,55,64,42,-28,-19,-48,-49,-73,-40,-19,-41,-48,-65,-12,-41,-32,-44,-39,-39,-42,30,-41,-206,-114,-164,-228,-69,-94,-128,-255])
x = np.array([29,-3,58,8,-58,-145,-88,40,23,-23,63,70,96,34,41,20,134,42,191,148,125,86,159,359,191,188,156,109,235,148,40,106,82,487,106,150,157,364,428,261,320,524,244,33,216,500,375,105,290,269,76,207,471,516,452,296,579,319,368,142,318,450,395,243,282,181,209,337,305,80,177,274,153,121,73,414,105,90,376,180,192,245,49,70,101,70])

plt.scatter(x,y, c=y, s=30, alpha=0.8,cmap=plt.cm.gist_rainbow, label='Globular Clusters')
plt.xlabel(r'$R cos \beta cos(\lambda -325°)$')
plt.ylabel(r'$R sin \beta$')
plt.title('SISTEMA COMPLETO DE CUMULOS GLOBULARES EN UN PLANO PERPENDICULAR A LA GALAXIA',fontsize=8)

x1=[0]
y1=[0]
plt.scatter(x1,y1, s=100, marker='x',linewidths=4, label='SOL', c='black')

l = plt.axhline(y=0, xmin=0, xmax=600, c='black')

p = plt.axhspan(-17.5, 17.5, facecolor='blue', alpha=0.3,)

a=np.average(x) 
print (a)
b=np.average(y) 
print (b)
plt.scatter(a,b, s=100, marker='+',linewidths=4, label='Promedio', c='red')

#distancia del centro del grupo de cumulos globulares al sol
dist=a-x1
print (dist)
plt.text(-140,300, 'Distancia del centro de los cumulos al sol 19Kpc', fontsize=8)


#Desviacion standard
stdevx=np.std(x)
print (stdevx)
stdevy=np.std(y)
print (stdevy)

#diametro del grupo de cumulos globulares 
maxi=np.max(y)
maximo= maxi+stdevy
mini=np.min(y)
minimo=mini+stdevy
print (maximo)
print (minimo)
minimoabs=np.abs(minimo)
diame=minimoabs+maximo
diametro=diame/10
print (diametro)
pto1=([-150,630])
pto2=([0,0])
plt.axvline(x=-150, ymin=-300, ymax =600 , linewidth=2, color='k')
plt.axvline(x=630, ymin=-300, ymax =600 , linewidth=2, color='k')
plt.text(-140,350, 'Diametro del grupo de cumulos globulares 77 Kpc',fontsize=8)

# show plot 
plt.plot()
plt.legend(loc=1, prop={'size':9})
pyplot.savefig("output.png")


