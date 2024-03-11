# Recursion and looping are two ways that you can make your program perform the same task a certain number of times. This quiz focuses on the two main python loop types, While and For.

# While loops continue executing for as long as a boolean condition is true.
# For loops execute over a collection or other iterable data, performing an operation with each piece of data from the collection.
# Remembering your basic boolean and conditionals, there are a few key parts of a loop.
# While Loops:

i = 1          #Creates a variable
print("Starting the loop now!")                 #a debugging print statement                 
while i < 6:   #continues executing for as long as i is less than six
    print(i)       #prints out the value of i in the current loop
    i += 1         #adds one to the variable i
    if i == 4:     #if i is four
        continue         #continue causes the loop to stop executing, and restart (ie go back to the top)
    if i == 3:           #if the value of I is three
        print("i equals three")       #print
    print("I finished a loop!")       #notice the indentation - this is no longer within the if statement.
else:                                    #this else statement occurs when the loop condition is no longer true
    print("i is now larger than five")

print ("The loop successfully finished")         #a debugging print statement
# There is also one other statement, the break which will immediately terminate the loop and move on to the next code.

# Try to answer the following questions about this loop - if you're struggling, then just try running it (it will tell you the answers!)
i = 0   
print(i)
while i <= 10:
    if i == 1:
        print(str(i)+"st loop")
    if i == 2:
        print(str(i)+"nd loop")
    if i == 3:
        print(str(i)+"rd loop")
    if i > 3:
        print(str(i)+"th loop")
    if i == 5:
        break
    i+= 1
print(i)
 
# What is the value of i at the end of the loop

# 
# /////

# modify this loop with the following requirements:

# i = 0
# while i <= 10:
#     if i == 1:
#         print(str(i)+"st loop")
#     if i == 2:
#         print(str(i)+"nd loop")
#     if i == 3:
#         print(str(i)+"rd loop")
#     if i > 3:
#         print(str(i)+"th loop")
#     if i == 5:
#         break
#     i+= 1

# requirements

# Wrap the entire loop within a function foo_looper(n) which takes any integer input
# allow the loop to start from n
# allow the loop to run from n to 10
# when i equals 9 print "second to last loop" after printing "9th loop"
# For example:

# Test	Result
# foo_looper(0)
# 1st loop
# 2nd loop
# 3rd loop
# 4th loop
# 5th loop
# 6th loop
# 7th loop
# 8th loop
# 9th loop
# second to last loop
# 10th loop
# foo_looper(3)
# 3rd loop
# 4th loop
# 5th loop
# 6th loop
# 7th loop
# 8th loop
# 9th loop
# second to last loop
# 10th loop
# foo_looper(10)
# 10th loop
# Answer:(penalty regime: 10, 20, ... %)

def foo_looper(n):
    for i in range(n, 11):  # Start from n to 10
        if i == 1:
            print(str(i) + "st loop")
        elif i == 2:
            print(str(i) + "nd loop")
        elif i == 3:
            print(str(i) + "rd loop")
        else:
            if i != 0:  # Skip printing for i=0
                print(str(i) + "th loop")
        if i == 9:  # Special message for the second to last loop
            print("second to last loop")
        if i == 10:  # Stop the loop after printing for 10
            break
# ////////////////
def foo_bounded_while(start, end):
    while start <= end:
        print(start)
        start **= 2
    print(start)  # Print the final value, which is larger than end
# ///////////

# There are some syntax errors and some logic errors in this code.

# Note that 'non-negative' includes zero.

# Hint:  You might find it easiest to paste this into VS Code first, to highlight errors and test the code, then paste your corrected code into the answer box below.

print("Please input two non-negative numbers and I'll add them up for you!\n")

try:
    first_number = float(input("Please enter your first number: "))
    second_number = float(input("Please enter your second number: "))
    
    if (first_number >= 0 and second_number >= 0):
        print("The result of adding your numbers together is: " + str(first_number + second_number))
    else:
        print("At least one of those numbers was not positive, please try again. Goodbye!")
except ValueError:
    print("You did not enter valid numbers. Please run the program again and enter numbers only.")

# //////

# A function in python is a named block of code that executes when "called". In python the syntax for creating a function is simple:

# def function_name(variable_input):
#     #This is my first function!

#     print("I am running my function!")

#     variable_output = variable_input + " Werld!"

#     return(variable_output)


# printing_var = function_name("Hello")
# print(printing_var)
# Copy and paste the code above into your python development environment, and execute it to see the output. the exact explanation of each keyword is described below

# 1: def function_name(input_variable):
# def is the keyword in python to tell the interpreter that you are about to create a new function

# function_name can be any name that can be assigned to a variable (non-protect, and not starting with a number), and is how you will subsequently reference the function. 

# input_variable is a variable that is passed into the function when it is called. This can be any value, including variables - however it is up to the function what values are useful

# Note that the parentheses, spaces, and colon are all vital. After the function is defined, and until the function is finished, all code is "indented" with four spaces.

# 2:     #This is my first function
# This line is prefaced by a # character, which tells python to not execute any of the subsequent code. Usually comments are used to help increase readability and understanding of your code. Note that the four spaces are still used.
# 3:    print("I am running my function!")
# This line is a print statement, as you have seen before. It is no different when executed within a function.
# 4:    variable_output = variable_input + " Werld!"
# This line is the first "functional" line in our function. It takes the input of the function (variable_input) and performs an action on it (adds the string " Werld!")
# 5:    return(variable_output)
# The return statement is likely one of the most important in functions, and finishes the block of code, returning the variable in the parentheses to where ever the function has been called for
# 6:printing_var = function_name("Hello")
# This line is the first time the function is actually executed, with the caller being the variable - printing_var, which is assigned to the value in the return statement of the function - function_name. 
# 7:print(printing_var)
# This line sends the variable printing_var to the std output, with the value "Hello Werld!"

