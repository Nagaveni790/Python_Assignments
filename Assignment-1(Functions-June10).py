#!/usr/bin/env python
# coding: utf-8

# 1.In Python, what is the difference between a built-in function and a user-defined function? Provide an example of each.
# 
# Answer:->
#     In Python, a built-in function is a function that is already provided as part of the Python programming language. These functions are readily available and can be used without the need for any additional import or declaration. 
#     On the other hand, a user-defined function is a function that is created by the user to perform a specific task or set of tasks.
#     
#     Example:Built-in function
#     
#     result = len("Hello, world!")
#     print(result)  # Output: 13
#     
#    In the above example, the len() function is a built-in function that calculates the length of a given string. It returns the number of characters in the string.
#    
#    Example:User defined function
#    
#    def add_numbers(a, b):
#        return a + b
# 
#    result = add_numbers(5, 3)
#    print(result)  # Output: 8
#  
#    In this example, we define a user-defined function called add_numbers(). It takes two parameters, a and b, and returns their sum. We then call the function with arguments 5 and 3, and the function returns the result 8.

# 2.How can you pass arguments to a function in Python? Explain the difference between positional arguments and keyword arguments.
# 
# Answer:->
#     In Python, you can pass arguments to a function by specifying them within the parentheses when calling the function. There are two ways to pass arguments: positional arguments and keyword arguments.
# 
# Positional Arguments:
#  Positional arguments are passed to a function based on their position or order. The values you provide when calling the function are assigned to the corresponding parameters in the order they appear in the function's parameter list.
#  Example:
#      def greet(name, age):
#         print("Hello,", name)
#         print("You are", age, "years old")
# 
#      greet("Alice", 25)
#      
#    In this example, the function greet() takes two positional arguments: name and age. When calling the function, we provide the values "Alice" and 25. The first argument "Alice" is assigned to the name parameter, and the second argument 25 is assigned to the age parameter.
# 
# Keyword Arguments:
#        Keyword arguments are passed to a function by specifying the parameter name followed by the corresponding value. This way, the order of the arguments does not matter.
#        
#    Example:
#          def greet(name, age):
#             print("Hello,", name)
#             print("You are", age, "years old")
# 
#          greet(age=25, name="Alice")
#     
#    In this example, we pass the arguments using their parameter names: age=25 and name="Alice". The function matches the arguments to the parameters based on their names, allowing us to provide the arguments in any order.
# 

# 3.What is the purpose of the return statement in a function? Can a function have multiple return
# statements? Explain with an example.
# 
# Answer:->
#         The purpose of the return statement in a function is to specify the value or values that the function should output or return to the caller. It allows the function to provide a result that can be used for further computations or stored in a variable.
# 
# The return statement also serves another important role: it terminates the execution of the function. When a return statement is encountered, the function immediately exits, and any code after the return statement is not executed.
# 
# Yes, a function can have multiple return statements. Once a return statement is executed, the function exits immediately, regardless of whether there are more return statements or code after the initial return statement. This means that only one return statement is executed during the execution of the function.
# 
# Example:
#     def absolute_value(num):
#         if num < 0:
#             return -num
#         else:
#             return num
# 
#     result1 = absolute_value(5)
#     result2 = absolute_value(-7)
# 
#     print(result1)  # Output: 5
#     print(result2)  # Output: 7
# 
# In this example, the absolute_value() function takes a number as an argument. It checks if the number is less than 0. If it is, the function returns the negation of the number (-num). Otherwise, if the number is greater than or equal to 0, it simply returns the number itself.
# 
# When we call the function absolute_value(5), the argument 5 is not less than 0, so the else block is executed, and the function returns 5. When we call the function absolute_value(-7), the argument -7 is less than 0, so the if block is executed, and the function returns -7.

# 4.What are lambda functions in Python? How are they different from regular functions? Provide an
# example where a lambda function can be useful.
# 
# Answer:->
#     
#    Lambda functions, also known as anonymous functions, are small and concise functions in Python that are defined without a name. They are typically used for one-time or simple operations where defining a regular function is unnecessary or would add unnecessary complexity.
#    
#    General syntax of a lambda function:
#        lambda arguments: expression
# 
# Lambda functions can take any number of arguments but must contain only a single expression. The expression is evaluated and returned as the result of the lambda function.
# 
# Lambda functions are different from regular functions in a few ways:
# 
# Syntax: Lambda functions are defined using the 'lambda' keyword, followed by a colon (':') to separate the arguments from the expression. Regular functions are defined using the 'def' keyword, followed by the function name, parentheses for arguments, and a block of code.
# 
# Name: Lambda functions are anonymous, meaning they don't have a specific name. Regular functions, on the other hand, have a name that can be used to call them.
# 
# Scope: Lambda functions are limited to their own expression and do not have access to variables outside the expression unless explicitly passed as arguments. Regular functions have access to variables in their defined scope and can use them within their code block.
# 
# 
# Lambda functions are particularly useful in situations where a small, one-time function is needed, such as when using higher-order functions like map(), filter(), or reduce(). They can also be used as function arguments or in situations where a function needs to be defined quickly without defining a separate named function.
# 
# Example:
# 
#     multiply = lambda x, y: x * y
#     result = multiply(5, 3)
#     print(result)  # Output: 15
#     
#   In this example, we define a lambda function multiply that takes two arguments, x and y, and returns their product. We then call the lambda function with arguments 5 and 3, and it returns the result 15.

