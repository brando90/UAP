import time
# start_time = time.time()
# main()
# print time.time() - start_time, "seconds"

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

	def estimateCountsForGroup(self, g_i):
		"""
		Returns the counts for group g_i in the current data set.
		By counts we mean an estimate of the number of g's in the data set.
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
					Tki
				index = (index + 1) % n
		#calculate relevant statistics
		self.mean_counts_per_time = float(sel.k) / float(Tki) #for poission distribution
		total_counts_g_i = (self.k * self.n) / Nki #total estiamte of the number of elements of g_i the data set has
		return total_counts_g_i
