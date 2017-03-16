import math
from constants import * 

def isco			(BHmass,spin):
	# BHmass=BHmass*solarMass

	if spin == "prograde":
		factor=1.0
	if spin == "no spin":
		factor=6.0
	if spin == "retrograde":
		factor=9.0

	gravitationalRadius=(G*BHmass)/(c**2)
	isco=factor*gravitationalRadius
	
	return(isco)

def gravRadius		(BHmass):
	# BHmass=BHmass*solarMass
	radius=(2.0*G*BHmass)/(c**2)
	
	return(radius)

def mass			(isco,spin):
	if spin == "prograde":
		factor=1.0
	if spin == "no spin":
		factor=6.0
	if spin == "retrograde":
		factor=9.0

	BHmass=(isco*(c**2))/(factor*G)

	return(BHmass)

def accretionRate	(BHmass,ratio,isco):
	# BHmass=BHmass*solarMass
	Mdot=(ratio)*((8.0*math.pi*3.0e8*mProton*isco)/sigT) 		  #accretion rate               : kg/s

	return(Mdot)