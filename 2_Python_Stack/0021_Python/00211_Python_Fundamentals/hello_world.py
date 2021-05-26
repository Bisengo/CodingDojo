# 1. TASK: print "Hello World"
print("Hello World")

# solution
# Hello World

#===========================================================

# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print("Hello",name)	# with a comma
print("Hello " +name )	# with a +

# solution
# Hello Noelle
# Hello Noelle

#===========================================================

# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello",name)	# with a comma
# print("Hello " + name )	# with a +	-- this one should give us an error!
print("Hello " + str(name)) # typecasting

# solution for print("Hello", name)
# Hello 42
#========================================
# solution for print("Hello " + name )
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: must be str, not int
#========================================
# solution for print("Hello " + str(name))
# Hello 42
#===========================================================

# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"

print("I love to eat {} and {}.".format(fave_food1, fave_food2)) # with .format()
# solution
# I love to eat sushi and pizza.

print(f"I love to eat {fave_food1} and {fave_food2}") # with an f string.
# solution
# I love to eat sushi and pizza.

print("coding dojo".upper())
# solution
# CODING DOJO

print("CHICAGO".lower())
# solution
# chicago

print("coding dojo".count("d"))
# solution
# 2

print("coding dojo is definitely a good school".count("d"))
# solution
# 4