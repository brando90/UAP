import numpy as np
import random as rand
import scipy as scipy
import pylab

class SmoothCurveGenerator:
	def __init__(self, data1, data2):
		self.data1 = data1
		self.data2 = data2

	def getData1(self):
		return self.data1

	def getData2(self):
		return self.data2

	#Estimate the mean for one array of data points
	#data = np.array([x1, ..., xn])
	def estimateSampleMean(self, data):
		n = data.shape[0]
		x_tot = np.sum(data)
		x_mean = x_tot/n
		return x_mean

	def estimateSampleVariance(self, data):
		n = data.shape[0]
		x_mean = self.estimateSampleMean(data)
		variance = np.sum( np.dot(data - x_mean, data - x_mean) )/n
		return variance

	def generateKernelDenistyEstimateSmoothFunction(self):
		#stacks things column wise
		samp = np.hstack([sampD1,sampD2])
		# obtaining the pdf function (pointer)
		my_pdf = scipy.stats.gaussian_kde(samp)
		return my_pdf

	def plotSmoothFunction_1D(self, pdf, lowerBound = -5, upperBound = 5, spacing = 100):
		#returns evenly spaced numbers over a specified interval
		x = np.linspace(lowerBound, upperBound, upperBound) 
		plot(x, pdf(x), 'r') # distribution function
		hist(samp, normed=1, alpha=.3) # histogram
		show()



#scg = SmoothCurveGenerator([1,2,3])
