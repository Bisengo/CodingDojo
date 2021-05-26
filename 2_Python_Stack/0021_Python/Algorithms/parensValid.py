def parensValid(stringInput):
    openParensCount = 0
    closeParensCount = 0
    for i in range(len(stringInput)):
        if stringInput[i] == "(":
            openParensCount += 1
        if stringInput[i] == ")":
            closeParensCount += 1
        if closeParensCount > openParensCount:
            return False

    if openParensCount == closeParensCount:
        return True
    else:
        return False
print(parensValid("Hel(lo)  (world"))

        