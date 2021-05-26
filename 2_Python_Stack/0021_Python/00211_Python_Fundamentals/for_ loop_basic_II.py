#1
#Biggie Size - Given a list, write a function that changes all 
#positive numbers in the list to "big".
#Example: biggie_size([-1, 3, 5, -5]) returns that same list, 
#but whose values are now [-1, "big", "big", -5]

def biggie_size(givenList):
    length = len(givenList)
    for i in range(0, length):
        if givenList[i] > 0:
            givenList[i] = "big"
    return givenList
givenList = [-1, 3, 5, -5]
print(biggie_size(givenList))
#solution:
#[-1, 'big', 'big', -5]

#=================================================================

#2
#Count Positives - Given a list of numbers, create a function to 
#replace the last value with the number of positive values. 
#(Note that zero is not considered to be a positive number).
#Example: count_positives([-1,1,1,1]) changes the original list 
# to [-1,1,1,3] and returns it
#Example: count_positives([1,6,-4,-2,-7,-2]) changes the list 
#to [1,6,-4,-2,-7,2] and returns it

def count_positives(givenList):
    count = 0
    length = len(givenList)
    for i in range(0, length):
        if givenList[i] > 0:
            count += 1
    givenList[length - 1] = count
    return givenList
    
print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))
#solutions:
#[-1, 1, 1, 3]
#[1, 6, -4, -2, -7, 2]

#=================================================================

#3
#Sum Total - Create a function that takes a list and returns 
#the sum of all the values in the array.
#Example: sum_total([1,2,3,4]) should return 10
#Example: sum_total([6,3,-2]) should return 7
def sum_total(givenList):
    sumTot = 0
    length = len(givenList)
    for i in range(0, length):
        sumTot += givenList[i]
    return sumTot

print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))
#solution
#10
#7

#=================================================================

#4
#Average - Create a function that takes a list and returns 
#the average of all the values.
#Example: average([1,2,3,4]) should return 2.5
def average(givenList)
    summ = 0
    length = len(givenList)
    for i in range(0, length):
        summ += givenList[i]
    avg = summ / length
    return avg

print(average([1,2,3,4]))
#solution: 2.5

#=================================================================

#5
#Length - Create a function that takes a list and 
#returns the length of the list.
#Example: length([37,2,1,-9]) should return 4
#Example: length([]) should return 0
def length(givenList):
    return len(givenList)

print(length([37,2,1,-9]))
print(length([]))
#solutions:
#4
#0

#=================================================================

#6
#Minimum - Create a function that takes a list of numbers and 
#returns the minimum value in the list. If the list is empty, 
#have the function return False.
#Example: minimum([37,2,1,-9]) should return -9
#Example: minimum([]) should return False

def minimum(givenList):
    length = len(givenList)
    if length ==0:
        return False
    
    minVal = givenList[0]
    for i in range(1, length):
        if givenList[i] < minVal:
            minVal = givenList[i]
    return minVal

print(minimum([37,2,1,-9]))
print(minimum([]))

#solution:
# -9
# False

# OR

def minimum(givenList):
    length = len(givenList)
    if length ==0:
        return False
    else:
        return min(givenList)

print(minimum([37,2,1,-9]))
print(minimum([]))
#solution:
# -9
# False


#=================================================================

#7
# Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def maximum(list):
    if len(list) == 0:
        return False
    else:
        return max(list)
print(maximum([37,2,1,-9]))
print(maximum([]))

#solutions:
# 37
# False

#=================================================================

#8
# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(list):
    listSum = 0
    for i in list:
        listSum += i
    avg = listSum/len(list)
    new_dict = {
        "sumTotal": listSum,
        "average": avg,
        "minimum": min(list),
        "maximum": max(list),
        "length": len(list)
        }
    return new_dict
print(ultimate_analysis([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(ultimate_analysis([37,2,1,-9]))
#solutions:
#{'sumTotal': 55, 'average': 5.5, 'minimum': 1, 'maximum': 10, 'length': 10}
#{'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4}

#=================================================================

#9
# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

# without creating a second list
def reverse(list):
    list.reverse()
    print(list)
    return list
reverse([37,2,1,-9])
#solutions:
#[-9, 1, 2, 37]

# OR
def reverse_list2(some_list):
    lgth = len(some_list)
    for i in range(0, lgth//2, 1):
        temp = some_list[i]
        some_list[i] = some_list[lgth - 1 - i]
        some_list[lgth - 1 - i] = temp
    return some_list
print(reverse_list2([37,2,1,-9]))
#solution:
#[-9, 1, 2, 37]

# OR

# by creating a second list
def reverse_list2(some_list):
    some_list = some_list[::-1]
    return some_list

reverse_list([37,2,1,-9])
#solution:
#[-9, 1, 2, 37]

#=================================================================