
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.misc import toimage

def surfacePlot(Surface):
	dimensions=surface.shape

	X = np.arange(-dimensions[0], dimensions[0], 1)
	Y = np.arange(-dimensions[0], dimensions[0], 1)
	X, Y = np.meshgrid(X, Y)

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	surf = ax.plot_surface(X, Y, a, rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
	plt.show()

def imagePlot(image):
	toimage(mapArray).show()
