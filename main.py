from 	constants import *
import 	calculations
import 	formulas
import 	numpy as np
import 	plotMethods
import matplotlib.pyplot as plt
import 	quasar
import 	structures

def main():
#############################################	SET UP STUFF			############################################
	
	quasarName="PG1115+080"
	BHmass=1.0e9*solarMass
	spin='no spin'
	isco=quasar.isco(BHmass,spin)
	M_dot=formulas.accretionRate(isco,ratio) #need to replace .1 with the value from constants.py	
	#Map data
	mapSize=500
	R_E= 3.62e14
	lRpixelSize=R_E*25./10000.
 	pixelSize= lRpixelSize #now given by whatever website

#############################################	CALCULATIONS			############################################


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

#############################################	ONE DIMENSIONAL CHECK	###################################

	radii=structures.line(isco*(-10),isco*10,1000)
	radius=abs(radii)
	
	for i in range(len(radius)):
		if abs(radius[i]) <= isco:
			radius[i]=0

	
	print("Black hole mass [Kg]:")
	print(BHmass)
	print("")
	
	print("ISCO [m]:")
	print(isco)
	print("")
	
	print("accretion rate [Kg/s]")
	print(M_dot)
	print("")
	
	print("eddington luminosity:")
	print(formulas.eddingtonLuminosity())
	print("")
	
	print("luminosity from ISCO [J/s]")
	print(formulas.luminosity(BHmass,M_dot,isco))
	print("")
	
	print("temperature at ISCO [K]")
	T_isco=formulas.SSDtemperature(BHmass,M_dot,isco)
	print(T_isco)
	print("")
	
	print("output of planck function at ISCO lambda=479.0e-9 m ")
	pOut0=formulas.planckFunction(wBlue,T_isco)
	print(pOut0)
	print("")

	print("NEXT CHECK:")
	temperatures=formulas.SSDtemperature1D(BHmass,M_dot,radius)
	print("first few values from SSD temperature function")	
	print(temperatures[0:4])
	print("")
	print("check that 1D temp function agrees with the single value function, next two outputs should agree:")
	t=np.array([isco])
	t2=formulas.SSDtemperature1D(BHmass,M_dot,t)	
	print("temperature at ISCO:")
	print(t2[0])
	print(T_isco)
	print("")

	print("first few values of planck Function")
	pOut=formulas.planckFunction1D(wBlue,temperatures)
	print(pOut[0:4])
	print("")

	print("Check that 1D planck function agrees with the single value function, next two ouputs should agree:")
	pOUt2=formulas.planckFunction1D(wBlue,t2)
	print(pOUt2[0])
	print(pOut0)
	print("")

	print("Done with first part of check")
	print("")

#############################################	TWO DIMENSIONAL CHECK	###################################
	
	dMap	=	structures.distanceMap(mapSize,lRpixelSize)
	dMap	=	structures.addGap(dMap,[0,6*isco],'mapValues')

	tMap	=	calculations.SStemperatureMap(dMap,isco,BHmass)
	tMap2	= 	formulas.SSDtemperature2D(BHmass,M_dot,dMap)

	print("check if original and new two-dimensional formulas for temperatures works: next two outputs should agree")
	print(tMap	[1,0:4])
	print(tMap2	[1,0:4])

	print("Check if 2D temperature formulas agree at ISCO, next two outputs should agree:")

	testTemp=np.zeros((2,2))
	testTemp[0,0]=isco
	testTemp=formulas.SSDtemperature2D(BHmass,M_dot,testTemp)
	print(testTemp[0,0])
	print(T_isco)



	planckOut1=calculations.IntensityMap(tMap,wBlue)
	planckOut2=calculations.IntensityMap(tMap2,wBlue)
	planckOut3=formulas.planckFunction2D(wBlue,tMap)
	planckOut4=formulas.planckFunction2D(wBlue,tMap2)
	print("testing out planck law formulas, old and new, next four ouputs should agree:")
	print(planckOut1[1,0:4])
	print(planckOut2[1,0:4])
	print(planckOut3[1,0:4])
	print(planckOut4[1,0:4])

	test2=np.zeros((2,2))
	test2[0,0]=T_isco

	# planckOut1=calculations.IntensityMap(test2,wBlue)
	# planckOut2=formulas.planckFunction2D(wBlue,test2)
	# print("checking output of planck function at ISCO, next three outputs should agree:")
	# print(pOut0)
	# print(planckOut1[0,0])
	# print(planckOut2[0,0])

#############################################	PLOTS					###################################
	
	# surface1=plotMethods.surfacePlot(planckOut1)
	# surface2=plotMethods.surfacePlot(planckOut3)
	# plt.show()

	# plotMethods.plot(radius)
	# plotMethods.xyplot(radii,pOut)


main()