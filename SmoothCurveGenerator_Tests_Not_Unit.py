import SmoothCurveGenerator as scg
import numpy as np
import scipy as scipy
from scipy.stats import norm
import pylab

#The tests in this file will not throw any errors if they don't pass.
#they are more qualitative and shows plots if you want to asses the library.

class PlotDiagramTests:
	def __init__(self, mean, std, size_sample_data = 300):
		#generate data with mean loc and std scale
		#generate 300 data points with dimension 1
		#the sample data matrix is of size (300,1)
		self.sampD1 = list(scipy.stats.norm.rvs(loc=mean,scale=std,size=size_sample_data))
		self.sampD2 = list(scipy.stats.norm.rvs(loc=mean,scale=std,size=size_sample_data))

	def KSE_Simple_Normal_Test(self):
		sampD1 = list(self.sampD1)
		sampD2 = list(self.sampD2)

		gen = scg.SmoothCurveGenerator(sampD1, sampD2)
		pdf = gen.generateKernelDenistyEstimateSmoothFunction()
		gen.plotSmoothFunction_1D(pdf)


test1 = PlotDiagramTests(-1.0, 1, 300)
test1.KSE_Simple_Normal_Test()
