#!/usr/bin/env python
# coding: utf-8

# 1.What is a lambda function in Python, and how does it differ from a regular function?
# 
# Answer:->
#     Lambda functions, also known as anonymous functions, are small and concise functions in Python that are defined without a name. They are typically used for one-time or simple operations where defining a regular function is unnecessary or would add unnecessary complexity.
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

# 2.Can a lambda function in Python have multiple arguments? If yes, how can you define and use them?
# 
# Answer:->
#         Yes, a lambda function in Python can have multiple arguments. You can define and use multiple arguments in a lambda 
#         function by separating them with commas within the parentheses.
#         
#         Example:
#             multiply = lambda x, y: x * y
#             result = multiply(5, 3)
#             print(result)  # Output: 15
#             
#    In this example, the lambda function multiply takes two arguments, x and y, and returns their product. The lambda function is defined using the lambda keyword, followed by the arguments separated by commas, a colon (:), and the expression (x * y).
# 
# To use the lambda function, you call it like a regular function and pass the required arguments (5 and 3 in this case). The result is stored in the variable result and printed, which outputs 15.
# 
# You can define lambda functions with any number of arguments by separating them with commas in the argument list. For example, a lambda function with three arguments would look like this:
# 
# my_function = lambda arg1, arg2, arg3: arg1 + arg2 + arg3
# 
#         

# 3.How are lambda functions typically used in Python? Provide an example use case.
# 
# Answer:->
#     
#    Lambda functions in Python are typically used in situations where a small, one-time function is needed, such as when working
#    with higher-order functions like map(), filter(), or reduce(). They are especially useful in functional programming 
#    paradigms or when a function needs to be defined quickly without the need for a separate named function.
#    
#    Example:
#        # Using lambda function with map()
#         numbers = [1, 2, 3, 4, 5]
#         squared_numbers = list(map(lambda x: x ** 2, numbers))
#         print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
#     In this example, the map() function applies a given function (in this case, a lambda function) to each element of the 
#     numbers list. The lambda function lambda x: x ** 2 squares each number in the list.
# 
# By passing the lambda function lambda x: x ** 2 as the first argument to map(), each element of the numbers list is squared, resulting in a new list squared_numbers containing the squared values.

# 4.What are the advantages and limitations of lambda functions compared to regular functions in Python?
# Answer:->
# 
# Lambda functions in Python have several advantages and limitations compared to regular functions. Let's explore them:
# 
# Advantages of Lambda Functions:
# 
# Concise and Readable Code: Lambda functions allow you to write compact and inline functions, reducing the overall code length and improving code readability.
# 
# Eliminates the Need for Named Functions: Lambda functions are anonymous, meaning they don't require a separate function name. This is useful for small, one-time operations where defining a named function is unnecessary and would add unnecessary complexity to the code.
# 
# Convenience in Functional Programming: Lambda functions are commonly used in functional programming paradigms where functions can be treated as first-class citizens. They can be easily passed as arguments to other functions like map(), filter(), or reduce().
# 
# Limitations of Lambda Functions:
# 
# Single Expression Limitation: Lambda functions can only contain a single expression. They are not designed to handle complex or multi-line operations. If you need to write a function with multiple statements or complex logic, a regular named function is more suitable.
# 
# Lack of Documentation: Lambda functions do not support docstrings, which are used to document regular functions. This can make it harder for other developers (or even yourself) to understand the purpose and usage of the function.
# 
# Limited Debugging: Debugging lambda functions can be more challenging since they don't have a specific name. If an error occurs within a lambda function, the traceback might not provide detailed information about the specific function causing the error.
# 
# Scope Limitations: Lambda functions have limited access to variables outside their own expression. They can only access global variables or variables passed as arguments. This can make them less flexible for more complex scenarios that require access to a wider scope.
# 
# Readability Trade-off: While lambda functions can make code more concise, they can also make it less readable if used excessively or inappropriately. Complex or nested lambda functions can make the code harder to understand and maintain.
# 
# 
# 

# 5.Are lambda functions in Python able to access variables defined outside of their own scope? Explain with an example.
# 
# Answer:->
#     Yes, lambda functions in Python can access variables defined outside of their own scope. However, this access is subject to the rules of variable scoping and depends on the specific situation.
# 
# In general, lambda functions can access variables from the enclosing scope (also known as the lexical scope) if those variables are accessible at the time the lambda function is defined. This behavior is known as "lexical closure" or "closure" in programming.
# 
# Example:
# 
# def outer_function():
#     x = 10
#     lambda_function = lambda y: x + y
#     return lambda_function
# 
# closure = outer_function()
# result = closure(5)
# print(result)  # Output: 15
# 
# In this example, the outer_function() defines a variable x with a value of 10. It then creates a lambda function lambda_function that takes an argument y and returns the sum of x and y. The lambda function accesses the x variable from its enclosing scope.
# 
# When outer_function() is called, it returns the lambda function lambda_function. This returned function is assigned to the variable closure.
# 
# Finally, the closure function is called with the argument 5, resulting in the sum of x and y (which is 10 + 5 = 15). The result is printed, and the output is 15.
# 

# In[5]:


#6.Write a lambda function to calculate the square of a given number.
square = lambda x: x**2
square(4)
   


# In[4]:


#7.Create a lambda function to find the maximum value in a list of integers.

find_maximum = lambda lst : max(lst)
lst = [2,5,1,10]
result = find_maximum(lst)
print(result)
  


# In[3]:


#8.Implement a lambda function to filter out all the even numbers from a list of integers.
filter_even = lambda lst : list(filter(lambda x: x%2 == 0,lst))
lst = [2,1,3,4,8]
filter_even(lst)
    
  


# In[2]:


#9.Write a lambda function to sort a list of strings in ascending order based on the length of each string.
sort_list = lambda lst: sorted(lst,key=lambda x:len(x))
lst=["apple", "banana", "cherry", "date", "elderberry"]
sort_list(lst)


# In[7]:


#10.Create a lambda function that takes two lists as input and returns a new list containing the common elements between the two lists.
common_elements = lambda lst1,lst2 : list(filter(lambda x: x in list2,list1))
list1 = [1,5,8,10]
list2 = [8,5,1,2,3]
common_elements(list1,list2)


# In[16]:


#11.Write a recursive function to calculate the factorial of a given positive integer.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
fact = int(input("Enter positive integer to calculate its factorial "))
factorial(fact)


# In[18]:


#12.Implement a recursive function to compute the nth Fibonacci number.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
fib = int(input("Enter number"))
fibonacci(fib)


# In[19]:


#13.Create a recursive function to find the sum of all the elements in a given list.
def list_sum(lst):
    if not lst:
        return 0
    else:
        return lst[0] + list_sum(lst[1:])
my_list = [1, 2, 3, 4, 5]
result = list_sum(my_list)
print(result) 


# In[2]:


#14.Write a recursive function to determine whether a given string is a palindrome.
def palindrome(str):
    if str == str[::-1]:
        return str + " is a Palindrome"
    else:
        return  str + " Not a Palindrome"
str = input("Enter a string to find wether it is a palindrome or not ")
palindrome(str)


# In[3]:


#15.Implement a recursive function to find the greatest common divisor (GCD) of two positive integers.
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
result = gcd(36, 48)
print(result)  # Output: 12

