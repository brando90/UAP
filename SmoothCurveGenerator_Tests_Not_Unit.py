import SmoothCurveGenerator as scg
import numpy as np
import scipy as scipy
from scipy.stats import norm
import pylab
from abc import ABCMeta, abstractmethod

#The tests in this file will not throw any errors if they don't pass.
#they are more qualitative and shows plots if you want to asses the library.

class PlotDiagramTests:
	__metaclass__ = ABCMeta

	@classmethod
	def KSE_Simple_Normal_Test_Plot(self):
		print "KSE_Simple_Normal_Test Test"
		mean1 = -1.0
		std1 = 1
		mean2 = 2.0
		std2 = 0.5
		size_sample_data = 300
		#generate data with mean loc and std scale
		#generate 300 data points with dimension 1
		#the sample data matrix is of size (300,1)
		sampD1 = list(scipy.stats.norm.rvs(loc=mean1,scale=std1,size=size_sample_data))
		sampD2 = list(scipy.stats.norm.rvs(loc=mean2,scale=std2,size=size_sample_data))

		gen = scg.SmoothCurveGenerator(sampD1, sampD2)
		kde_pdf = gen.generateKernelDensityEstimateSmoothFunction()
		gen.plotSmoothFunction_1D(kd_pdf)

	@classmethod
	def Normal_Simple_Test_Plot(self):
		mean1 = -1.0
		std1 = 1
		mean2 = 2.0
		std2 = 0.5
		size_sample_data = 300
		#generate data with mean loc and std scale
		#generate 300 data points with dimension 1
		#the sample data matrix is of size (300,1)
		sampD1 = list(scipy.stats.norm.rvs(loc=mean1,scale=std1,size=size_sample_data))
		sampD2 = list(scipy.stats.norm.rvs(loc=mean2,scale=std2,size=size_sample_data))

		gen = scg.SmoothCurveGenerator(sampD1, sampD2)

PlotDiagramTests.KSE_Simple_Normal_Test_Plot()