# 5.How does the concept of "scope" apply to functions in Python? Explain the difference between local
# scope and global scope.
# 
# Answer:->
#     The concept of "scope" in Python refers to the visibility or accessibility of variables within different parts of the code. In Python, variables defined inside a function have local scope, while variables defined outside any function (at the module level) have global scope. Understanding scope is crucial for determining where variables can be accessed and modified.
#     
#   Local Scope:
#         Variables defined within a function have local scope. They are only accessible within the function where they are 
#         defined. These variables cannot be accessed outside the function or by other functions unless explicitly passed as
#         arguments or returned as function results.
#    
#    Example:
#    def my_function():
#        x = 10
#        print(x)  # Output: 10
# 
#    my_function()
#    print(x)  # Raises NameError: name 'x' is not defined
#    
#   In this example, the variable x is defined within the my_function() function. It can be accessed and used within the function, but outside the function, trying to access x raises a NameError because the variable is not defined in the global scope.
#  
#   Global Scope:
#         Variables defined outside any function, at the module level, have global scope. They are accessible throughout the 
#         module, including within functions. Global variables can be accessed and modified from any part of the module,
#         including inside functions.
#         
#        Example:
#            x = 10
#            def my_function():
#                print(x)  # Output: 10
# 
#            my_function()
# 
#    In this example, the variable x is defined outside the function. It can be accessed within the my_function() function without any issues. The function has access to global variables by default.
# 

# 6.How can you use the "return" statement in a Python function to return multiple values?
# 
# Answer:->
#     In Python, the return statement in a function can be used to return multiple values by returning them as a tuple, a list, or any other iterable object. By grouping multiple values together, you can effectively return multiple values from a function.
#     
#     Example:
#         def get_person_info():
#             name = "Alice"
#             age = 25
#             country = "USA"
#             return name, age, country
# 
#         person_info = get_person_info()
#         print(person_info)  # Output: ('Alice', 25, 'USA')
#         
#    In this example, the get_person_info() function retrieves and returns three pieces of information: name, age, and country. Instead of returning them individually, we group them together separated by commas in the return statement. This creates a tuple containing the values name, age, and country. When the function is called and the return statement is encountered, the tuple is returned as a single value.
# 

# 7.What is the difference between the "pass by value" and "pass by reference" concepts when it comes to function arguments in Python?
# 
# Answer:->
#         The concepts of "pass by value" and "pass by reference" are not applicable in the same way as in some other programming 
#         languages. Instead, Python uses a concept called "pass by assignment" or "pass by object reference" to handle function
#         arguments
#         
#      In Python, when you pass an object as an argument to a function, a reference to that object is passed. The assignment of the reference to a parameter creates a new reference to the same object. Therefore, modifications to the object's state inside the function can be visible outside the function.
# 
# To understand this concept better, let's consider two scenarios:
# 
#    Immutable Objects (e.g., numbers, strings, tuples):
#             When you pass an immutable object to a function, such as a number or a string, the function receives a copy of the 
#             value. Any modifications made to the parameter inside the function will not affect the original object.
#             
#             Example:
#                 def modify_immutable(num):
#                     num += 1
# 
#                 x = 10
#                 modify_immutable(x)
#                 print(x)  # Output: 10
#                 
#    In this example, the function modify_immutable() takes an integer argument num. When the argument x is passed to the
#    function, a copy of the value 10 is made, and the parameter num refers to that copy. Any modifications made to num inside
#    the function do not affect the original value of x.
# 
# 
#   Mutable Objects (e.g., lists, dictionaries):
#             When you pass a mutable object to a function, such as a list or a dictionary, the function receives a reference to 
#             the object. Modifying the object's state inside the function will affect the original object.
#             
#             Example:
#                 def modify_mutable(my_list):
#                     my_list.append(4)
# 
#                 my_list = [1, 2, 3]
#                 modify_mutable(my_list)
#                 print(my_list)  # Output: [1, 2, 3, 4]
#                 
#    In this example, the function modify_mutable() takes a list argument my_list. When the list my_list is passed to the
#    function, a reference to the original list is passed. The parameter my_list refers to the same list object. Therefore, 
#    modifications made to my_list inside the function will be reflected in the original list.

# 8.Create a function that can intake integer or decimal value and do following operations:
# a. Logarithmic function (log x)
# b. Exponential function (exp(x))
# c. Power function with base 2(2x)
# d. Square root
# 
# Answer :->
#     import math
#     def perform_operations(x):
#         result= {}
#         result['logarithm'] = math.log(x)
#         result['Exponential'] = math.exp(x)
#         result['power'] = math.pow(2,x)
#         result['square_root'] = math.sqrt(x)
#         return result
#     perform_operations(4)
#     
#     #output:
#   {'logarithm': 1.3862943611198906,
#  'Exponential': 54.598150033144236,
#  'power': 16.0,
#  'square_root': 2.0}

# 9.Create a function that takes a full name as an argument and returns first name and last name.
# 
# Answer:->
#     def extract_firstLast(full_name):
#         name = full_name.split()
#         first_name = name[0]
#         last_name = name[-1]
#         return first_name,last_name
#     full_name = input("Enter a full name")
#     extract_firstLast(full_name)
#     
#     
