def palisearch(string):
	result1 = []
	result2 = []
    length = len(string)

	for i in range(0, length // 2):
		result1.append(string[i])
	for j in range(length, (length // 2) - 1, -1):
		result2.append(string[j])
	return result1 == result2

    print