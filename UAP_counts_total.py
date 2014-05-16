import time
import random
import os
import numpy as np
import math

class TupleData:
	def __init__(self, group, attribute):
		self.group = group
		self.attribute = attribute

	def getGroup(self):
		return self.group

	def getAttribute(self):
		return self.attribute

def printTest():
	print "Import was successful!"
	os.exit(0)

def getRandomOffsets(k, data_len, seed = 0):
	"""
	Generates a list of k random offsets. 
	An offset is an index such that 0<= index < self.n
	"""
	# random.randint(a, b)
	# Return a random integer N such that a <= N <= b.
	random.seed(0)
	offsets = []
	for i in range(k):
		rand_index = random.randint(0, data_len - 1)
		offsets.append(rand_index)
	return offsets

def estimateCountsForGroupPoisson(data, list_offests, g_i):
	"""
	Returns the counts for group g_i in the current data set.
	By counts we mean an estimate of the number of g's in the data set.
	Also, estiamtes the mean number of elements (counts) you will expect to 
	see in a unit time period.
	"""
	n = len(data)
	list_nij = {} #list of elements traversed for group g_i
	list_tij = {}
	Nki = 0 #total elements travered to see self.k g_i's
	Tki = 0 #total time traversed to see self.k g_i's
	for o in list_offests:
		searching_for_g_i = True
		index = o
		start_time = time.time()
		while searching_for_g_i:
			current_elem = data[index].group
			if current_elem == g_i:
				end_time = time.time()
				searching_for_g_i = False
				#get data
				tij = end_time - start_time #time to find that g_i (on offset j = o)
				nij = index - o + 1 #number of elements traversed until we found g_i (on offset j = o)
				#store data
				list_nij[o] = nij
				list_tij[o] = tij
				Nki += nij
				Tki += tij
			index = (index + 1) % n
	#calculate relevant statistics
	lambdaVal = float(len(list_offests) - 1) / float(Tki) #for poission distribution
	#tau = float(Tki) / float(Nki)
	T = 5.49245905876
	total_counts_g_i = lambdaVal * T
	#total_counts_g_i = (len(list_offests) * n) / Nki #total estiamte of the number of elements of g_i the data set has
	return total_counts_g_i

def getEstiamteLambda2(data, g_i, fixed_time=2.0):
	n = len(data)
	timeout = time.time() + fixed_time
	n_i = 0
	index = 0
	times_up = False
	while not times_up:
		current_elem = data[index].group
		if current_elem == g_i:
			n_i+=1
		if time.time() > timeout:
			times_up = True
		index = (index + 1) % n

	lambdaVal = n_i / fixed_time
	T = 5.49245905876
	counts = lambdaVal * T
	return counts

def estiamteTimeToTraverseData(data):
	print "ESTIAMTING TIME TO TRAVERSE DATA"
	start_time = time.time()
	ni = 0
	n = len(data)
	for index in range(n):
		current_elem = data[index].group
		if current_elem == 0:
			ni+=1
		ni = (ni + 0) % n
	end_time = time.time()
	print end_time - start_time
	os.exit(0)

# def estimateCountsForGroupSubGroupAlg(self, g_i, size_subgroup, times_to_sample, seed = 0):
# 	"""
# 	Returns the counts for group g_i in the current data set.
# 	By counts we mean an estimate of the number of g's in the data set.
# 	This methid does it by considering subgroups.
# 	Note that if size_subgroup * times_to_sample >= self.n, then there is
# 	no point in estiamting it this way, you might as well look at the whole
# 	data an actually count it.
# 	"""
# 	total_number_of_elements_alg_inspects = num_subgroups * times_to_sample
# 	if total_number_of_elements_alg_inspects >= self.n:
# 		raise NameError("There is not point of doing an estimate when the exact answer can be obtain with O(n) runtime.")
# 	fraction_of_g_i = self.estimateFractionOfGroupi(g_i, size_subgroup, times_to_sample, seed)
# 	return fraction_of_g_i * self.n

# def estimateFractionOfGroupi(self, g_i, size_subgroup, times_to_sample, seed = 0):
# 	"""
# 	Returns an estiamte for the fraction of elements for group g_i in the current data set.
# 	"""
# 	rand_offsets = self.getRandomOffsets(times_to_sample, seed)
# 	count_g_i = 0
# 	for offset in rand_offsets:
# 		index = offset
# 		while index < offset + size_subgroup:
# 			element = self.data[index % self.n]
# 			if element == g_i:
# 				count_g_i+=1
# 			index+=1
# 	return float(count_g_i) / float(size_subgroup * times_to_sample)

