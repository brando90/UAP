import time
import random

class EstimateCountsPoission:
	def __init__(self, list_offests, data):
		self.data = data # {g : DataArray(g, path) for g in groups} TODO check this
		self.n = len(data)
		self.checkOffsetsValid(list_offests)
		self.list_offests = list_offests
		self.k = len(list_offests)

	def checkOffsetsValid(list_offests):
		for o in list_offests:
			if o >= self.n:
				raise NameError('None of the offests should be greater than the length of the data set.')
		return True

	# def sum_dict(d):
	# 	total = 0
	# 	for key in d:
	# 		total += d[key]
	# 	return total

	def getRandomOffsets(self, k, seed = 0):
		"""
		Generates a list of k random offsets. 
		An offset is an index such that 0<= index < self.n
		"""
		# random.randint(a, b)
		# Return a random integer N such that a <= N <= b.
		random.seed(0)
		offsets = []
		for i in range(k):
			rand_index = random.randint(0, self.n - 1)
			offsets.append(rand_index)
		return offsets

	def estimateCountsForGroupPoisson(self, g_i):
		"""
		Returns the counts for group g_i in the current data set.
		By counts we mean an estimate of the number of g's in the data set.
		Also, estiamtes the mean number of elements (counts) you will expect to 
		see in a unit time period.
		"""
		n = self.n
		list_nij = {} #list of elements traversed for group g_i
		list_tij = {}
		Nki = 0 #total elements travered to see self.k g_i's
		Tki = 0 #total time traversed to see self.k g_i's
		for o in self.list_offests:
			searching_for_g_i = True
			index = o
			start_time = time.time()
			while searching_for_g_i:
				current_elem = self.data[index]
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
		self.mean_counts_per_time = float(sel.k) / float(Tki) #for poission distribution
		total_counts_g_i = (self.k * self.n) / Nki #total estiamte of the number of elements of g_i the data set has
		return total_counts_g_i

	def estimateCountsForGroupSubGroupAlg(self, g_i, size_subgroup, times_to_sample, seed = 0):
		"""
		Returns the counts for group g_i in the current data set.
		By counts we mean an estimate of the number of g's in the data set.
		This methid does it by considering subgroups.
		Note that if size_subgroup * times_to_sample >= self.n, then there is
		no point in estiamting it this way, you might as well look at the whole
		data an actually count it.
		"""
		total_number_of_elements_alg_inspects = num_subgroups * times_to_sample
		if total_number_of_elements_alg_inspects >= self.n:
			raise NameError("There is not point of doing an estimate when the exact answer can be obtain with O(n) runtime.")
		fraction_of_g_i = self.estimateFractionOfGroupi(g_i, size_subgroup, times_to_sample, seed)
		return fraction_of_g_i * self.n

	def estimateFractionOfGroupi(self, g_i, size_subgroup, times_to_sample, seed = 0):
		"""
		Returns an estiamte for the fraction of elements for group g_i in the current data set.
		"""
		rand_offsets = self.getRandomOffsets(times_to_sample, seed)
		count_g_i = 0
		for offset in rand_offsets:
			index = offset
			while index < offset + size_subgroup:
				element = self.data[index % self.n]
				if element == g_i:
					count_g_i++
				index++
		return float(count_g_i) / float(size_subgroup * times_to_sample)
