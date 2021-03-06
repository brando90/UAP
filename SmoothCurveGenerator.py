import numpy as np
import random as rand
import scipy as scipy
from scipy import stats
from pylab import plot,show,hist
import math as math

#CONSTANTS
INFINITY = float("inf")
MINUS_INFINITY = float("-inf")

class SmoothCurveGenerator:
#class SmoothCurveGenerator(stats.rv_continuous):
	def __init__(self, data1, data2):
		self.data1 = np.array(data1)
		self.data2 = np.array(data2)
		self.samp = self.hstackData()
		# self.a = float("-inf")
		# self.b = float("inf")
		# self.numargs = 0

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

	# def setPdf(self, input_pdf):
	# 	self.pdf = input_pdf

	# def _pdf(self, x):
	# 	return self.pdf(x)

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

	#computes expected value
	#return sum^{ub}_{x = lb}{pdf(x) * fn(x)}
	def expect(self, pdf, fn=None, lb=None, ub=None):
		#this term is f(x) * x that will be integrated to get expectation
		if fn == None:
			fn = lambda x: x
		if lb == None:
			lb = MINUS_INFINITY
		if ub == None:
			ub = INFINITY
		def summationTermInExpectation(x):
			return pdf(x) * fn(x)
		return scipy.integrate.quad(summationTermInExpectation, lb, ub)

#expect(func=None, args=(), loc=0, scale=1, lb=None, ub=None,

	def assignEmptyBounds(self, lb, ub):
		if lb == None:
			lb = MINUS_INFINITY
		if ub == None:
			ub = INFINITY
		return (lb, ub)

	#Total Variation
	def getTotalVariation(self, p_pdf, q_pdf, lb=None, ub=None):
		(lb, ub) = self.assignEmptyBounds(lb, ub)
		def summationTermInExpectation(x):
			return math.fabs(p_pdf(x) - q_pdf(x))
		return scipy.integrate.quad(summationTermInExpectation, lb, ub)

	#Returns D(p||q) = E[log(p(x)/q(x))] = E[log(1/q(x))] - E[log(1/p(x))]
	def getKlDivergence(self, p_pdf, q_pdf, lb=None, ub=None):
		(lb, ub) = self.assignEmptyBounds(lb, ub)
		def information_p_pdf(x):
			if p_pdf(x) == 0:
				return 0.0
			#return math.log(1.0/p_pdf(x), 2)
			return -1 * math.log(p_pdf(x), 2)
		def information_q_pdf(x):
			if q_pdf(x) == 0:
				return 0.0
			#return math.log(1.0/q_pdf(x), 2)
			return -1 * math.log(q_pdf(x), 2)
		e_q_x, error_q = self.expect(p_pdf, information_q_pdf, lb, ub)
		e_p_x, error_p = self.expect(p_pdf, information_p_pdf, lb, ub)
		divergence = e_q_x - e_p_x
		return divergence

	def SquaredHellingerDistance(self, p_pdf, q_pdf, lb=None, ub=None):
		(lb, ub) = self.assignEmptyBounds(lb, ub)
		def summationTermInExpectation(x):
			return 0.5 * math.pow(math.sqrt(p_pdf(x)) - math.sqrt(q_pdf(x)),2)
		return scipy.integrate.quad(summationTermInExpectation, lb, ub) 

	def EngineersMetric(self, p_pdf, q_pdf, lb=None, ub=None):
		(lb, ub) = self.assignEmptyBounds(lb, ub)
		e_p, error_p = scipy.integrate.quad(p_pdf, lb, ub)
		e_q, error_q= scipy.integrate.quad(q_pdf, lb, ub)
		return math.fabs(e_p - e_q)

	def LpMetric(self, p_pdf, q_pdf, p_exponent, lb=None, ub=None):
		(lb, ub) = self.assignEmptyBounds(lb, ub)
		p = float(p_exponent)
		def summationTermInExpectation(x):
			return math.pow(math.fabs(p_pdf(x) - q_pdf(x)), float(p))
		pth_distance, error = scipy.integrate.quad(summationTermInExpectation, lb, ub)
		return math.pow(pth_distance, 1.0/float(p))



#scg = SmoothCurveGenerator([1,2,3])
