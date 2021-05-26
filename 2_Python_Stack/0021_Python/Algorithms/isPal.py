x = "racecar"
def isPal(stringInput):
    newstr = ""
    for i in range(len(stringInput)-1, -1, -1):
        newstr += stringInput[i]
    print(f"the new string is {newstr}")
    print(f"the initial string is {stringInput}")
    if stringInput == newstr:
        print("True")
        return True
    else:
        print("False")
        return False

isPal(x)

"""
There is a more efficient way
"""
def isPal2(stringInput)
    for i in range(0, len(stringInput)//2, 1)
        if stringInput[i] != stringInput[len(stringInput)-1-i]:
            return False
    return True



