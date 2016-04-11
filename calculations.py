from constants import *
import numpy as np 
import math
import structures
def temperatureMap(distMap,isco):
	Mdot=ratio*8.0*math.pi*c*mProton*isco/sigT #kg/s based on black hole with no spin 
	A=(G*BHmass*Mdot)/(8.0*math.pi*sigma)
	A=A**(.25)
	dimension=math.sqrt(len(distMap))
	tempMap=structures.distanceMap(dimension)
	for i in  range(dimension-1):
		if map[i]!=0:
			temp[i]=A*(distMap[i]**(-3.0/4.0))
	


def IntensityMap(tempMap,wValue):
	intensity=np.zeros((mapSize,mapSize))
	for i in range(len(tempMap)-1):
		if tempMap[i] !=0:
			exp=(e**(h*c))/(KB*wValue*tempMap[i])
			dummy=(wValue**5)*(exp-1)
			intensity[i]=dummy


def normalize(mapArray):
	tots=sum(mapArray)
	return(mapArray/tots)


def isolateRegion(maparray,bottomleft,valueRange):
	return(maparray[bottomleft[0]:bottomleft[0]+valueRange,bottomleft[1]:bottomleft[1]+valueRange])

def zoom(mapArray,location,dimension):
	return(maparray[location[0]-(dimension/2):location[0]-1+(dimension/2),location[1]-(dimension/2):location[1]-1 + (dimension/2)])





def convolve(magMap,intensityMap,regionData):
# example of regionData variable
# regionData=[bottomleftCorner,[xrange,yrange]]
	mapRegion=isolateRegion(magMap,regionData[0],regionData[1])
	IMsize=np.shape(intensityMap)
	i=0
	points=list()
	while i < IMsize[2]:
		dummy=mapRegion[0+i:IMsize[2]+i,0:]
		dummy=intensityMap*dummy
		points.append(sum(dummy))

	return(points)

def where(mapArray,valueRange):
	mapSize=np.shape(mapArray)
	values=list()
	for in range(0,mapSize-1):
		if mapArray[i] >= valueRange[0] and i<= valueRange[1]:
			values.append(i)

	return(values)


def xycoordinate(map,point):
	IMsize=np.shape(map)
	xpoint=point%IMsize[0]
	ypoint=point//IMsize[0]
	return([xpoint,ypoint])


def tilt(magMap,degree):
	theta=degree*math.pi/180
	factor=math.cos(theta)
	mapSize=np.shape(magMap)
	mapSize=mapSize[1]
	a=mapSize/2
	b=mapSize*factor/2
	center=mapSize/2
	array=distanceMap(mapSize)
	newarray=emptyArray(mapSize)
	# need to make the points of the "circle" that would go away when the source is tilted by some degree
	# look at tiltimage in old lensingResearch directory
	# for i in range(0,mapSize[0]):



	return()



























