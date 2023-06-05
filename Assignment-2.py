#!/usr/bin/env python
# coding: utf-8

# ## Basic Assignment 2

# 
# 1.What are the two values of the Boolean data type? How do you write them?
# Answer :->
#     The Boolean data type represents a logical value that can have one of two states: true or false.
#     These two values, true and false, are the only possible values for the Boolean data type. 
#     

# 2.What are the three different types of Boolean operators?
# Answer:->
#     The three basic types of Boolean operators are:
# 
#    AND Operator: The AND operator is used to combine multiple conditions or expressions. It returns true only if 
#    both conditions are true. In programming, it is often represented by the symbol "&&" or the keyword "AND".
#    For example,in the expression "A AND B," the result is true only if both A and B are true.
# 
#    OR Operator: The OR operator is used to combine multiple conditions or expressions. It returns true if at least one of 
#    the conditions is true. In programming, it is often represented by the symbol "||" or the keyword "OR".
#    For example, in the expression "A OR B," the result is true if either A or B (or both) is true.
# 
#    NOT Operator: The NOT operator is used to negate or reverse the value of a condition or expression. It returns true if 
#    the condition is false, and false if the condition is true. In programming, it is often represented by the symbol "!" or
#    the keyword "NOT". For example, in the expression "NOT A," the result is true if A is false and false if A is true.
#     

# 3.Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean
# values for the operator and what it evaluate)
# Answer:->
# 1.AND Operator (&&):
# 
# |   A   |   B   | A && B |
# |-------|-------|--------|
# | false | false | false  |
# | false | true  | false  |
# | true  | false | false  |
# | true  | true  | true   |
# 
# 2.OR Operator(||):
# 
# |   A   |   B   | A || B |
# |-------|-------|--------|
# | false | false | false  |
# | false | true  | true   |
# | true  | false | true   |
# | true  | true  | true   |
# 
# 3.NOT Operator(!):
# 
# |   A   |   !A  | 
# |-------|-------|
# | false | true  | 
# | true  | false | 
# 
# 
# 
# 

# 4.What are the values of the following expressions?
# (5 > 4) and (3 == 5)
# not (5 > 4)
# (5 > 4) or (3 == 5)
# not ((5 > 4) or (3 == 5))
# (True and True) and (True == False)
# (not False) or (not True)
# 
# Answer:->
#     (5 > 4) and (3 == 5) is False
#     not (5 > 4) is False
#     (5 > 4) or (3 == 5) is True
#     not ((5 > 4) or (3 == 5)) is False
#     (True and True) and (True == False) is False
#     (not False) or (not True) is True
#     
#     
#     

# 5.What are the six comparison operators?
# 
# Answer:->
#     The six comparison operators are:
# 
#    1.Equal to (==): This operator checks if two values are equal and returns true if they are, and false otherwise.
#    For example, 5 == 5 would evaluate to true, while 5 == 10 would evaluate to false.
# 
#    2.Not equal to (!=): This operator checks if two values are not equal and returns true if they are not, and false 
#    if they are equal. For example, 5 != 5 would evaluate to false, while 5 != 10 would evaluate to true.
# 
#    3.Greater than (>): This operator checks if the value on the left is greater than the value on the right, returning true
#    if it is, and false otherwise. For example, 10 > 5 would evaluate to true, while 5 > 10 would evaluate to false.
# 
#    4.Less than (<): This operator checks if the value on the left is less than the value on the right, returning true 
#    if it is, and false otherwise. For example, 5 < 10 would evaluate to true, while 10 < 5 would evaluate to false.
# 
#    5.Greater than or equal to (>=): This operator checks if the value on the left is greater than or equal to the value on 
#    the right, returning true if it is, and false otherwise. For example, 10 >= 5 would evaluate to true, while 5 >= 10
#    would evaluate to false.
# 
#    6.Less than or equal to (<=): This operator checks if the value on the left is less than or equal to the value on the 
#    right, returning true if it is, and false otherwise. For example, 5 <= 10 would evaluate to true, while 10 <= 5 
#    would evaluate to false.
#    
#    

