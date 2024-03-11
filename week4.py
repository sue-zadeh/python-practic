# Lambda functions are simple, one line functions that can be generated in python. They can be thought of as "tiny functions". Whether to use a lambda or a def is a matter of some debate, and generally speaking, using a def is better for readability, while using a lambda is better for speed, and size of code. The general structure of a lambda function is as follows

# x = lambda a : a + 10
# there are a few things to note:

# x = | this creates the name of a lambda, as x
# lambda |- this is the key word to tell python you are defining a lambda function. (like def declares a normal function)
# a : | this is the argument
# a+10 | this is the function body.
# print(x(5))
# >>>15