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

	# def test_total_variation(self):
	# 	mean1 = 0.0
	# 	std1 = 1
	# 	size_sample_data = 500
	# 	#generate data with mean loc and std scale
	# 	#generate 300 data points with dimension 1
	# 	#the sample data matrix is of size (300,1)
	# 	sampD1 = list(scipy.stats.norm.rvs(loc=mean1,scale=std1,size=size_sample_data))
	# 	#sampD2 = list(scipy.stats.norm.rvs(loc=mean2,scale=std2,size=size_sample_data))

	# 	gen = scg.SmoothCurveGenerator(sampD1, [])
	# 	kde_pdf = gen.generateKernelDensityEstimateSmoothFunction()
	# 	print "expect: ", gen.expect(kde_pdf)
	# 	print "getTotalVariation: ", gen.getTotalVariation(kde_pdf, kde_pdf)
	# 	print "kl divergence: ", gen.SquaredHellingerDistance(kde_pdf, kde_pdf)
	# 	print "SquaredHellingerDistance: ", gen.SquaredHellingerDistance(kde_pdf, kde_pdf)
	# 	print "EngineersMetric: ", gen.EngineersMetric(kde_pdf, kde_pdf)
	# 	print "LpMetric: ", gen.LpMetric(kde_pdf, kde_pdf, 1.0)

	def test_simple_kl_divergence_test(self):
		mean1 = 3.0
		std1 = 5
		size_sample_data = 1000
		sampD1 = list(scipy.stats.norm.rvs(loc=mean1,scale=std1,size=size_sample_data))
		gen = scg.SmoothCurveGenerator(sampD1, [])
		pdf_normal_fitted_by_kde_mean1 = gen.generateKernelDensityEstimateSmoothFunction()

		mean1 = 2.0
		std1 = 7
		size_sample_data = 1000
		sampD1 = list(scipy.stats.norm.rvs(loc=mean1,scale=std1,size=size_sample_data))
		gen = scg.SmoothCurveGenerator(sampD1, [])
		pdf_normal_fitted_by_kde_mean2 = gen.generateKernelDensityEstimateSmoothFunction()
		print "Here"
		print "KL DIVERGENCE: N1, N2 ", gen.getKlDivergence(pdf_normal_fitted_by_kde_mean1, pdf_normal_fitted_by_kde_mean2)
		print "KL DIVERGENCE: N2, N1 ", gen.getKlDivergence(pdf_normal_fitted_by_kde_mean2, pdf_normal_fitted_by_kde_mean1)
		#print "KL DIVERGENCE: N1, N1 ", gen.getKlDivergence(pdf_normal_fitted_by_kde_mean1, pdf_normal_fitted_by_kde_mean1)
		print "Here"

	#integrate ((1/(5*sqrt(2*pi*1))*e^((-1/2)(1/25)(x-5)^2) * log_2((3/5)*e^((8/225)(x-5)^2))) from -infinity to infinity

if __name__ == '__main__':
	unittest.main()