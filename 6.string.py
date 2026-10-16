# ==================================================
# TOPIC 3: STRINGS IN PYTHON
# ==================================================

# 1. String
# Definition:
# A string is a sequence of characters enclosed in
# single quotes, double quotes, or triple quotes.

# Example:
name = "Ananya"
print(name)

# Output:
# Ananya


# ==================================================
# 2. Creating a String
# ==================================================

# Definition:
# A string can be created using single, double,
# or triple quotation marks.

# Example 1:
a = 'Hello'
print(a)

# Output:
# Hello

# Example 2:
b = "Python"
print(b)

# Output:
# Python

# Example 3:
c = """Welcome to Python"""
print(c)

# Output:
# Welcome to Python


# ==================================================
# 3. String Indexing
# ==================================================

# Definition:
# Indexing is used to access individual characters
# in a string.

# Remember:
# Positive indexing starts from 0.
# Negative indexing starts from -1.

# Example:
name = "Python"

print(name[0])
print(name[1])
print(name[5])

# Output:
# P
# y
# n

# Negative indexing example:
print(name[-1])
print(name[-2])

# Output:
# n
# o


# ==================================================
# 4. String Slicing
# ==================================================

# Definition:
# Slicing is used to access a part of a string.

# Syntax:
# string[start:stop:step]

# Example:
name = "Python"

print(name[0:3])
print(name[2:6])
print(name[:4])
print(name[::2])

# Output:
# Pyt
# thon
# Pyth
# Pto

# Explanation:
# The stop index is not included.


# ==================================================
# 5. len() Function
# ==================================================

# Definition:
# The len() function returns the number of characters
# in a string.

# Example:
name = "Python"
print(len(name))

# Output:
# 6


# ==================================================
# 6. lower() Method
# ==================================================

# Definition:
# The lower() method converts all letters to lowercase.

# Example:
name = "PYTHON"
print(name.lower())

# Output:
# python


# ==================================================
# 7. upper() Method
# ==================================================

# Definition:
# The upper() method converts all letters to uppercase.

# Example:
name = "python"
print(name.upper())

# Output:
# PYTHON


# ==================================================
# 8. capitalize() Method
# ==================================================

# Definition:
# The capitalize() method converts the first character
# to uppercase and the remaining letters to lowercase.

# Example:
name = "hello PYTHON"
print(name.capitalize())

# Output:
# Hello python


# ==================================================
# 9. title() Method
# ==================================================

# Definition:
# The title() method converts the first letter of
# each word to uppercase.

# Example:
name = "i love python"
print(name.title())

# Output:
# I Love Python


# ==================================================
# 10. strip() Method
# ==================================================

# Definition:
# The strip() method removes spaces from the beginning
# and end of a string.

# Example:
name = "  Hello  "
print(name.strip())

# Output:
# Hello


# ==================================================
# 11. replace() Method
# ==================================================

# Definition:
# The replace() method replaces one part of a string
# with another.

# Syntax:
# string.replace(old, new)

# Example:
name = "I like Java"
print(name.replace("Java", "Python"))

# Output:
# I like Python


# ==================================================
# 12. find() Method
# ==================================================

# Definition:
# The find() method returns the index of the first
# occurrence of a character or substring.
# It returns -1 if the value is not found.

# Example:
name = "Python"
print(name.find("t"))
print(name.find("z"))

# Output:
# 2
# -1


# ==================================================
# 13. count() Method
# ==================================================

# Definition:
# The count() method returns how many times a
# character or substring occurs.

# Example:
name = "banana"
print(name.count("a"))

# Output:
# 3


# ==================================================
# 14. String Concatenation
# ==================================================

# Definition:
# Concatenation means joining two or more strings.

# Example:
a = "Hello"
b = "Python"

print(a + " " + b)

# Output:
# Hello Python


# ==================================================
# 15. String Repetition
# ==================================================

# Definition:
# The * operator repeats a string a specified number
# of times.

# Example:
name = "Hi "
print(name * 3)

# Output:
# Hi Hi Hi


