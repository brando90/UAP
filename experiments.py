from scipy import stats
import numpy as np
def measure(n):
	"""
	Measurement model, return two coupled measurements.
	Returns two np.arrays() with two mixture guassian with 2 modes.
	"""
	m1 = np.random.normal(size=n)
	m2 = np.random.normal(scale=0.5, size=n)
	return m1+m2, m1-m2

m1, m2 = measure(10)
print type(m1), m2

##---get max and mins
m1, m2 = measure(2000)
xmin = m1.min()
xmax = m1.max()
ymin = m2.min()
ymax = m2.max()

##---
X, Y = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
positions = np.vstack([X.ravel(), Y.ravel()])
values = np.vstack([m1, m2])
kernel = stats.gaussian_kde(values)
Z = np.reshape(kernel(positions).T, X.shape)