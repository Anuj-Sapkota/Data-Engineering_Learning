# # first = "Anuj"
# # last = "Sapkota"

# # #Print
# # print(type(first))
# # print(type(first) == str)
# # # Strings are instance of Str class

# # # Casting number into string
# # decade = str(1980)
# # print(type(decade))
# # print(decade)

# # Multiple Lines

# multilineString = """This 
# is
# a 
# multiline
# String."""
# print(multilineString)

# # escape special characters
#     # Print a single quote
# print("I\'m a programmer.\tI am learning Python.\nI am enjoying\\it.")

# #String Methods
# # .lower() - converts string to lower case
# # .upper() - converts string to upper case
# # .title() - converts string to title case
# #print("anuj sapkota".title())
# print("Anuj".replace("n","B"))

### Strip ####
# its default syntax is string.strip([characters]) where c.. are the characters we want to remove. but we donot specify any characters it will just remove whitespaces
# removes chars/ spaces from the begining or the end only
# rstrip ==> Removes the right
# lstrip ==> Removes the left

# Build a menu
# title = "menu".upper()
# print(title.center(20,"="))
# print("coffee".ljust(17,".") + "$1".rjust(3))
# print("Muffin".ljust(17,".") + "$2".rjust(3))
# print("Cheescake".ljust(17,".") + "$4".rjust(3))

# String index values
# first = "AnujSapkota"
# print(first[1:])

# # some methods return boolean data
# print(first.startswith("A"))
# print(first.endswith("a"))

# # Complex data type
# comp_value = 5 + 3j
# print(type(comp_value))
# print(comp_value.real)
# print(comp_value.imag)

# Built in data types in python
# 1) abs() ===> Returns the non-negative integer of a number
# 2) round() ==> Returns the rounded number of a float number.
# 3) round(int, specifier) ==> Returns the rounded number of a float number upto the specifier decimals place.

########## Functions in the math module
# Power and root functions
# math.sqrt(x) ==> Square root of x
# math.pow(x, y) ==> x ^ y
# math.exp(x) ==> e ^ x
# math.expm1(x) ==> e ^ -1

########## Logarithmic Functions ==> To what power must the base be raised to produce the given number
# math.log(x) ==> Natural log ( base e) ==> math.log(10) -> 2.30
# math.log(x, base) ==> Log of x in given base 
# math.log2(x) ==> Log base 2 
# math.log10(x) ==> Log base 10

######### Trigonometric Functions###########
# math.sin(x) ===> sine of x in radians
# .... Others are same
# math.asine(x) ===> Inverse of sine
# math.atan2(y,x) ==> atan(y/x)  ===> 2 is there just for the num/den 

######## hyperbolic Functions
# math.sinh(x) ==> hypebolic Sine

######### Factorial and combinatorics#########
# math.factorial(n) ===> returns n!
# math.comb(n ,k) ==> Combinations: nCk
# math.perm(n ,k) ==> Permutations: nPk

# print(" Factorial and combinatorics ".center(40, "#"))
########### Special Functions
# math.gdc(a, b) ==> Greatest common divisor of a and b
# math.lcm(a, b) ==> Least common multiple of a and b 
# math.isqrt(n) ==> integer square root 

######## Casting string to number
# zipcode = "102123"
# zip_value = int(zipcode)
# print(type(zip_value))