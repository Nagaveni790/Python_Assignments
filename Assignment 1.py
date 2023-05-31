#!/usr/bin/env python
# coding: utf-8

# 1. In the below elements which of them are values or an expression? eg:- values can be
# integer or string and expressions will be mathematical operators.
# *
# 'hello'
# -87.8
# -
# /
# +
# 6
# 
# Answer:-> * is an expression 
# 'hello' is a value
# -87.8 is a value because its a float value
# - is an expression
# / is an expression
# + is an expression
# 6 is a value since its a integer
# 
# 

# 2.What is the difference between string and variable?
# 
# Answer:->  A variable is a named storage location in a computer's memory that can hold a value.
#            It is used to store and manipulate data in a program.
#            Example : "age" that stores a person's age, and you can change its value as needed.
#         
#           Whereas,  String is sequence of characters enclosed in quotation marks(single or double). 
#           a string is a specific data type used to represent textual data, such as words, sentences, or characters.
#           Example:-> str = "This is a string"
#                     in above example str is a variable and characters within double quotes is string.
#                 

# 3.Describe three different data types.
# 
# Answer :-> 
#     Data type is a classification that specifies the type of data that variable or expression can hold.
#     Since, Python is a dynamically-typed programming language we don't have to declare variable data types explicitly.he data       type is automatically inferred based on the value assigned to the variable.
#     
#     Python supports several built in data types including:
#     1. Numeric Types
#     2. Sequence Types
#     3. Mapping Types
#     4. Set Types
#     5. Boolean Types
#     6. None Types
#    
#    *Numeric Types: This type contains numeric values which can be int or float values.
#    
#    *Sequence Types : This contains character values which can be in the form of string,list and tuple,
#    where,
#    string represents strings of characters, such as "hello" or "Python".
#    list: Represents an ordered collection of items, enclosed in square brackets ([]),
#    such as [1, 2, 3] or ['apple', 'banana',   'orange'].
#    tuple: Similar to lists but immutable (cannot be modified once created), enclosed in parentheses (()),
#    such as (1, 2, 3) or ('a', 'b', 'c').
#     
#    *Mapping types: This includes dictionary which represents a collection of key-value pairs, enclosed in curly braces ({}), 
#    such as {'name': 'John', 'age': 25}.
#    
#    *Set Types: This includes sets which represents an unordered collection of unique elements, enclosed in curly braces ({}), 
#    such as {1, 2, 3} or {'apple', 'banana', 'orange'}.
#    
#    *Boolean Type: Represented as bool which is either True or False.
#    
#    *None Type: None: Represents the absence of a value or a null value
#    
#   

# 4.What is an expression made up of? What do all expressions do?
# Answer :-> 
#        An expression is a combination of values, variables, operators, and function calls that can be evaluated to produce 
#        a result. In programming, expressions are used to perform computations and represent values or conditions.
#        
#        
#   The primary purpose of an expression is to compute a value based on the provided inputs. Expressions can be used in various contexts, such as assigning values to variables, passing arguments to functions, or determining conditions in control structures (e.g., if statements, loops). They allow you to perform calculations, make decisions, and manipulate data within a program.

# 5.This assignment statements, like spam = 10. What is the difference between an
# expression and a statement?
# 
# Answer:-> 
#     An expression is a combination of values, variables, operators, and function calls that can be evaluated to produce a result. It typically yields a value.Expressions can be used within statements to compute values, make decisions, or perform calculations.
#     On the other hand, Statement is a complete unit of code that performs an actions or control the flow of execution.It represents a specific instruction or operation to be carried out. 
#     Assignment statements, like "spam = 10", are a type of statement that assign a value (in this case, 10) to a variable (spam). 

# 6.After running the following code, what does the variable bacon contain?
# bacon = 22
# bacon + 1
# 
# answer :-> 
#     After running the above code, the variable bacon contains value 22. Since we are just incrementing the bacon variable with expression +1 so which results the output 23.
# 

# 7.What should the values of the following two terms be?
# 'spam' + 'spamspam'
# 'spam' * 3
# 
# Answer:->
#      -> 'spam' + 'spamspam': This expression concatenates the two strings 'spam' and 'spamspam', 
#      resulting in the string 'spamspamspam'. The value of this expression is 'spamspamspam'.
# 
#    -> 'spam' * 3: This expression multiplies the string 'spam' by 3, which means repeating the string three times.
#       The result is the string 'spamspamspam'. The value of this expression is also 'spamspamspam'.
# 
# In both cases, the resulting value is the same, 'spamspamspam', but they are achieved using different operations. The + operator concatenates strings, while the * operator repeats a string a specified number of times.

# 8.Why is eggs a valid variable name while 100 is invalid?
# 
# Answer:-> 
#     In programming, variable names need to follow certain rules and conventions. 
#     Here are some guidelines for valid variable names:
# 
#    1.Valid characters: Variable names can contain letters (a-z, A-Z), digits (0-9), and underscores (_). 
#     However, they cannot start with a digit.
# 
#    2.No reserved words: Variable names cannot be the same as reserved words or keywords in the programming language. 
#    For example, you cannot use "if," "for," or "while" as variable names.
# 
# Based on these guidelines, "eggs" is a valid variable name because it consists of only letters and does not violate any rules or clash with reserved words.
# 
# However, "100" is an invalid variable name because it starts with a digit. Variable names must begin with a letter or an underscore. Starting with a digit would lead to confusion because it could be mistaken for a number, causing potential issues in the code.
# 
# It's important to choose meaningful and descriptive variable names that adhere to the rules of the programming language you are using. This helps improve code readability and maintainability.
# 
# 
# 
# 

# 9.What three functions can be used to get the integer, floating-point number, or string
# version of a value?
# 
# Answer :->
#     To convert a value to different data types, you can use the following three functions:
#     
#    1.int() :This function can be used to convert a value to an integer data type. 
#     It takes a value as an argument and returns the integer representation of that value. 
#     If the value cannot be converted to an integer, a ValueError will be raised.
#    
#    2.float() :This function can be used to convert a value to float data type. It takes a value as an argument and returns
#    the float representation of that value.
#    If the value cannot be converted to float, a ValueError will be raised.
#    
#    3.str() : This function converts a value to a string data type. It takes a value as an argument and returns a
#    string representation of that value. It is commonly used to convert numbers or other data types to a string
#    for concatenation or display purposes.

# 10.Why does this expression cause an error? How can you fix it?
# 'I have eaten' + 99 + 'burritos.'
# 
# Answer:-> This expression 'I have eaten'+ 99 +'burritos' causes TypeError since here we are trying to concatenate string with integer which is not allowed in string, To fix this error you can ensure that all the values being concatenated are of the same data type, which in this case is a string. One way to achieve this is by converting the integer to a string before concatenation.
# Here's an updated version of the expression that fixes the error:
# 'I have eaten ' + str(99) + ' burritos.' 
