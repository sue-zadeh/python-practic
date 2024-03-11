# As a reminder: collections are arrays or sequences of values. They can be any type, and any order. There are a number of built in collections in python, and different ways to reference elements within those sets.

# In general, the INDEX is used to denote the POSITION of an element within a collection, and python begins counting from 0, and negatives indicate "from the end" - e.g.: [0,1,2,3....-3,-2,-1]

# values may be printed that are contained within the collection, or the entire collection may be printed. There are many other functions available to collections that are not available to other data types, including sorting, reversing, and iterating. 


# Collection Types

# Uses	Example	 print(x) output	how to print 3	Important Notes
#  List	 A basic collection type for unmanaged lists	 x = [1,2,3,4,5]	 [1,2,3,4,5]	 print(x[2])	An unmanaged collection that retains its order, and can be modified
# Set	A collection that does not allow duplicates, and is unordered	x = {1,2,3,4,3,3,3,3}	 {1,2,3,4}	 Impossible to do easily - must print entire set, and/or convert to a list	A collection that does not retain its order, and removes all duplicates. The contents of a set must be of the type int , float , str , tuple or NoneType.
#  Tuple	 A collection that cannot be subsequently changed	 x = (1,2,3)	 (1,2,3)	  print(x[2])	A collection that is "immutable" which means it cannot be changed after creation.
# Dict	A collection made up of  Key:Value pairs	x = {"1st Key":"first value",  2:"Second Key", "Third Key":3, "1st Key":"New First Value", 4:3}	 {'1st Key': 'New First Value', 2: 'Second Key', 'Third Key': 3, 99: 3}	 print(x["Third Key"])
# OR
# print(x[99])
# A special set - all keys must be unique, and if repeated (e.g. "1st Key" in example) they are overwritten with the new value . Keys can be any of the following dataypes: int , float , str , tuple or NoneType
# Fun fact: int , float , str , tuple and NoneType are able to be used in sets because they are Hashable - in general that means that their hash value never changes during their lifetime - i.e., a 3 will always be the same 3, whereas a certain list [a,b,c] may change over the course of its life (even if all the elements contained within are hashable!). This is one of the most useful parts of a tuple - it is a hashable collection!
# Question 1Not yet answeredMarked out of 1.00Flag question
# Question text
# Select the variable assignments that are valid, assuming each line is being executed in an empty shell (no pre-assigned variables)

# Question 1Select one or more:

# a.
# x = {(1,):1}



# b.
# def = "hello"


# c.
# X = set("apple")
# X = "A"


# d.
# X = ["1",1,["1"]]


# e.
# X= list(str(int(str("1"))))


# f.
# x = {[1]:1}


# g.
# X = [a]


# h.
# X = [1]


# i.
# x = {1:[1]}


# j.
# x = [1,2,3,4,"test"]
# y = x[-2]

# big_y = x[y]

# Question 2Not yet answeredMarked out of 1.00Flag question
# Question text
# In Python, lists can only contain one data type at a time, eg only integers or only strings, but not both.

# Question 2Select one:
# True
# False

short_list = [7, 'a', 'b', 'c', 'd', 'e', "ten"]

# ///////

# Create a list called |set_list| that contains exactly 7 elements, that when cast to a set, will contain only 3 elements.

# For example:

# Test	                         Result
# print(len(set_list))
# print(len(set(set_list)))
#                                   7
#                                   3
# Answer:(penalty regime: 10, 20, ... %)

set_list = [1, 2, 3, 1, 2, 3, 1]
# /////////////

# Dictionaries are an excellent way to store and access information.

# Create a dictionary called list_dict which has N elements, where N is at least 5 . Create a new entry within this dictionary with a key called "dict_len", which has the value equal to the number of elements (N).

# For example:

# Test	Result
# print(len(list_dict) >= 5)
# print(list_dict["dict_len"] == len(list_dict))
# True
# True
# Answer:(penalty regime: 10, 20, ... %)

list_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}

# Add 1 to account for the new 'dict_len' key we're about to insert
list_dict["dict_len"] = len(list_dict) + 1


