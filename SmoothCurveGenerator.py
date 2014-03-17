import numpy as np
import random as rand
import scipy as scipy
from pylab import plot,show,hist

class SmoothCurveGenerator:
	def __init__(self, data1, data2):
		self.data1 = np.array(data1)
		self.data2 = np.array(data2)
		self.samp = self.hstackData()

	def getData1(self):
		return self.data1

	def getData2(self):
		return self.data2

	def getSamp(self):
		return self.samp

	def hstackData(self):
		#stacks things column wise
		return np.hstack([self.getData1(), self.getData2()])

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

	def generateKernelDensityEstimateSmoothFunction(self):
		# obtaining the pdf function (pointer)
		my_pdf = scipy.stats.gaussian_kde(self.samp)
		return my_pdf

	#TODO problem: having pdf as an input to functions is a problem because
	#some functions in scipy need the parameters explicity. 
	#like loc and scale. However, if that is all they need then it could be
	#the same interface loc and scale for all functions
	# def getPdfNormal(self, mean, std):
	# 	return scipy.stats.norm.pdf(I)

	def plotSmoothFunction_1D(self, pdf, lowerBound = -5, upperBound = 5, spacing = 100):
		#returns evenly spaced numbers over a specified interval
		x = np.linspace(lowerBound, upperBound, spacing) 
		plot(x, pdf(x), 'r') # distribution function
		hist(self.getSamp(), normed=1, alpha=.3) # histogram
		show()

	#Returns D(p||q) = E[log(p(x)/q(x))] = E[log(1/q(x))] - E[log(1/p(x))]
	def getKlDivergence(self, p_pdf, q_pdf):
		#TODO
		return None

	#Returns EMD(p,q)
	def getEMD(self, p_pdf, q_pdf):
		#TODO
		return None



#scg = SmoothCurveGenerator([1,2,3])
