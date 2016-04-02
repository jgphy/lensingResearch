import numpy as np
import math
import matplotlib.pyplot as plt

def distanceMap(mapSize):
	dmap=np.zeros((mapSize,mapSize))
	center=mapSize//2
	for i in range (0,mapSize):
		for j in range(0,mapSize):
			a[i,j]=math.sqrt((i-center)**2+(j-center)**2)

	dmap=np.array(dmap)
	return(dmap)


def emptyArray(size):
	return(np.zeros(size,size))

def Gap(surfaceMap,valueRange,metric):

	if metric== "mapValues":
		for i in surfaceMap:
			if (surfaceMap[i] >= valueRange[0]) or (surfaceMap[i] <= valueRange[1]):
				surfaceMap[i]=0
	if metric== "distanceValues":
		size=surfaceMap.shape
		dummy= distanceMap(size[0])
		for i in dummy:
			if (dummy[i] >= valueRange[0]) or (dummy[i] <= valueRange[1]):
				surfaceMap[i]=0

	return(surfaceMap)

def invertedGap(surfaceMap,valueRange,metric):

	if metric== "mapValues":
		for i in surfaceMap:
			if (surfaceMap[i] <= valueRange[0]) or (surfaceMap[i] >= valueRange[1]):
				surfaceMap[i]=0
	if metric== "distanceValues":
		size=surfaceMap.shape
		dummy= distanceMap(size[0])
		for i in dummy:
			if (dummy[i] <= valueRange[0]) or (dummy[i] >= valueRange[1]):
				surfaceMap[i]=0

	return(surfaceMap)


def info():
	print("distanceMap(mapSize= 'dimensions of map') : return a n x n array with distance values from the center.")
	print("Gap(surfaceMap,valueRange=[1,2],metric= mapValues or distanceValues): inserts a gap into surfaceMap")
