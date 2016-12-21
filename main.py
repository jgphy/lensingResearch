import quasar
import structures
import plotMethods
import calculations
from constants import *
import numpy
def main():
	# SET UP STUFF===================================== 

	mapSize=300
	BHmass=2.0e8*solarMass
	spin='no spin'
	R_E= 1.81e+15
	isco=quasar.isco(BHmass,"no spin")
	# print(isco)
	lRpixelSize=R_E*10./10000.
 	hRpixelSize=R_E*1./10000. 
 	# print(lRpixelSize)
 	pixelSize= lRpixelSize #now given by whatever website
 	
	# mapsSize=calculations.figureOutMapSize(BHmass,spin,pixelSize,isco)


	#==================================================





	dMap=structures.distanceMap(mapSize,lRpixelSize)


	dMap=structures.addGap(dMap,[0,6*isco],'mapValues')
	plotMethods.surfacePlot(dMap)
	tMap=calculations.SStemperatureMap(dMap,isco,BHmass)
	# plotMethods.surfacePlot(tMap)
	intMap=calculations.IntensityMap(tMap,wBlue)
	# print(numpy.amax(tMap))
	intMap=calculations.log(intMap)
	# print(numpy.amax(intMap))
	# plotMethods.surfacePlot(intMap)

	# distances=calculations.log(distances)
	# plotMethods.surfacePlot(intMap)
	# gappedMap=structures.invertedGap(distances,[100,105],"distanceValues")
	# plotMethods.surfacePlot(gappedMap)

main()