import quasar
import structures
import plotMethods
import calculations
import formulas
from constants import *
import numpy








def main():
	##################################SET UP STUFF############################ 
	quasarName="PG1115+080"
	mapSize=500
	BHmass=1.0e9*solarMass
	spin='no spin'
	R_E= 3.62e14
	isco=quasar.isco(BHmass,"no spin")
	lRpixelSize=R_E*25./10000.
 	hRpixelSize=R_E*1./10000.
 	pixelSize= lRpixelSize #now given by whatever website

 	

#############################################CALCULATIONS############################################


	# # mapsSize=calculations.figureOutMapSize(BHmass,spin,pixelSize,isco)
	# # print(mapSize)

	# #==================================================

	# dMap=structures.distanceMap(mapSize,lRpixelSize)


	# dMap=structures.addGap(dMap,[0,6*isco],'mapValues')
	# # plotMethods.surfacePlot(dMap)
	# tMap=calculations.SStemperatureMap(dMap,isco,BHmass)
	# #plotMethods.surfacePlot(tMap)
	# intMap=calculations.IntensityMap(tMap,wBlue)
	# plotMethods.surfacePlot(intMap)
	# radius=dMap[10,450]
	# print(radius)




















######################################ONE DIMENSIONAL CHECK################################################
	print("BHmass [Kg]")
	print(BHmass)
	print("ISCO [m]")
	print(isco)


	radii=structures.line(isco*(-10),isco*10,1000)
	radius=abs(radii)
	accretion=formulas.accretionRate(isco,.1)

	formulas.eddingtonLuminosity()

	#check Luminosity at isco??
	print("luminosity at ISCO [J/s]")
	formulas.luminosity(BHmass,accretion,isco)
	#check Temperature at the isco
	T_isco=formulas.SSDtemperature(BHmass,accretion,isco)
	print("temperature at ISCO [K]")
	print(T_isco)

	print("output of planck function at ISCO lambda=479.0e-9 m ")
	formulas.planckFunction(wBlue,T_isco)
	for i in range(len(radius)):
		if abs(radius[i]) <= isco:
			radius[i]=0


	temperatures=formulas.SSDtemperature1D(BHmass,accretion,radius)
	# plotMethods.plot(radius)
	# plotMethods.xyplot(radii,temperatures)




main()