# Question 1Not completeMarked out of 1.00Flag question
# Question text
# Using the following code, Copy and paste it into Visual Studio Code, and 

# correct the spelling mistake, so that the function returns any string input, with " world!" attached. Remember to double check cases and spaces.
# remove the print statement, so the only message in the output channel is variable_input + " world!"
# def function_name(variable_input):
#     #This is my first function!

#     print("i am running my function!")

#     variable_output = variable_input + " werld!"

#     return variable_output

# For example:

# Test	                                 Result
# print(function_name("Hello"))
#                                        Hello world!
# Answer:(penalty regime: 10, 20, ... %)

def function_name(variable_input):
    #This is my first function!
    variable_output = variable_input + " world!"
    return variable_output

# Test the function
print(function_name("Hello"))

# ////

# Python functions can have multiple inputs simply by separating them with a comma within the function definition:

# def function(var1,var2):
#     print (var1)
#     return(var2)


# Write a python function, multiple_input(var1,var2), that accepts an integer as the first variable, and a list as the second variable, and first prints the list, and then returns value at position var1 from list var2.

# For example:

# Test	Result
# print(multiple_input(0,[1,2,3,4]))
# [1, 2, 3, 4]
# 1
# print(multiple_input(2,["var1","var2","var3","var4"]))
# ['var1', 'var2', 'var3', 'var4']
# var3
# print(multiple_input(-1,[1,2,3,4]))
# [1, 2, 3, 4]
# 4
# Answer:(penalty regime: 10, 20, ... %)

def multiple_input(var1, var2):
    print(var2)
    return var2[var1]


# ////


# Create a function; square_times(var_one,var_two) which accepts any two integer or float inputs, and first finds the square of var_one , and then multiples that result by var_two, and returns that value.

# Hint:  Use ** operator to raise a value to the power, e.g. xy is x**y

# For example:

# Test	Result
# print(square_times(3,9))
# 81
# print(square_times(-3,2))
# 18
# Answer:(penalty regime: 10, 20, ... %)

def square_times(var_one, var_two):
    return (var_one ** 2) * var_two

# Test cases
print(square_times(1, 2))  # Should output 2
print(square_times(3, 9))  # Should output 81
print(square_times(-3, 2)) # Should output 18

# /////

# Using your knowledge of sets and lists, write a function uniques(list), that takes a list as an input, prints the list, and then returns a set containing only the unique elements from that list.

# For example:

# Test	Result
# print(uniques([1,2,3]))
# [1, 2, 3]
# {1, 2, 3}
# print(uniques([1,1,1,3,2,2,3,2,3]))
# [1, 1, 1, 3, 2, 2, 3, 2, 3]
# {1, 2, 3}
# Answer:(penalty regime: 10, 20, ... %)
def uniques(lst):
    print(lst)
    return set(lst)

# Test cases
print(uniques([1, 2, 3]))
print(uniques([1, 1, 1, 3, 2, 2, 3, 2, 3]))

# ////////////

# Although discouraged in other courses and classes, within coding searching for answers that have already been written is highly recommended.  Some of the most useful sites are 

# ws3schools
# stackoverflow
# the python language documentation


# It is important that as you search you read through the code and attempt to understand each line.

# A prime number if a number that is only divisible(without remainder) by itself, and 1. Write a function to check whether a number is a prime. 

# Using google, try to find some code that has already been written, that can be used to check if some integer input is a prime number. Read a few results and either find one that fits the following signature, or adapt an existing solution, (or write your own if you're feeling confident!).

# The function should be named test_prime(n) where n is an integer, and the function should return either True (if n is a prime) or False(if n is not). This test should also work for 1(Not a Prime), and 2(is a prime).

# N.B. this is a hard question, and it is not expected that you fully understand it - it is primarily designed to teach you to google and adapt existing code.

# For example:

# Test	                           Result
# print(test_prime(5))
#                                  True
# print(test_prime(4))
#                                   False
# print(test_prime(1))
#                                   False



def test_prime(n):
    if n <= 1:
        return False  # 1 and numbers less than 1 are not prime numbers
    if n == 2:
        return True   # 2 is the only even prime number
    if n > 2 and n % 2 == 0:
        return False  # All other even numbers are not primes

    # Check for factors other than 1 and n
    for current in range(3, int(n ** 0.5) + 1, 2):  # Only test up to the square root of n
        if n % current == 0:
            return False
    return True

# Test cases
print(test_prime(5))  # Should return True
print(test_prime(4))  # Should return False
print(test_prime(1))  # Should return False


# /////////


# Write a function called fizzbuzz that takes one (integer) parameter and returns "fizz" if it is divisible by 5, "buzz" if it is divisible by 7 and "fizzbuzz" if it is divisible by both 5 and 7, if the number is not divisible by either, then the number that was input should be returned.



# Just past your function into the answer box

# Answer:(penalty regime: 10, 20, ... %)

def fizzbuzz(n):
    if n % 5 == 0 and n % 7 == 0:
        return "fizzbuzz"
    elif n % 5 == 0:
        return "fizz"
    elif n % 7 == 0:
        return "buzz"
    else:
        return n
