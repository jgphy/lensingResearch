import quasar
import structures
import plotMethods
import calculations
import constants


def main():
	distances=structures.distanceMap(300,1)
	# plotMethods.surfacePlot(distances)
	gappedMap=structures.invertedGap(distances,[100,105],"distanceValues")
	plotMethods.surfacePlot(gappedMap)


main()