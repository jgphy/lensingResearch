import numpy as np

def mapReader(filename,dimension):
	txt= open(filename)
	mapArray=txt.read()
	mapArray=mapArray.split("\n")

	print(mapArray[-1])
	if mapArray[-1] == '':
		mapArray.pop(-1)
	for i in  range(4,len(mapArray)):
		mapArray[i]=float(mapArray[i])

	dummy=mapArray[4:] #the first four lines give information regarding the magnification map
	mapArray=np.reshape(dummy,(dimension,dimension))
	return(mapArray)