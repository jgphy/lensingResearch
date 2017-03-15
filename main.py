import quasar
import structures
import plotMethods
import calculations
from constants import *
import numpy
def main():
	# SET UP STUFF===================================== 
	quasarName="PG1115+080"
	mapSize=500
	BHmass=1.0e9*solarMass
	print(BHmass)
	spin='no spin'
	R_E= 3.62e14
	isco=quasar.isco(BHmass,"no spin")
	print(isco)
	lRpixelSize=R_E*25./10000.
 	hRpixelSize=R_E*1./10000.
 	print(lRpixelSize/(3.0e8)) 
 	print(lRpixelSize)
 	pixelSize= lRpixelSize #now given by whatever website
 	print(isco/pixelSize)
 	
	# # mapsSize=calculations.figureOutMapSize(BHmass,spin,pixelSize,isco)
	# # print(mapSize)

	# #==================================================

	# dMap=structures.distanceMap(mapSize,lRpixelSize)


	# dMap=structures.addGap(dMap,[0,6*isco],'mapValues')
	# # plotMethods.surfacePlot(dMap)
	# tMap=calculations.SStemperatureMap(dMap,isco,BHmass)
	# # plotMethods.surfacePlot(tMap)
	# intMap=calculations.IntensityMap(tMap,wBlue)
	# plotMethods.surfacePlot(intMap)
	# radius=dMap[10,450]
	# print(radius)






	# # normalizedMap=calculations.normalize(intMap)
	# # print(normalizedMap[0,0:10])
	# # print(normalizedMap[0:10,0])
	# # plotMethods.surfacePlot(normalizedMap)
	# # plotMethods.writeToFile(normalizedMap)
	# # # plotMethods.surfacePlot(intMap)

main()