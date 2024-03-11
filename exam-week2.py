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
