# ==================================================
# TOPIC 5: TUPLES IN PYTHON
# ==================================================

# 1. Tuple
# Definition:
# A tuple is a collection of elements stored in a single variable.
# Tuples are ordered and immutable.
# Tuples allow duplicate values.

# Example:
fruits = ("apple", "banana", "mango")
print(fruits)

# Output:
# ('apple', 'banana', 'mango')


# ==================================================
# 2. Creating a Tuple
# ==================================================

# Definition:
# Tuples are created using parentheses ().

# Example:
numbers = (10, 20, 30, 40)
print(numbers)

# Output:
# (10, 20, 30, 40)


# ==================================================
# 3. Tuple with Different Data Types
# ==================================================

# Definition:
# A tuple can store different data types.

# Example:
data = ("Ananya", 20, 85.5, True)
print(data)

# Output:
# ('Ananya', 20, 85.5, True)


# ==================================================
# 4. Accessing Tuple Elements (Indexing)
# ==================================================

# Definition:
# Indexing is used to access individual tuple elements.
# Positive indexing starts from 0.
# Negative indexing starts from -1.

# Example:
fruits = ("apple", "banana", "mango")

print(fruits[0])
print(fruits[1])
print(fruits[-1])

# Output:
# apple
# banana
# mango


# ==================================================
# 5. Tuple Slicing
# ==================================================

# Definition:
# Slicing is used to access a part of a tuple.

# Syntax:
# tuple[start:stop:step]

# Example:
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
print(numbers[:3])
print(numbers[::2])

# Output:
# (20, 30, 40)
# (10, 20, 30)
# (10, 30, 50)

# Remember:
# The stop index is not included.


# ==================================================
# 6. Tuple Immutability
# ==================================================

# Definition:
# Tuples are immutable, which means their elements
# cannot be changed after creation.

# Example:
numbers = (10, 20, 30)
# numbers[0] = 100  # This causes a TypeError.

print(numbers)

# Output:
# (10, 20, 30)


# ==================================================
# 7. Creating a Single-Element Tuple
# ==================================================

# Definition:
# A single-element tuple must contain a comma.

# Example:
a = (10,)
print(type(a))

# Output:
# <class 'tuple'>

# Remember:
# (10) is an integer, not a tuple.
# (10,) is a tuple.


# ==================================================
# 8. len() Function
# ==================================================

# Definition:
# len() returns the number of elements in a tuple.

# Example:
numbers = (10, 20, 30, 40)
print(len(numbers))

# Output:
# 4


# ==================================================
# 9. count() Method
# ==================================================

# Definition:
# count() returns how many times a value appears in a tuple.

# Example:
numbers = (10, 20, 10, 30, 10)
print(numbers.count(10))

# Output:
# 3


# ==================================================
# 10. index() Method
# ==================================================

# Definition:
# index() returns the index of the first occurrence of a value.

# Example:
numbers = (10, 20, 30, 20)
print(numbers.index(20))

# Output:
# 1


# ==================================================
# 11. Tuple Concatenation
# ==================================================

# Definition:
# Concatenation means joining two tuples using +.

# Example:
a = (10, 20)
b = (30, 40)

print(a + b)

# Output:
# (10, 20, 30, 40)


# ==================================================
# 12. Tuple Repetition
# ==================================================

# Definition:
# The * operator repeats tuple elements.

# Example:
numbers = (1, 2)
print(numbers * 3)

# Output:
# (1, 2, 1, 2, 1, 2)


# ==================================================
# 13. Membership Operators
# ==================================================

# Definition:
# in checks whether an element exists in a tuple.
# not in checks whether an element does not exist.

# Example:
numbers = (10, 20, 30)

print(20 in numbers)
print(50 not in numbers)

# Output:
# True
# True


# ==================================================
# 14. Looping Through a Tuple
# ==================================================

# Definition:
# A loop can access each tuple element one by one.

# Example:
fruits = ("apple", "banana", "mango")

for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# mango


# ==================================================
# 15. Tuple Packing
# ==================================================

# Definition:
# Tuple packing means storing multiple values in one tuple.

