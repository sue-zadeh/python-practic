# print ('hi world')
# the_world_is_flat = False
# if the_world_is_flat:
#     print("Be careful not to fall off!")

def max_and_min_number_in_list(lst):
    max = lst[0]
    min = lst[0]
    for a in lst:
        if a > max:
            max = a
        if a < min:
            min = a
    return (max, min)

print(max_and_min_number_in_list([1, 2, 3, 4, 5]))  # it it has error here, but it returns (5, 1) on my VS
print(max_and_min_number_in_list([-1, -4, -5, -7]))  # it returns (-1, -7) on my VS

# /////

def average_list(lst):
    # Calculate the average as the sum of the list divided by the number of elements
    return float(sum(lst) / len(lst))

# Test cases
print(average_list([1, 2, 3, 4, 5, 6, 7, 10.2]))  # Should return 4.775
print(average_list([-3, -2, -1, 0]))  # Should return -1.5

# //////////////////

# Nesting for loops is an excellent way to generate complicated output. For example the following code makes triangle shape in stars. Copy and run it in your own IDE

# n=5;
# for i in range(1,n+1,+1): # note the use of the range function, to generate a list equal to [1,2,....,n,n+1]
#         for j in range(i):
#             print ("* ", end="") #note the use of the end function, which replaces the default /n with "". 
#         print(i)
        
# Using all your knowledge of loops so far, make the following additions to the above code:

# wrap the loop in a function triangle_stars(int), that takes an integer input of any positive value
# fix the bug in the code that causes it to print one fewer rows of stars than needed (eg with the integer 5, it should print 5 rows of stars, from 1 to 5. The code currently prints 4 rows).
# add another pair of nested for loops within the same function, which print the same thing but flipped, (ie a decreasing number of stars). 
# finally, at the end of every row, print the total number of stars in that row (no 0's).
# NB that the middle row of stars should only be printed once
# also note that the range function can be run to generate a count down, using the form: range(start,stop,-1), and that it should probably be used to make your upside down triangle.

# For example:

# Test	Result

# triangle_stars(3)
# * 1
# * * 2
# * * * 3
# * * 2
# * 1
# triangle_stars(5)
# * 1
# * * 2
# * * * 3
# * * * * 4
# * * * * * 5
# * * * * 4
# * * * 3
# * * 2
# * 1
# Answer:(penalty regime: 10, 20, ... %)


def triangle_stars(n):
    # Print the ascending part of the triangle
    for i in range(1, n + 1):
        print('* ' * i + str(i))
        
    # Print the descending part of the triangle, skipping the base since it's already printed
    for i in range(n - 1, 0, -1):
        print('* ' * i + str(i))

# Test the function
triangle_stars(5)  # This should print a symmetrical triangle with 5 rows at its widest
triangle_stars(3)  # This should print a symmetrical triangle with 3 rows at its widest


# //////
# Booleans are True and False variables that can be used to control flow and check the status of executions. They are also used with loops, though this will be covered later.

# There are a few main ways to compare variables to determine True or false Status

# a == b    #checks whether a and b are the same value 
# a != b     # checks whether a and b are NOT the same value
# a >= b    # checks if a is greater than or equal to b (can also be used with < to check if a is less than or equal)
# a >b       # checks is a is greater than (and not equal) to b
# a is b     # checks whether the variables point to the same data 
# a ==b and a == c # and combines two booleans, both must be true to return true
# a==b or a == c # or combines two booleans, whether if either is true, it returns true 
# bool(a) # essentially casting a variable to a boolean type checks if it has a value:
# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.
# The following exercises require the writing of simple functions, so you may wish to return to the following exercises after reviewing the Python function content, if you are not familiar with functions.

# /////

# Write a function compare(a,b), that takes two integer variables, and returns the larger of the two values, or returns "these values are equal" if they are equal.

# For example:

# Test	                 Result

# print(compare (1,2))
#                            2
# print(compare (3,2))
#                        3
# print(compare (1,1))
# these values are equal
# Answer:(penalty regime: 10, 20, ... %)

def compare(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return "these values are equal"

# Test cases
print(compare(1, 2))
print(compare(3, 2))
print(compare(1, 1))

# /////

def bool_test(value):
    return bool(value)

# Test cases
print(bool_test("string")) # True
print(bool_test(30)) # True
print(bool_test([])) # False
print(bool_test(["a non empty","list"])) # True


# /////

def type_check(variable):
    if isinstance(variable, int):
        return "this variable type is: Integer"
    elif isinstance(variable, str):
        return "this variable type is: String"
    elif isinstance(variable, float):
        return "this variable type is: Float"
    elif isinstance(variable, list):
        return "this variable type is: List"
    else:
        return "this variable type is: " + str(type(variable)).split("'")[1]

# Test cases
print(type_check("Hello World!")) # this variable type is: String
print(type_check(123)) # this variable type is: Integer
print(type_check(1.11)) # this variable type is: Float
print(type_check(["i am a list!"])) # this variable type is: List

# I am wondering why the first one doesn't showed the right answer, while it works on my vs code properly. 
# on the previous exercise which was about loop i has the same problem

# //////

# create a simple function named double_input(input), which takes any input variable and returns that variable, times 2 

# "hello"*2 = "hellohello" 
# 2*2 = 4.


# For example:

# Test	Result
# print(double_input("Hello"))
# HelloHello
# print(double_input(2))
# 4
# print(double_input([1,2,3]))
# [1, 2, 3, 1, 2, 3]
# Answer:(penalty regime: 10, 20, ... %)

def double_input(input):
    return input * 2

# Test cases
print(double_input("Hello"))  # Should print "HelloHello"
print(double_input(2))        # Should print "4"
print(double_input([1, 2, 3]))  # Should print "[1, 2, 3, 1, 2, 3]"

# //////////////

# Write a python function accel_finder that uses the formula Force = Mass * Acceleration to find the exact acceleration of an object, given its mass and a force being applied to it, and then returns it



# For example:

# Test	Result
# print (accel_finder(10,2))
# 0.2
# print (accel_finder(10.1,6))
# 0.594059405940594
# print (accel_finder(1000000,8))
# 8e-06
# Answer:(penalty regime: 10, 20, ... %)
def accel_finder(mass, force):
    acceleration = force / mass
    return acceleration

# Test cases
print(accel_finder(10, 2))
print(accel_finder(10.1, 6))
print(accel_finder(1000000, 8))

# /////////////////////

# Write a function palindrome_test(str) which tests whether a given string is a palindrome
# (is the same forwards and backwards)

# For example:

# Test	Result
# print(palindrome_test("ABBA"))
# print(palindrome_test("The Who"))
# [True]
# [False]
# print(palindrome_test("ARcaaaaA"))
# print(palindrome_test("a"))
# print(palindrome_test("aA"))
# [False]
# [True]
# [False]
# Answer:(penalty regime: 10, 20, ... %)

def palindrome_test(str):
    # Remove spaces and convert to lowercase for uniform comparison
    cleaned_str = str.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return cleaned_str == cleaned_str[::-1]

# Test cases
print(palindrome_test("ABBA"))  # Should return True
print(palindrome_test("The Who"))  # Should return False
print(palindrome_test("ARcaaaaA"))  # Should return False
print(palindrome_test("a"))  # Should return True
print(palindrome_test("aA"))  # Should return True
