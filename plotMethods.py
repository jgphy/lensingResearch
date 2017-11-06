import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.misc import toimage
from matplotlib import pylab as pl 

def surfacePlot (surface):
	dimensions=len(surface)
	X, Y = np.mgrid[:dimensions,:dimensions]
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1, projection='3d')
	surf = ax.plot_surface(X, Y, surface, rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
	# cset = ax.contourf(X, Y, surface, zdir='z',offset=-6,cmap=cm.cool)
	# plt.show()
	return(surf)

def contourPlot(data,dimensions):
	X, Y = np.mgrid[0:1:dimensions[0]*1j,0:1:dimensions[0]*1j]
	fig, axes = pl.subplots()
	c1 = axes.contourf(X, Y, data)
	pl.colorbar(c1, ax=axes);
	pl.show()



def imagePlot   (image):

	toimage(image).show()

def writeToFile (data):
	target=open('SBmap.txt','w')
	target.truncate()
	for i in range(0,len(data)):
		for j in range(0,len(data)):
			target.write(str(data[i,j]))
			if j < (len(data)):
				target.write("\n")

def plot        (data):
	plt.plot(data)
	plt.show()

def xyplot      (x,y):
	plt.plot(x,y)
	plt.show()


# def ds9():
	