# Example:
student = "Ananya", 20, "Python"
print(student)

# Output:
# ('Ananya', 20, 'Python')


# ==================================================
# 16. Tuple Unpacking
# ==================================================

# Definition:
# Tuple unpacking means assigning tuple elements
# to separate variables.

# Example:
student = ("Ananya", 20, "Python")

name, age, course = student

print(name)
print(age)
print(course)

# Output:
# Ananya
# 20
# Python


# ==================================================
# 17. Converting a List into a Tuple
# ==================================================

# Definition:
# tuple() converts an iterable, such as a list, into a tuple.

# Example:
numbers = [10, 20, 30]
result = tuple(numbers)

print(result)

# Output:
# (10, 20, 30)


# ==================================================
# 18. Converting a Tuple into a List
# ==================================================

# Definition:
# list() converts a tuple into a list.

# Example:
numbers = (10, 20, 30)
result = list(numbers)

print(result)

# Output:
# [10, 20, 30]


# ==================================================
# 19. Important Points to Remember
# ==================================================

# 1. Tuples use parentheses ().
# 2. Tuples are ordered.
# 3. Tuples are immutable.
# 4. Tuples allow duplicate values.
# 5. Tuples can contain different data types.
# 6. Indexing starts from 0.
# 7. count() counts occurrences of a value.
# 8. index() returns the first matching index.
# 9. A single-element tuple requires a comma.
# 10. list() converts a tuple into a list.
# 11. tuple() converts a list into a tuple.


# ==================================================
# 20. Difference Between List and Tuple
# ==================================================

# List:
# 1. Uses square brackets [].
# 2. Mutable (can be changed).
# 3. Example: numbers = [10, 20, 30]

# Tuple:
# 1. Uses parentheses ().
# 2. Immutable (cannot be changed).
# 3. Example: numbers = (10, 20, 30)


# ==================================================
# 21. Practical Questions
# ==================================================

# Easy:
# 1. Create a tuple of five numbers and print it.
t=(1,2,3,4,5,6)
print(t)
# 2. Print the first element of a tuple.
t=(1,2,3,4,5,6)
print(t[0])
# 3. Find the length of a tuple.
t=(1,2,3,4,5,6)
print(len(t))

# Medium:
# 4. Count how many times 10 appears in a tuple.
t=(10,20,30,40,50,10,60,10)
print(t.count(10))
# 5. Convert a tuple into a list.
t=(1,2,3,4,5,6)
l=list(t)
print(l)
# 6. Unpack a tuple into three variables.
t=(1,2,3)
a,b,c=t
print(a)
# Hard:
# 7. Find the largest element in a tuple.
t = (10, 50, 20, 80, 30)
print("Largest element:", max(t))
# 8. Check whether a value exists in a tuple.
t = (10, 20, 30, 40, 50)
n = int(input("Enter a number: "))

if n in t:
    print("Value exists")
else:
    print("Value does not exist")
# 9. Join two tuples and print the result.
t1 = (10, 20, 30)
t2 = (40, 50, 60)

t3 = t1 + t2
print(t3)

# ------------------------------------------------------------------------------------------------------------------------------
























































# # COLLECTION VARIABLE: LIST, TUPLE, SET, DICTIONARY--->(can store multiple datatypes)
# # ordered ,immutable,allow duplicate values,can store different data types, cannot append(done by converting to list and then change to tuple)

# t=(1,2,3)
# print(t[0])
# print(t[-1])

# t=(8,10,"hello",6.8,8)
# print(t)

# # Tuple Operations
# a=(1,2)
# b=(3,4)
# print(a+b)
# print(a*2) # 2 times a tuple repeated
# print(t.count(8))

# # to add a new item in to tuple
# # first convert into list and add item and convert into tuple and print
# t=(1,2,3)
# l=list(t)
# l.append(4)
# t=tuple(l)
# print(t)

# t=(0,6,7,8)
# l=list(t)
# l.pop(2)#index position
# t=tuple(l)
# print(t)

# t=(6,8,7,3,4)
# l=list(t)
# l.remove(7)
# l.remove(8)#element
# t=tuple(l)
# print(t)