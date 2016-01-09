import math
def isco(BHmass,spin):
	G=6.67384e-11 			#m^3 kg^-1 s^-2
	c=3.0e8		  			#m/s
	solarMass=1.98855e30 	#kg
	BHmass=BHmass*solarMass

	if spin == "prograde":
		factor=1.0
	if spin == "no spin":
		factor=6.0
	if spin == "retrograde":
		factor=9.0

	gravitationalRadius=(2.0*G*BHmass)/(c**2)
	isco=factor*gravitationalRadius
	
	return(isco)



def gravRadius(BHmass):
	G=6.67384e-11 	#m^3 kg^-1 s^-2
	c=3.0e8		  	#m/s
	solarMass=1.98855e30 	#kg
	BHmass=BHmass*solarMass
	radius=(2.0*G*BHmass)/(c**2)

	
	return(radius)


def mass(isco,spin):
	G=6.67384e-11 	#m^3 kg^-1 s^-2
	c=3.0e8		  	#m/s
	if spin == "prograde":
		factor=1.0
	if spin == "no spin":
		factor=6.0
	if spin == "retrograde":
		factor=9.0

	BHmass=(isco*(c**2))/(factor*G)

	return(BHmass)

def acrretionRate(BHmass,ratio,isco):
	thing=0
	mProton=1.67262178e-27                                  #mass of proton                     : kilograms
	sigT=6.65e-29                                           #Thompson scattering crosssection   :m^2
	G=6.673e-11                                             #Gravitatinal constant              : m^3 kg^-1 s^-2
	sigma=5.6703732e-8                                      #Stefan-Boltzmann constant          : W m^-2 K^-4
	solarMass=1.98855e30 									#solar mass 						:kg
	BHmass=BHmass*solarMass
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



