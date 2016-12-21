import math
from constants import * 

def isco(BHmass,spin):
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

def gravRadius(BHmass):
	# BHmass=BHmass*solarMass
	radius=(2.0*G*BHmass)/(c**2)
	
	return(radius)

def mass(isco,spin):
	if spin == "prograde":
		factor=1.0
	if spin == "no spin":
		factor=6.0
	if spin == "retrograde":
		factor=9.0

	BHmass=(isco*(c**2))/(factor*G)

	return(BHmass)

def acrretionRate(BHmass,ratio,isco):
	# BHmass=BHmass*solarMass
	Mdot=(ratio)*((8.0*math.pi*3.0e8*mProton*isco)/sigT) 		  #accretion rate               : kg/s

	return(Mdot)

def info():

	print("function: isco(BHmass: solar masses, spin= 'prograde' or'retrograde' or 'no spin') returns isco size in meters. ")
	print("")
	print("function: gravRadius(BHmass: solar masses) returns gravitational radius. ")
	print("")
	print("function: mass(isco in meters,spin='prograde' or 'retrograde' or 'no spin') returns mass given isco im meters and spin")
	print("")
	print("function: accretionRate(BHmass: solar masses, Eddington ratio,isco: meters) returns accretion rate")
	print("")