# ///////////////////

# Create a function; words_to_numbers(list); which takes in a list of strings,
# which are all integers, eg ["3","8","1"] and returns a list of integers; eg [3,8,1]
# For example:

# Test	Result
# print(words_to_numbers(["3","4","5"]))
# [3, 4, 5]
# Answer:(penalty regime: 10, 20, ... %)

def words_to_numbers(lst):
    return list(int(item) for item in lst)

# Test cases
print(words_to_numbers(["3"]))
print(words_to_numbers(["3", "4", "5"]))

# //////////////////

# Create a function element_counter(list, type) that counts and returns the number of elements in a list until an object of type is encountered, including the object itself. Remember, you can use the isinstance(obj,type) built in function to compare types.

# For example:

# Test	Result
# l = [10,20,30,(10,20),40]
# t = tuple
# print(element_counter(l,t))
# 4
# Answer:(penalty regime: 10, 20, ... %)
def element_counter(lst, t):
    count = 0
    for element in lst:
        count += 1  # Increment count for each element
        if isinstance(element, t):
            break  # Stop counting when an element of type t is encountered
    return count

# Test cases
l = [10, 20, 30, (10, 20), 40]
t = tuple
print(element_counter(l, t))  # Expected output: 4

l = [10, 20, 30, 10, 20, 40]
t = int
print(element_counter(l, t))  # Expected output: 1

l = [10, 20, 30, (10, 20), [40], 1, 2]
t = list
print(element_counter(l, t))  # Expected output: 6

# //////////////////

# It is relatively easy to rest whether a given collection is sorted, because if any pairwise
# comparison is not sorted, then by definition the entire list is not sorted.

# write a function check_sorted(list) which takes a list as an input, and returns 
# true if the list is sorted from smallest to largest, and false elsewise. Note that 
# any list with only 1 element is also considered sorted.



# For example:

# Test	Result
# print(check_sorted([1,2,3,4,5]))
# True
# print(check_sorted([5,4,3,2,1]))
# False
# print(check_sorted([1]))
# True
# print(check_sorted([2,1,4,51,5]))
# False
# Answer:(penalty regime: 10, 20, ... %)
def check_sorted(lst):
    # A list with 0 or 1 elements is always sorted
    if len(lst) < 2:
        return True
    # Iterate over the list checking if current element is greater than the next one
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

# Test cases
print(check_sorted([1, 2, 3, 4, 5]))  # Should return True
print(check_sorted([5, 4, 3, 2, 1]))  # Should return False
print(check_sorted([1]))              # Should return True
print(check_sorted([2, 1, 4, 5, 1]))  # Should return False
# ///////////////
# bubble sorting is a simple sorting algorithm that essentially compares each element to its neighbor to sort the list

# write a function bubble_sort(list), which takes a list, and returns a list sorted from smallest to largest elements. without using list.sort().

# the pseudocode for bubble sort is as follows, but you will have to write your own python code.

# input = list
# starting with i = 0
# compare i with i+1; if i > i+1, then swap those two elements. If not then no swapping occurs
# increment i by 1, and repeat step three.
# repeat until the end of the list is found (eg i=len(list)), this will place the largest element from the unsorted list, at the very end of the list.
# repeat until all elements have been sorted.
# return the sorted
# each time an element is swapped, print the list.



# For example:

# Test	Result
# nlist = ["A","C","B","a","c","b"]
# print(bubble_sort(nlist))
# ['A', 'B', 'C', 'a', 'c', 'b']
# ['A', 'B', 'C', 'a', 'b', 'c']
# ['A', 'B', 'C', 'a', 'b', 'c']
# nlist = [4,3,2,1]
# print(bubble_sort(nlist))
# [3, 4, 2, 1]
# [3, 2, 4, 1]
# [3, 2, 1, 4]
# [2, 3, 1, 4]
# [2, 1, 3, 4]
# [1, 2, 3, 4]
# [1, 2, 3, 4]
# Answer:(penalty regime: 10, 20, ... %)
# Check