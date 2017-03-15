import numpy as np
import math
import matplotlib.pyplot as plt

def distanceMap(mapSize,pixelSize):
	
	dMap=np.zeros((mapSize,mapSize))
	center=mapSize//2
	for i in range (0,mapSize):
		for j in range(0,mapSize):
			dMap[i,j]=math.sqrt((i-center)**2+(j-center)**2)
			dMap[i,j]=dMap[i,j]*pixelSize
	return(dMap)

def emptyArray(size):
	return(np.zeros((size,size)))

def addGap(surfaceMap,valueRange,metric):

	if metric== "mapValues":
		for i in range(0,len(surfaceMap)):
			for j in range(0,len(surfaceMap)):
				if (surfaceMap[i,j] >= valueRange[0]) and (surfaceMap[i,j] <= valueRange[1]):
					surfaceMap[i,j]=0
	if metric== "distanceValues":
		size=surfaceMap.shape
		dummy= distanceMap(size[0],1)
		for i in range(0,size[0]):
			for j in range(0,size[0]):
				if (dummy[i,j] >= valueRange[0]) and (dummy[i,j] <= valueRange[1]):
					surfaceMap[i,j]=0

	return(surfaceMap)

def invertedGap(surfaceMap,valueRange,metric):

	if metric== "mapValues":
		for i in range(0,len(surfaceMap)):
			for j in range(0,len(surfaceMap)):
				if (surfaceMap[i,j] <= valueRange[0]) or (surfaceMap[i,j] >= valueRange[1]):
					surfaceMap[i,j]=0
	if metric== "distanceValues":
		size=surfaceMap.shape
		dummy= distanceMap(size[0],1)
		for i in range(0,len(surfaceMap)):
			for j in range(0,len(surfaceMap)):
				if (dummy[i,j] <= valueRange[0]) or (dummy[i,j] >= valueRange[1]):
					surfaceMap[i,j]=0

	return(surfaceMap)


def line(start,end,nPoints):
	return(np.linspace(start,end,nPoints))

def info():
	print("distanceMap(mapSize= 'dimensions of map') : return a n x n array with distance values from the center.")
	print("Gap(surfaceMap,valueRange=[1,2],metric= mapValues or distanceValues): inserts a gap into surfaceMap")
	print("invertedGap(surfaceMap,valueRange[1,2], metric= mapValues or distanceValues: zeros everything not within valueRange")
	print("emptyArray(size): returns 2d array filled with zeros")