#def estimateCountsForGroupPoisson(self, g_i, offset, time_limit, ):

def MakeShuffledData(data, meta):
	"""
	data = is a data_utils.Data. data[g] will give you the DataArray for that group
	"""
	groups = meta['groups']
	all_data = np.array([])
	for g in groups:
		d = np.array([TupleData(group=g, attribute=a) for a in data[g].array])
		all_data = np.append(all_data, d)
	np.random.shuffle(all_data)
	return all_data

def GetApproxCountsForGroups(shuffledData, meta, debug = False):
	counts2groups = {}
	for g in meta["groups"]:
		list_offests = getRandomOffsets(k=100, data_len=len(shuffledData), seed=0)
		current_counts = estimateCountsForGroupPoisson(shuffledData, list_offests, g)
		#current_counts = getEstiamteLambda2(shuffledData, g)
		counts2groups[g] = current_counts
        if debug:
	        print 
	        print "group: ", g
	        print "list_offests", list_offests 
	        print "counts: " , current_counts
	return counts2groups

def GetTrueCounts(data, meta):
	trueCounts = {}
	for g in meta["groups"]:
		trueCounts[g] = len(data[g].array)
	return trueCounts

def GetApproxTotals(groups2counts, approxMeans, meta):
	totalAttribute = {}
	for g in meta["groups"]:
		counts = groups2counts[g]
		approx_mean = approxMeans[g]
		totalAttribute[g] = counts * approx_mean
	return totalAttribute

def GetTrueTotal(trueCounts, trueMeans, meta):
	trueTotalAttribute = {}
	for g in meta["groups"]:
		counts = trueCounts[g]
		approx_mean = trueMeans[g]
		trueTotalAttribute[g] = counts * approx_mean
	return trueTotalAttribute

#MAPE, the Mean Absolute Percentage Error
def GetMeanAbsolutePercentageError(errorArray):
	return float(sum(errorArray))/float(len(errorArray))

#APE, the Absolute Percentage Error
def GetAbsolutePercentageError(trueValsArray, approxValsArray, metaArg):
	# print "trueValsArray", trueValsArray
	# print "approxValsArray", approxValsArray
	# print "type(trueValsArray)", type(trueValsArray)
	# print "type(approxValsArray)", type(approxValsArray)
	meta = metaArg
	relativeErrors = [0]*len(meta["groups"])
	for g in meta["groups"]:
		trueVal = trueValsArray[g]
		approxVal = approxValsArray[g]
		# print "g: ", g
		# print "type(trueVal)", type(trueVal)
		# print "type(approxVal)", type(approxVal)
		# print "trueVal", trueVal
		# print "approxVal", approxVal
		diff = math.fabs(trueVal - approxVal)
		relativeErrors[g] = float(diff)/float(trueVal)
	return relativeErrors, GetMeanAbsolutePercentageError(relativeErrors)



# def DoUAP(data, meta, algsum):
# 	true_means = algsum["actual_means"]
#     approx_means = algsum["means"]
# 	shuffleData = UAP.MakeShuffledData(data, meta)

#     #UAP.estiamteTimeToTraverseData(shuffleData)

#     #get counts
#     approxCounts = UAP.GetApproxCountsForGroups(shuffleData, meta)
#     trueCounts = UAP.GetTrueCounts(data, meta)
#     if len(approxCounts) != len(trueCounts):
#         print "len(approxCounts) != len(trueCounts)"
#         raise
#     #cal totals = counts * means
#     approxTot = UAP.GetApproxTotals(approxCounts, approx_means, meta)
#     trueTot = UAP.GetTrueTotal(trueCounts, true_means, meta)

#     #print "\npercentage error calculation"
#     percentageErrorsCounts, MAPEcounts = UAP.GetAbsolutePercentageError(trueValsArray=trueCounts, approxValsArray=approxCounts, metaArg=meta)
#     #print "-------"
#     percentageErrorsTotal, MAPEtotal = UAP.GetAbsolutePercentageError(trueValsArray=trueTot, approxValsArray=approxTot, metaArg=meta)
#     print ":::::::> percentageErrorsCounts", MAPEcounts
#     print ":::::::> percentageErrorsTotal", MAPEtotal