# 6.How do you tell the difference between the equal to and assignment operators?Describe a
# condition and when you would use one.
# 
# Answer:->
#     To differentiate between the equal to (==) operator and the assignment (=) operator, it's important to understand 
#     their  respective purposes and contexts.
# 
#    Equal to (==) operator:
#    The equal to operator (==) is used for comparison. It checks if two values are equal and returns a Boolean value of 
#    true or false. It is typically used within conditional statements or expressions to compare values.
#    For example:
#        x = 5
#        y = 10
#        if x == y:
#          print("x is equal to y")
#        else:
#          print("x is not equal to y")
#          
#    Assignment (=) operator:
#    The assignment operator (=) is used to assign a value to a variable. It assigns the value on the right-hand side to
#    the variable on the left-hand side. 
#    For example:
#            x = 5
# 
# The equal to (==) operator is used for comparison, while the assignment (=) operator is used to assign a value to a variable. The equal to operator checks for equality between two values, whereas the assignment operator assigns a value to a variable.
# 
#    
#    

# 7.Identify the three blocks in this code:
# spam = 0
# if spam == 10:
# print('eggs')
# if spam > 5:
# print('bacon')
# else:
# print('ham')
# print('spam')
# print('spam')
# 
# Asnwer :-> Block1
# if spam == 10:
#     print('eggs')
# 
# Block2:
#     if spam > 5:
#         print('bacon')
#        
# Block3:
#     else:
#         print('ham')
#         print('spam')
#         print('spam')
#         
# 

# In[1]:


#8.Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
#Greetings! if anything else is stored in spam.

spam = 1 

if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")


# 9.If your programme is stuck in an endless loop, what keys you’ll press?
# 
# Answer:->
#         Ctrl + C: This key combination sends the KeyboardInterrupt signal to the running program, which interrupts its 
#         execution and raises a KeyboardInterrupt exception. When you press Ctrl + C, the program will terminate, allowing you 
#         to regain control.
#     By pressing Ctrl + C, you effectively send a signal to the Python interpreter to stop the program's execution. 
#     It's a common way to break out of an infinite loop or terminate a program that is taking too long to complete.
# 

# 10.How can you tell the difference between break and continue?
# Answer:->
#      "break" and "continue" are both control flow statements used within loops, but they serve different purposes.
# 
# "break" statement: When encountered within a loop (for loop or while loop), the "break" statement terminates the loop prematurely and transfers the execution to the statement immediately following the loop. It is often used to exit a loop early when a certain condition is met.
# Example:
#     for i in range(1, 10):
#     if i == 5:
#         break
#     print(i)
# 
# 
# "continue" statement: When encountered within a loop, the "continue" statement skips the rest of the current iteration and moves to the next iteration of the loop. It is useful when you want to skip certain iterations based on a condition. 
# Example:
#     for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)
# 

# 11.In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
# Answer:->
#     In a for loop, the expressions range(10), range(0, 10), and range(0, 10, 1) are all equivalent and produce the same sequence of numbers.
# 
# The range() function in Python generates a sequence of numbers starting from a specified start value (inclusive) and
# ending at a specified stop value (exclusive), with an optional step value that determines the increment between numbers.
# Here's the breakdown:
# 
# range(10): This expression generates a sequence of numbers from 0 to 9. The start value is omitted, so by default, 
# it starts from 0. The stop value is 10, but since it's exclusive, the sequence ends before reaching 10.
# 
# range(0, 10): This expression is explicitly specifying the start and stop values. It generates a sequence of numbers
# from 0 to 9, just like range(10).
# 
# range(0, 10, 1): This expression is explicitly specifying the start, stop, and step values. It generates a sequence of
# numbers from 0 to 9, with a step value of 1. Since the step value is 1, it increments by 1 in each iteration.

# In[1]:


#12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
#program that prints the numbers 1 to 10 using a while loop.
#Answer :->
    #program that prints the numbers 1 to 10 using a for loop

for i in range(1,11):
    print(i)
    


# In[2]:


#program that prints the numbers 1 to 10 using a while loop.
i=1
while i <= 10:
    print(i)
    i += 1


# 13.If you had a function named bacon() inside a module named spam, how would you call it after
# importing spam?
# 
# Answer:-> 
#     To call the bacon() function from the spam module after importing it, you would use the following syntax:
#    
#     import spam
#     spam.bacon()
# 
