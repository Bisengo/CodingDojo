def palisearch(string):
	result1 = []
	result2 = []

	for i in range(0, len(string) // 2):
		result1.append(string[i])
	for j in range(-1, -(len(string) // 2) - 1, -1):
		result2.append(string[j])
	return result1 == result2