import numpy as np

class DataGenerator:
	def __init__(self, amount, number_of_groups, mean, std):
		self.amount = amount
		self.number_of_groups = number_of_groups
		self.mean = mean
		self.std = std

	def GenerateData(self):
		g_data = []
		for group_index in range(number_of_groups):
			data = self.generateDataPoint(amount, mean, std)
			g_data.append(data)
		return g_data

	def generateDataPoint(self, amount, mean, std):
		return np.random.normal(amount, mean, std)

number_of_groups = 10
amount = 3
mean = 1
std = 2
gen = DataGenerator(number_of_groups,amount,mean,std)
print gen.GenerateData()