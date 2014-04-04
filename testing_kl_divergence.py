import numpy as np
# import random as rand
import scipy as scipy
from scipy import stats
from pylab import plot,show,hist
import SmoothCurveGenerator as scg

from scipy.stats import norm
# numargs = norm.numargs
# [  ] = [0.9,] * numargs
mean = 1.0
std = 1.0
rv = norm(loc=mean, scale=std)
# Display frozen pdf
x = np.linspace(-3, 3)
h = plot(x, rv.pdf(x))
#show()
print ("mean: ", mean)
print ("std: ", std)
print ("scipy.stats.norm.expect: ", scipy.stats.norm.expect(lambda x: x, loc=mean, scale=std))

mean1 = -1.0
std1 = 1
size_sample_data = 300
sampD1 = list(scipy.stats.norm.rvs(loc=mean1,scale=std1,size=size_sample_data))
gen = scg.SmoothCurveGenerator(sampD1, [])
kde_pdf = gen.generateKernelDensityEstimateSmoothFunction()
#gen.plotSmoothFunction_1D(kde_pdf)

def f(x):
	return kde_pdf(x) * x

def g(x):
	return scipy.stats.norm.pdf(x, loc=mean, scale=std) * x

print scipy.integrate.quad(g, float("-inf"), float("inf"))



