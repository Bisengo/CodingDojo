# Practice using default parameter values, passing in named arguments
# and passing in named arguments

import random

def randInt(min=0, max=100):
    if min == max or min >= max or max <= 0:
        return "change your inputs"
    else:
        num = min + (max-min) * random.random()
        return int(num)

print(randInt()) 		    # should print a random integer between 0 to 100
print(randInt(max=50)) 	    # should print a random integer between 0 to 50
print(randInt(min=50)) 	    # should print a random integer between 50 to 100
print(randInt(min=50, max=500))     # should print a random integer between 50 and 500
print(randInt(min=80, max=20))      # should be covered the border cases
print(randInt(min=80, max=0))       # should be covered the border cases