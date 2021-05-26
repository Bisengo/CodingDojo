def parensValid(inputString):
    #some code here
    # go through the string, and keep track of number of open and number of close parens
    opencount = 0
    closedcount = 0
    for i in range(0,len(inputString),1):
        if inputString[i] == "(":
            opencount +=1
        if inputString[i] == ")":
            closedcount +=1
        if closedcount > opencount:
            return False
    if opencount != closedcount:
        return False
    else:
        return True

    #after getting the totals, compare the total open versus total closed
    # returns either True or False


print(parensValid(")(")) 