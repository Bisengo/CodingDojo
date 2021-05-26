#1
#Countdown - Create a function that accepts a number as an input. 
#Return a new list that counts down by one, from the number 
#(as the 0th element) down to 0 (as the last element).
#Example: countdown(5) should return [5,4,3,2,1,0]
def Countdown(number):
    newlist = []
    for i in range(number, -1, -1):
        newlist.append(i)
    return newlist

print(Countdown(5))
# solution: [5, 4, 3, 2, 1, 0]

#==============================================================
#2
#Print and Return - Create a function that will receive a list 
#with two numbers. Print the first value and return the second.
#Example: print_and_return([1,2]) should print 1 and return 2
def print_and_return(number1, number2):
    print(number1)
    return number2

print_and_return(1, 2)
# solution: 1
a = print_and_return(3, 4)
# solution: 3
print(a)
# solution: 4

#==============================================================
#3
#First Plus Length - Create a function that accepts a list and 
#returns the sum of the first value in the list plus the list's length.
#Example: first_plus_length([1,2,3,4,5]) should return 6 
#(first value: 1 + length: 5)
def first_plus_length(list):
    if type(list[0]) is int:
        return list[0] + len(list)
    elif type(list[0]) is str:
        return "The first value of list is a String"
    elif type(list[0]) is bool:
        return "The first value of list is a Boolean"
    else:
        return "Abracadabra Abracadabra"

print(first_plus_length([1, 2, 3, 4, 5]))
#solution: 6

print(first_plus_length(["Papa", 2, 3, 4, 5]))
#solution: The first value of list is a String

print(first_plus_length([True, 2, 3, 4, 5]))
#solution: The first value of list is a Boolean

print(first_plus_length([1.5, 2, 3, 4, 5]))
#solution: Abracadabra Abracadabra

#==============================================================
#4
#Values Greater than Second - Write a function that accepts a list 
#and creates a new list containing only the values from the 
#original list that are greater than its 2nd value. 
#Print how many values this is and then return the new list. 
#If the list has less than 2 elements, have the function return False
#Example: values_greater_than_second([5,2,3,2,1,4]) should 
#print 3 and return [5,3,4]
#Example: values_greater_than_second([3]) should return False

def val_greater_than_second(givenList):
    newList = []
    count = 0
    if len(givenList) < 2:
        return False
    else:
        for i in givenList:
            if i > givenList[1]:
                newList.append(i)
                count += 1
    print(count)
    return newList
givenList = [5,2,3,2,1,4]
a = val_greater_than_second(givenList)
print(a)
#solution
#3
#[5, 3, 4]

#==============================================================
#5
#This Length, That Value - Write a function that accepts 
#two integers as parameters: size and value. The function should 
# create and return a list whose length is equal to the given size, 
#and whose values are all the given value.
#Example: length_and_value(4,7) should return [7,7,7,7]
#Example: length_and_value(6,2) should return [2,2,2,2,2,2]
def length_and_value(length, value):
    newList = []
    for i in range(0, length):
        newList.append(value)
    return newList

print(length_and_value(4, 7))
print(length_and_value(6, 2))
#solutions:
#[7, 7, 7, 7]
#[2, 2, 2, 2, 2, 2]
