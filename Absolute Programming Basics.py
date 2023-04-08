# -*- coding: utf-8 -*-
"""
Absolute Programming Basics with Python
Spyder version 5.3.3
"""
# This video is a broad introduction to a lot of programming concepts, but we will not be looking at any of them in depth
# Starting with the absolute basics, this is a line of code
# Note how even when I try to execute these lines, it does not produce anything
print("This is different, look at the bottom right")

# This is a comment, a line of code that is "ignored" by Python
# Python is the programming language that we will be using today
# More specifically, this is Python with Anaconda and using Spyder as an IDE (Integrated Development Environment)
# You can just run a command in the console if you want, like this

# Now, why do we code?
# We can do a lot of things in Python, but let's start with some simple math
# The line below adds together 4 and 5
4 + 5

# The output of the console is the number 9
# In some ways, a programming language is just a glorified and hyper complicated calculator
# Divide 5 over 9
5/9

# Let's keep the simple math for a while with substraction and multiplication at the same time
8 - 3
5 * 5

# We only we 25, why?
# Because even though we did execute both statements, the console only returns the last one
print(8 - 3)
print(5 * 5)

# Notice how applying the print function gives us  the output for both operations
# Let's do something famous, but with a small tweak
print("Hello, Python!")

# As we expected, the output is shown at the console
# With the absolute basics covered, let's move to variables

# Introduction to variables
# A variable "stores" a value
# Let's just create a variable named "five" with the value of 5
# We assign the value to the variable on the left with =
five = 5

# Notice how the variable explorer now displayes our first variable
# We can print our variable 5
print(five)

# We can also perform math with it, because the value of the variable is 5
print(five + 6)

# We can even create a new variable with our previous variable
new_variable = (five * 3)/4
print(new_variable)

# Variables can store pretty much everything, like a message
secret_message = "You are learning Python"
print(secret_message)

# What happens if we don't know what is inside a variable? We will see that in data types

# Some simple if statements and boolean values
# If statements follow some logic
# They allow us to do fancy stuff that for now we will call procedual programming

if 5 < 9:
    print("This makes sense")
else:
    print("This should not print")
    
# Reading it in plain English, if 5 is less than 9, print this makes sense
# Otherwise, print this should not print
# if statements allow us to execute things depending on a condition, notice if we do this

if 5 < 9 == False:
    print("This makes sense")
else:
    print("This should not print")

# Why did the else block print? Think about it for a second
# The indentation is used to execute blocks in Python
# More important, False is a boolean value
# Boolean values are special, they are either True or False
one_boolean = True
another_boolean = False

# Look at the variable explorer for a second, both variables are of bool type
# Boolean logic is rather straightforward, True is equal to True
one_boolean == one_boolean
# Or
True == True
# False is also equal to False, therefore True
another_boolean == another_boolean
# Or
False == False
# False is not equal to True, and it will give us False
another_boolean == one_boolean
# Or
False == True

# And finally, True is also not equal to False
one_boolean == another_boolean
# Or
True == False

# But a very special property is that 1 is equal to True and 0 is equal to False
1 == True
0 == False

# What if we add two Trues?
True + True

# The math checks out, what about multiplication using our variable?
one_boolean * 9

# The logic behind this is that computers think in 0s and 1s
# This covers most of the basics of if and boolean values

# Basic data types and casting
# Python has multiple data types, but for this video, we will just stick to three
# Boolean
a_third_boolean = True

# Numeric
num_variable = 665

# And strings
string_variable = "This is a string"

# Can we add a string and a number?
num_variable + string_variable

# We will get an error as Python does not know how to interpret mixing strings and numbers
# What about a number in a string?
num_string = "5"

# Try again
num_string + num_variable

# Even though we cannot add them directly, we can make Python interpret the string as a number
int(num_string) + num_variable

# This makes more sense if we use the function type, this gives us the data type of a variable

print(type(num_string))
print(type(int(num_string)))

# There are some limitations to casting though, such as trying to cast a string as an integer
int(string_variable)

# Python does not know how to convert it into a number

# Other operators besides basic math

# The Modulus operator
20 % 11

# If we divide 20 over 11, we have 9 left

# Exponentiation

2 ** 3

# This is two to the cube, or 8

# If you need a refresher in exponentiation, remember that 

two_times_two = 2 * 2

# Is the same as 

2 ** 2 == two_times_two

# Python lists and printing all the list
# A list contains various values inside it 

first_list = [0, 2, 4, 6, 8]

# We can print a list like we print any variable

print(first_list)

# We can use the len function to find out how many items are in a list

len(first_list)

# Lists allows for more flexibility as they can have multiple data types

mixed_list = [3, "Not a number", False]

# And we can print them

print(mixed_list)

# But if we use the type class, we will get the list data type

print(type(mixed_list))
print(type(first_list))

# A glimpse on more advanced topics, we can go through all the elements of a list
for i in range(len(first_list)):
    print(first_list[i])

# What is the range function?

range(len(first_list))

# This function allows us to stay in the index

# A very basic function
# We have been using functions from Python, but we can even create our own functions

def complex_operations(number):
    print("This is our first function")
    print("First, we take the number that you gave us")
    number = number + 5
    print("We have just added 5")
    number = number * 3
    print("We have multiplied the number by three")
    print(number)
    return number

complex_operations(3)    

# You can see how functions allow us to save time as we can recycle code

print(complex_operations(20))
print(complex_operations(13))

# Functional programming is powerful, and it can become very complex

# Importing a package
# A package is a collection of code and modules that we can use
# We use them by using import
import pandas as pd

# With the line above, we are importing pandas, and calling it by the alias "pd"

pd.isna(first_list)

# The isna function is inside pandas and allows us to check if any item of a list is null

# You can see the Data Analytics Computing Series to see multiple examples of predictive algorithms in Python