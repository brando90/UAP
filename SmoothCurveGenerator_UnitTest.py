import SmoothCurveGenerator as scg
import unittest

#every test will start with test_{some description}_{name of function from package being tested}

#Unit tests for SmoothCurveGenerator
class TestSmoothCurveGenerator(unittest.TestCase):
	def setUp(self):
		self.simpleDataPoints = [2,4]

	def test_simple_estimateSampleMean(self):
		scgen = scg.SmoothCurveGenerator([2,6])
		x_mean = scgen.estimateSampleMean(scgen.getDataList())
		actual_mean =  4
		self.assertEqual(x_mean, actual_mean)

	def test_simple_estimateSampleMean(self):
		scgen = scg.SmoothCurveGenerator([2,6])
		x_var = scgen.estimateSampleVariance(scgen.getDataList())
		actual_var =  4
		self.assertEqual(x_var, actual_var)
		

if __name__ == '__main__':
	unittest.main()