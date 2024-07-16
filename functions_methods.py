import math

# # FUNCTIONS
# print("a value") # doesn't return a value
# input("ask for a value") #returns a value

# # METHODS => FUNCTIONS OF DATATYPES
# print("value".upper())
# print("VALUE".lower())
# print("value".replace("e", "3"))

# # NEW FUNCTIONS
# print(abs(-1)) #absolute value, turns all nrs to positive ones
# print(max(10,5))
# print(min(0,1))
# print(len("test")) #length of string

# EXERCISE
width = int(input("Please insert width (cm) of the triangle: "))
height = int(input("Please insert height (cm) of the triangle: "))
pythagoras = math.sqrt((width * width) + (height * height))
print("The hypothenuse is", round(pythagoras,2), "cm")
# print(type(pythagoras)) #shows what type of the variable