import numpy as np
import random as rand

class SmoothCurveGenerator:
	def __init__(self, dataList):
		self.dataList = np.array(dataList)

	def getDataList(self):
		return self.dataList

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


scg = SmoothCurveGenerator([1,2,3])
