# Conditional Statements in Python--------------------------------

# 1. Definition ⭐----------------------
# A conditional statement is used to make decisions in a program based on whether a condition is True or False.

# 2. Types of conditional statements------------------
# * if statement
# *if-else statement
# *if-elif-else statement
# *Nested if statement

# 3. The if statement--------------------------
# Definition:-----------------------
# The if statement executes a block of code only when the condition is true.

# Syntax:------------------
# if condition:
#     statement

# Example:----------------
# age = 20
# if age >= 18:
#     print("Eligible to vote")   

# Output:------------
# Eligible to vote


# Explanation: Since 20 >= 18 is true, Python prints the message.


# Remember:
# : comes after the condition.
# Indentation (spaces before the statement) is important.
# ---------------------------------------------------------------------------------------------


# 2. If-Else Statement ⭐----------------------------

# Definition--------------------
# An if-else statement executes one block of code if the condition is true and another block if the condition is false.
# 
# Syntax----------------------
# if condition:
#     statement1
# else:
#     statement2


# Remember: else doesn't have a condition.


# Example 1: Positive or negative-----------------

# num = -5
# if num > 0:
#     print("Positive")
# else:
#     print("Negative")

# OUTPUT---------------------
# Negative


# Explanation:---------------
# num > 0 checks whether the number is greater than zero.
# Since -5 > 0 is False, Python executes the else block.
# Therefore, it prints Negative.


# Example 2: Voting eligibility---------------

# age = 16
# if age >= 18:
#     print("Eligible")
# else:
#     print("Not eligible")


# Output:
# Not eligible

# Because 16 is less than 18.

# Important theory question-----------------
# Q: What is the difference between if and if-else?
#     if: Executes code only when the condition is true.
#     if-else: Executes one block if true and another block if false.
# --------------------------------------------------------------------------
# 3. If-Elif-Else Statement ⭐--------------------------

# Definition-------------
# The if-elif-else statement is used to check multiple conditions and execute the block for the first condition that is true.
#
# Syntax-----------------------
# if condition1:
#     statement1
# elif condition2:
#     statement2
# else:
#     statement3


# if checks the first condition.
# elif means else if; it checks another condition if the earlier one was false.
# else executes when none of the previous conditions is true.


# Example: Check a person's score----------------------

# mark = 75
# if mark >= 90:
#     print("A Grade")
# elif mark >= 70:
#     print("B Grade")
# elif mark >= 50:
#     print("C Grade")
# else:
#     print("Fail")


# Output:
# B Grade


# Simple explanation---------------
# Is 75 >= 90? No.
# Is 75 >= 70? Yes!
# Python prints B Grade and skips the remaining conditions.


# Important: Python stops checking once it finds the first true condition.


# Theory question for your exam
# Q: What is the difference between if-else and if-elif-else?
#    if-else is used when there are two possible paths.
#    if-elif-else is used to check multiple conditions.
# -------------------------------------------------------------------
# __________________________________________________________________________________________________________
# ---------------------------------------------------------------------




























# # Find the sum of numbers from 1 to 100
# # sum=0
# # for i in range(1,101):
# #     sum=sum+i
# #     print(sum)

# ---------------------------------------

# for i in range(1,22,3):
#     print(i)

# ---------------------------------------------

# # Find the product of numbers from 1 to 10
# product=1
# for i in range(1,11):
#     product=product*i
#     print(product)

# ----------------------------------------------

# Print the multiplication table of a given number
# a=int(input("Enter a number "))
# for i in range(1,21):
#     table=a*i
#     print(table)
# -----------------------------------------------------

# a=int(input("Enter a number "))
# for i in range(1,10):
#     table=a*i
#     print(table)

# --------------------------------------------------

# for i in range(1,201):
#     if i % 4==0 and i % 8==0:
#         print(i)

# -------------------------------------------------

# Print all numbers between 1 and 100 that are divisible by 5 and 7
# # for i in range(1,101): 
# #     if i % 5==0 and i % 7==0:
# #         print(i)

# -----------------------------------------------------


# from 100 to 200 print only multiples of 10.
# for i in range(100,201,10):
#         print(i)

# ------------------------------------------------------

# Create a simple calculator using if elif else

# a=int(input("Enter the 1st number:"))
# b=int(input("Enter the 2nd numbetr:"))
# print("1.Addition")
# print("2.subtraction")
# print("3.division")
# print("4.multiplication")
# c=int(input("enter the number:"))
# if c==1:
#     print(a+b)
# elif c==2:
#     print(a-b)
# elif c==3:
#     print(a/b)
# elif c==4:
#     print(a*b)
# else:
#     print("error")       

# ---------------------------------------------

# n=int(input("Enter the number:")) 
# for i in range(2,n):
#     if n % i ==0:
#         print("not a prime number")
#     else:
#         print("prime number")

# ----------------------------------------------------
# 
# a=int(input("Enter the marks"))
# if(a>70 and a>=80):
#     print("a")
# elif a>=60 and a<=70:
#     print("b")
# elif a>=50 and a<=60:
#     print("c")
# elif a>=40 and a<=50:
#     print("d")
# elif a<=40: 
#     print("Fail")
# else:
#     print("Invalid")     

# ----------------------------------------------------
          
# a=int(input("Enter the marks"))
# if(a>150 and a<=200):
#     print("a")
# elif a>=110 and a<=150:
#     print("b")
# elif a>=80 and a<=110:
#     print("c")
# elif a>=50 and a<=80:
#     print("d")
# elif a<=50: 
#     print("Fail")
# else:
#     print("Invalid")     

# ----------------------------------------------


# largest= 0
# for i in range(101):
#     if i > largest:
#         largest = i
# print(largest)

# ----------------------------------------------

# for i in range(1,101):
#     if i % 3==0 and i % 5==0:
#         print("fizzbuzz")
#     elif i % 3==0:
#         print("fizz")
#     elif i % 5==0:
#         print("buzz")    
#     else:
#         print(i)    

# ----------------------------------------------

# smallest=0
# for i in range(0,101):
#     if(i<(i-1)):
#         smallest=i
# print=(smallest)