# ==================================================
# 16. Checking Membership
# ==================================================

# Definition:
# The in operator checks whether a character or
# substring exists in a string.

# Example:
name = "Python"

print("P" in name)
print("z" in name)

# Output:
# True
# False


# ==================================================
# 17. String Immutability
# ==================================================

# Definition:
# Strings are immutable, which means their individual
# characters cannot be changed directly after creation.

# Example:
name = "Python"
# name[0] = "J"  # This causes a TypeError.

# Correct way:
name = "J" + name[1:]
print(name)

# Output:
# Jython


# ==================================================
# 18. Important Points to Remember
# ==================================================

# 1. A string stores a sequence of characters.
# 2. Indexing starts at 0 for the first character.
# 3. Negative indexing starts at -1 for the last character.
# 4. Slicing extracts a part of a string.
# 5. len() returns the length of a string.
# 6. lower() converts letters to lowercase.
# 7. upper() converts letters to uppercase.
# 8. Strings are immutable.
# 9. The stop index in slicing is not included.
# 10. Strings can be joined using +.


# ==================================================
# 19. Practical Questions
# ==================================================

# Easy:
# 1. Create a string and print it.
s="hi"
print(s)
# 2. Find the length of "Hello".
name="hello"
print(len(s))
# 3. Convert "PYTHON" to lowercase.
s="PYTHON"
print(s.lower())

# Medium:
# 4. Print the first and last characters of "Python".
s="python"
print(s[0])
print(s[-1])
# 5. Reverse a string using slicing.
s="hi"
print(s[::-1])
# 6. Replace "Java" with "Python" in a string.
s="I love java"
print(s.replace("java","python"))

# Hard:
# 7. Count the vowels in a string.
s = input("Enter a string: ")
count = 0

for ch in s.lower():
    if ch in "aeiou":
        count += 1

print("Number of vowels:", count)
# 8. Check whether a string is a palindrome.
s = input("Enter a string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
# 9. Count how many times a character appears in a string.
s = input("Enter a string: ")
ch = input("Enter a character: ")

count = s.count(ch)
print("Occurrences:", count)

















































# s="hello "
# print(s[4])
# print(s[7])
# print(s[-3])
# print(s[-2:-6:-1])
# print(s[3:6])
# print(s[::-2])
# print(s[::-1])
# print(s[::1])
# # ---------------------------
# a="welcome home"
# print(a)
# print(len(a))
# print(a.capitalize())
# print(a.upper())
# print(a.lower())
# print(a.isupper())
# print(a.islower())
# print(a.index('l'))
# print(a.index('m',5))
# print(a.count('o'))
# print(a.count('e'))

# # ----------------------------------
# x="  hjsgfwieuhwe  hfjkwhiw"
# print(x.strip())
# print(x.startswith('t'))
# print(x.startswith(' '))

# f="good morning"
# print(f.replace("morning","afternoon"))
# print(f)

# print('{:<10}{:<10}'.format('hello','world')) # left align
# print('{:>10}{:>10}'.format('hello','world')) # right align
# print('{:^10}{:^10}'.format('hello','world')) # centre align
# print('{:>10}{:<10}'.format('hello','world')) # left and right

# -----------------------------

# b= "Enter a string"
# chr="Enter a character"
# count=0
# reverse=" "

# print(b.replace(" ","-"))
# print(b.find(chr))
# print(len(b))
# c="aeiousdg"
# for i in c:
#     if i in 

# print("number of vowels",count)
# print(b.count(chr))
# print(reverse)
# -------------------------------------
# print(b.upper())

# ---------------------------------------
# b = input("Enter a string: ")
# reverse = ""

# for chr in b:
#     reverse = chr + reverse

# if b == reverse:
#     print("Palindrome")
# else:
#     print("Not a palindrome")
# *****************************************

s="python full stack"
print(s.replace(" ","-"))
# ***************************************
s="python full stack"
print(s.replace(" ",""))
# ******************************************
s=input("Enter sentence:")
print(s.title())