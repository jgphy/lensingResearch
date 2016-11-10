import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.misc import toimage
# import importlib
# importlib.import_module('mpl_toolkits.mplot3d').__path__

def surfacePlot(surface):
	dimensions=len(surface)
	X, Y = np.mgrid[:dimensions,:dimensions]

	fig = plt.figure()
	ax = fig.add_subplot(1,1,1, projection='3d')
	surf = ax.plot_surface(X, Y, surface, rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
	plt.show()

def imagePlot(image):
	toimage(image).show()
