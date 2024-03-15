# Lambda functions are simple, one line functions that can be generated in python. They can be thought of as "tiny functions". Whether to use a lambda or a def is a matter of some debate, and generally speaking, using a def is better for readability, while using a lambda is better for speed, and size of code. The general structure of a lambda function is as follows

# x = lambda a : a + 10
# there are a few things to note:

# x = | this creates the name of a lambda, as x
# lambda |- this is the key word to tell python you are defining a lambda function. (like def declares a normal function)
# a : | this is the argument
# a+10 | this is the function body.
# print(x(5))
# >>>15

# Assume we have a list of tuples where each tuple contains a name and a score
scores = [('Anna', 95), ('Brad', 90), ('Charlie', 98), ('Diana', 87)]

# We want to sort this list by the score in descending order
# We can use a lambda function as the key to sorted() to achieve this
sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)

# The sorted list will be:
print(sorted_scores)  # Output: [('Charlie', 98), ('Anna', 95), ('Brad', 90), ('Diana', 87)]


# /////////////

# When used like this, you may ask "why use lambdas when ive just mastered functions? Arent they the same?"
# In the above format, the lambda function has a name, and therefore, yes, it is functionally very similar to a normal def function. However, the power of lambdas comes from their use as anonymous functions, i.e., they do not have to be named and declared, and can be returned as an output from another function.

# For example, lets say we have a function that takes one argument, and that argument will be multiplied by another unknown number. Using lambdas allows us to write the function body once, and return a lambda to be used for each specific output, e.g.:

# def my_func(n):
#   return lambda a : a * n

# my_doubler = my_func(2)
# my_tripler = my_func(3)

# print(my_doubler(11))
# print(my_tripler(10))
# Try it yourself in the below code-box, then remove the print statements, and create a "my_quadder" function.

# For example:

# Test	Result
# print(my_quadder(11))
# 44
# my_quintupler = my_func(5)
# print(my_quintupler(3))
# 15
# Answer:(penalty regime: 10, 20, ... %)
def my_func(n):
    return lambda a: a * n

# Now, create the "my_quadder" function by passing 4 to my_func
my_quadder = my_func(4)

# And also create the "my_quintupler" function by passing 5 to my_func
my_quintupler = my_func(5)


# /////
# Create three lambda functions in a row, called S,M, and D


# The first, S, should take three arguments, and add them together

# The second, M, should take three arguments, and multiply them together

# The third, D, should take two arguments, a and b, and divide them a/b.

# For example:

# Test	Result
# print(s(1,3,4))
# 8
# print (m(1,2,3))
# 6
# print (d(5,10))
S = lambda a, b, c: a + b + c
# Lambda function M multiplies three arguments
M = lambda a, b, c: a * b * c

# Lambda function D divides the first argument by the second
D = lambda a, b: a / b
print(S(1, 3, 4))  # This should print 8
print(M(1, 2, 3))  # This should print 6
print(D(5, 10))    # This should print 0.5

# //////////////

# Make a function that can be used to add any string to a string, surround it in a function called string_add(wordInput), and return a lambda function that takes another input, and adds wordInput to it.

# For example:

# Test	Result
# add_World= string_add("world!")
# print(add_World("hello "))
# hello world!
# add_World = string_add("morning!")
# print(add_World("Good "))
# Good morning!
# Answer:(penalty regime: 10, 20, ... %)

def string_add(wordInput):
    # Return a new lambda function that takes a string and appends wordInput to it
    return lambda s: s + wordInput

# Create a lambda function that appends "world!" to a string
add_World = string_add("world!")

# Create a lambda function that appends "Wide " and then "world!" to a string
add_World2 = string_add("Wide " + add_World(""))

# Create a lambda function that appends "Big " then "Wide " and then "world!" to a string
add_World3 = string_add("Big " + add_World2(""))

# Test the functions
print(add_World("hello "))    # Expected output: "hello world!"
# print(add_World2("hello "))   # Expected output: "hello Wide world!"
print(add_World3("Hello "))   # Expected output: "Hello Big Wide world!"
print(add_World3("Goodbye ")) # Expected output: "Goodbye Big Wide world!"

# /////////////////

# Another neat trick with lambdas is that you can use them to apply a sequence of functions to a variable, by storing a number of lambdas in a list, these can then be used easily by referencing the list index, e.g.:

func_list = [lambda a : a * 2, lambda a : a * 3,lambda a : a / 2]
print(func_list[1](2))
# What do you predict the output will be of this piece of code? Test it out to see if your prediction is correct!

# Using your knowledge of lists, loops, and lambdas, write a function; apply_lambdas(input_list, input_int),
# that takes an input_list consisting of lambdas, and an input_int to which each lambda function is applied in order, 
# and then return the total number as a float

# For example:

# Test	Result
# print(apply_lambdas([lambda a : a * 2, lambda a : a * 3,lambda a : a / 2], 3))
# 9.0
# print(apply_lambdas([lambda a : a * 2, lambda a : a * 3,lambda a : a / 2], 10))
# 30.0
# print(apply_lambdas([lambda a : a * 2, lambda a : a * 3,lambda a : a * 4], 3))
# 72.0
# print(apply_lambdas([lambda a : a * 2,lambda a : a * 2,lambda a : a * 2,lambda a : a * 2,lambda a : a * 2,lambda a : a * 2, lambda a : a * 2,lambda a : a * 2], 2))
# 512.0
# Answer:(penalty regime: 10, 20, ... %)

def apply_lambdas(input_list, input_int):
    result = input_int
    for func in input_list:
        result = func(result)
    return float(result)

# Test cases
print(apply_lambdas([lambda a: a * 2, lambda a: a * 3, lambda a: a / 2], 3))     # Should output 9.0
print(apply_lambdas([lambda a: a * 2, lambda a: a * 3, lambda a: a / 2], 10))    # Should output 30.0
print(apply_lambdas([lambda a: a * 2, lambda a: a * 3, lambda a: a * 4], 3))     # Should output 72.0
print(apply_lambdas([lambda a: a * 2, lambda a: a * 2, lambda a: a * 2, lambda a: a * 2, lambda a: a * 2, lambda a: a * 2, lambda a: a * 2, lambda a: a * 2], 2))    # Should output 512.0
