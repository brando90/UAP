import numpy as np
import random as rand

# class Parameters:
# 	def __init__(self, mean, std):
# 		self.mean = mean
# 		self.std = std

# 	def getMean(self):
# 		return self.mean

# 	def getStd(self):
# 		return self.std

class DataGenerator:
	def __init__(self, number_of_groups, amountLower, amountUpper, meanLower, meanUpper, stdLower, stdUpper, seedAmount = 0, seedMean = 0, seedStd = 0):
		self.number_of_groups = number_of_groups
		self.amountsList = self.initListRandNumbers(amountLower, amountUpper, seedAmount)
		self.meansList = self.initListRandNumbers(meanLower, meanUpper, seedMean)
		self.stdsList = self.initListRandNumbers(stdLower, stdUpper, seedStd)

	def initListRandNumbers(self, lower, upper, seed = 0):
		l = []
		rand.seed(seed)
		for i in range(number_of_groups):
			val = rand.randint(lower, upper)
			l.append(val)
		return l

	def GenerateData(self):
		g_data = []
		for group_index in range(number_of_groups):
			currentMean = self.getAmountForGroup(group_index)
			currentStd = self.getStdForGroup(group_index)
			currentAmount = self.getAmountForGroup(group_index)
			data = self.generateDataPoint(currentAmount, currentMean, currentStd)
			g_data.append(data)
		return g_data

	def generateDataPoint(self, amount, mean, std):
		return np.random.normal(mean, std, amount)

	def getAmountForGroup(self, group_index):
		return self.amountsList[group_index]

	def getMeanForGroup(self, group_index):
		return self.meansList[group_index]

	def getStdForGroup(self, group_index):
		return self.stdsList[group_index]

number_of_groups = 10
amountLower = 0
amountUpper = 5
meanLower = 1
meanUpper = 3
stdLower = 1
stdUpper = 5
gen = DataGenerator(number_of_groups, amountLower, amountUpper, meanLower, meanUpper, stdLower, stdUpper)
print gen.GenerateData()