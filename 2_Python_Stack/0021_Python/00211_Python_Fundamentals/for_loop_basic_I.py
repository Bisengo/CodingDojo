#Basic - Print all integers from 0 to 150.
for number in range(151):
    print(number)


#Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for number in range(5, 1005, 5):
    print(number)

#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, 
#print "Coding" instead. If divisible by 10, print "Coding Dojo".
for number in range(1, 101):
    if number % 10 == 0:
        print("Coding Dojo")
    elif number % 5 == 0:
        print("Coding")
    else:
        print(number)


#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, 
#and print the final sum.
sum = 0
for number in range(0, 500001):
    if number % 2 == 1:
        sum += number
print(sum)

#Countdown by Fours - Print positive numbers starting at 2018, 
#counting down by fours.
for number in range(2018, 0, -4):
    print(number)

#Flexible Counter - Set three variables: lowNum, highNum, mult. 
#Starting at lowNum and going through highNum, print only the 
#integers that are a multiple of mult. For example, if lowNum=2, 
#highNum=9, and mult=3, the loop should print 3, 6, 9 
#(on successive lines)

def multiple_of_mult(lowNum, highNum, mult):
    for number in range (lowNum, highNum + 1):
        if number % mult == 0:
            print(number)
multiple_of_mult(2, 9, 3)

# solution
# 3
# 6
# 9