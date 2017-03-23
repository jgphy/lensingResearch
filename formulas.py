from constants import *
import numpy as np
import math

#mostly from maoz chapter 4
def eddingtonLuminosity  ():
	
	Ledd=4.0*(pi)*c*G*mProton/sigT
	# print("L eddington [J/s]")
	# print(Ledd)
	return(Ledd)

def accretionRate        (r_isco,f): 
	M_dot=(f*8.0*(pi)*c*mProton*r_isco)/sigT
	# print("accretion rate aka M_dot [Kg/s]")
	# print(M_dot)
	return(M_dot)

def luminosity           (M,M_dot,radius):
	L=(.5*G*M*M_dot)/radius
	# print("luminosity [J/s]")
	print(L)
	return(L)

def SSDtemperature       (M,M_dot,radius):
	alpha=(G*M*M_dot)/(8.0*(pi)*sigma)
	alpha=alpha**(.25)
	# print("alpha-from Temperature formula")
	# print(alpha)
	T_radius = alpha  *  ((radius)**(-.75))
	# print("temperature at isco [K]")
	# print(T_radius)
	
	return(T_radius)

def SSDtemperature1D     (M,M_dot,radius):
	alpha=(G*M*M_dot)/(8.0*(pi)*sigma)
	alpha=alpha**(.25)	
	values=len(radius)
	values=int(values)
	out=np.zeros(values)	
	for i in range(values):
		if radius[i]!= 0:
			out[i]= alpha*((radius[i])**(-.75))

	return(out)

def SSDtemperature2D     (M,M_dot,radius):
	alpha=(G*M*M_dot)/(8.0*(pi)*sigma)
	alpha=alpha**(.25)
	
	dimension=(len(radius))
	# print(dimension)
	
	out=np.zeros((dimension,dimension))
	
	for i in range(dimension):
		for j in range(dimension):
			if radius[i,j] !=0:
				out[i,j]=alpha*(radius[i,j]**(-.75))
	return(out)

def planckFunction       (w,T_radius):
	
	dummy=2*h*(c**2.0)/(w**5.0)
	# print("dummy")
	# print(dummy)
	alpha=(h*c)/(w*KB*T_radius)
	# print("other alpha")
	# print(alpha)

	out=dummy/((e**(alpha))-1.0)
	# print("planckfunction [J/(s m^3)]")
	# print(out)
	return(out) #T_radius is a number

def planckFunction1D     (w,T_radius):
	
	dummy=2*h*(c**2.0)/(w**5.0)
	out=np.zeros(len(T_radius))
	
	for i in range(len(T_radius)):
		if T_radius[i] != 0:
			alpha=(h*c)/(w*KB*(T_radius[i]))
			out[i]=dummy/((e**(alpha))-1.0)

	return(out) #T_radius is 1*n array  

def planckFunction2D     (w,tempMap):#tempMap is n*n numpy array 
	dimension=(len(tempMap))
	# print("dimension")
	# print(dimension)
	out=np.zeros((dimension,dimension))
	dummy=2*h*(c**2.0)/(w**5.0)	

	for i in range(len(tempMap)):
		for j in range(len(tempMap)):
			if tempMap[i,j] !=0:
				alpha=(h*c)/(w*KB*(tempMap[i,j]))
				out[i,j]=dummy/((e**(alpha))-1.0)
	return(out)