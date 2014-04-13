import SmoothCurveGenerator as scg
import unittest
import numpy as np
import scipy as scipy

#every test will start with test_{some description}_{name of function from package being tested}

#Unit tests for SmoothCurveGenerator
class TestSmoothCurveGenerator(unittest.TestCase):
	def setUp(self):
		self.simpleDataPoints = [2,4]

	def test_simple_estimateSampleMean(self):
		scgen = scg.SmoothCurveGenerator([2,6], [])
		x_mean = scgen.estimateSampleMean(scgen.getData1())
		actual_mean =  4
		self.assertEqual(x_mean, actual_mean)

	def test_simple_estimateSampleMean(self):
		scgen = scg.SmoothCurveGenerator([2,6], [])
		x_var = scgen.estimateSampleVariance(scgen.getData1())
		actual_var =  4
		self.assertEqual(x_var, actual_var)

	def test_total_variation(self):
		mean1 = 0.0
		std1 = 1
		size_sample_data = 500
		#generate data with mean loc and std scale
		#generate 300 data points with dimension 1
		#the sample data matrix is of size (300,1)
		sampD1 = list(scipy.stats.norm.rvs(loc=mean1,scale=std1,size=size_sample_data))
		#sampD2 = list(scipy.stats.norm.rvs(loc=mean2,scale=std2,size=size_sample_data))

		gen = scg.SmoothCurveGenerator(sampD1, [])
		kde_pdf = gen.generateKernelDensityEstimateSmoothFunction()
		print "expect: ", gen.expect(kde_pdf)
		print "getTotalVariation: ", gen.getTotalVariation(kde_pdf, kde_pdf)
		print "SquaredHellingerDistance: ", gen.SquaredHellingerDistance(kde_pdf, kde_pdf)
		print "EngineersMetric: ", gen.EngineersMetric(kde_pdf, kde_pdf)
		print "LpMetric: ", gen.LpMetric(kde_pdf, kde_pdf, 1.0)
		

if __name__ == '__main__':
	unittest.main()