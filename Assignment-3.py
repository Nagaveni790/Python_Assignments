#!/usr/bin/env python
# coding: utf-8

# 1.Why are functions advantageous to have in your programs?
# Answer:-> 
#     Functions are advantageous to have in programs for several reasons:
#    1.Reusability: Functions allow you to write modular and reusable code. Once you define a function, you can call it multiple
#     times from different parts of your program without duplicating the code. This saves time and effort by promoting code
#     reuse and helps to keep your codebase organized and manageable.
# 
#    2.Abstraction: Functions provide a level of abstraction, allowing you to encapsulate a set of operations or logic into
#     a single entity. This abstraction hides the implementation details of the function, making the code more readable and 
#     easier to understand. When you use functions, you can focus on what the code does rather than how it does it.
# 
#    3.Code organization and maintainability: Functions help in organizing your code by breaking it down into smaller, self-
#    contained units. Each function can be responsible for a specific task, making it easier to understand and maintain. 
#    When a function needs modification or bug fixing, you can focus on that specific function without affecting other 
#    parts of the program.
# 
#    4.Debugging and troubleshooting: Functions make it easier to debug and troubleshoot your code. By isolating specific 
#    functionality within functions, you can test and debug them individually. This helps in identifying and fixing issues
#    more efficiently as you can narrow down the problem to a specific function, rather than having to search through the 
#    entire program.
# 
#    5.Readability and comprehension: Well-defined functions with clear names and a single responsibility make the code more 
#    readable and comprehensible. Functions can serve as self-documenting units of code, providing information about what they 
#    do based on their names and parameters.
# 
#    6.Collaboration: Functions facilitate collaboration among developers working on the same codebase. By breaking down a
#    program into functions, different team members can work on different functions simultaneously. This modular approach 
#    promotes better teamwork, as developers can work independently on their assigned tasks while ensuring the integration
#    of their functions into the larger program.
# 
# 
# 

# 2.When does the code in a function run: when it&#39;s specified or when it&#39;s called?
# Answer :->
#     The code within a function runs when the function is called. When you define a function, you are essentially creating a 
#     blueprint or a set of instructions for a particular task. The code inside the function is not executed until you explicitly
#     call the function in your program.
# 
#    To execute the code within a function, you need to invoke or call the function by using its name followed by parentheses().
#    The parentheses can optionally contain arguments or inputs that you pass to the function if it expects any.
#    
#    Example: 
#        #Function Definition
#        def hello():
#            print("Hello ineuron.ai")
#        #function call
#        hello()

# 3.What statement creates a function?
# Answer:->
#     To create a function, you use the def statement. The def statement is short for "define" and is specifically designed to
#     define functions.
#     
#     Here is the general syntax for creating a function:
#     
#     def function_name(arguments):
#     # Function body (code)
#     # ...
#     # ...
# 

# 4.What is the difference between a function and a function call?
# Answer:->
#         Function: A function is a named block of reusable code that performs a specific task. It encapsulates a set of 
#         instructions and can accept inputs (arguments) and optionally return a value. Functions are typically defined using a
#         specific syntax in programming languages, such as the def statement in Python.
# 
#    Whereas,Function call: A function call, also known as invoking or executing a function, is the act of using a defined 
#    function in your code to execute its instructions. When you make a function call, you specify the function name followed by
#    parentheses (). The parentheses may contain arguments (inputs) that are passed to the function if it expects any
#     

# 5.How many global scopes are there in a Python program? How many local scopes?
# Answer:->
#     In a Python program, there is typically one global scope and multiple local scopes.
# 
#    Global Scope: The global scope is the outermost scope in a Python program. It exists throughout the entire program and is 
#    accessible from any part of the code. Variables defined in the global scope are called global variables and can be accessed 
#    and modified from within functions or other scopes. Global variables are accessible both inside and outside functions.
# 
#    Local Scopes: Local scopes are created whenever a function is called or when certain control structures are used(like loops 
#    or conditional statements). Each time a function is called, a new local scope is created. Variables defined within a local 
#    scope are called local variables and are only accessible within that specific scope or the inner scopes nested within it. 
#    Local variables are typically used for temporary storage within functions and have no effect on variables in other scopes.
#    
#    Here's an example to illustrate the concept of global and local scopes:
#    global_variable = 10  # Global variable in the global scope
# 
# def my_function():
#     local_variable = 20  # Local variable in the local scope of my_function
#     print(local_variable)  # Accessing the local variable
#     print(global_variable)  # Accessing the global variable
# 
# my_function()  # Function call
# print(global_variable)  # Accessing the global variable outside the function
# 

# 6.What happens to variables in a local scope when the function call returns?
# 
# Answer:->
#     When a function call returns, the local variables in the local scope are deallocated from memory and cease to exist. 
#     These variables are specific to the function's execution and are not accessible outside the function.
# 
#    Here's what happens step by step when a function call returns:
# 
#    The function execution completes or encounters a return statement.
#    The function call returns control to the point where it was called.
#    The local scope of the function is destroyed, and all the variables defined within that scope are deallocated.
#    The program continues executing from the point where the function was called.
#    After the function call returns, any attempt to access the local variables from outside the function will result in an error 
#    or undefined behavior because those variables are no longer in scope. They have been removed from memory, and their values 
#    are no longer available.

# 7.What is the concept of a return value? Is it possible to have a return value in an expression?
# Answer:->
#     The concept of a return value refers to the value that a function can send back to the caller once its execution completes.
#     When a function is called, it can perform computations, manipulate data, or execute various operations. The return value 
#     allows the function to provide the result or outcome of its execution to the caller.
# 
#    A return value is specified using the return statement within a function. It typically follows the return keyword and is 
#    often an expression or variable that represents the desired result. When the return statement is encountered during the 
#    function's execution, the function stops executing, and the control flow is returned to the point where the function was 
#    called. The returned value is then available for further use by the caller.
#    
#    Example:
#    
#    def add_numbers(a, b):
#     result = a + b
#     return result
# 
#    sum_result = add_numbers(5, 3)
#    print(sum_result)

# 8.If a function does not have a return statement, what is the return value of a call to that function?
# Answer:->
#     If a function does not have a return statement, or if it reaches the end of the function without encountering a return 
#     statement, the function is considered to have an implicit return value of None. 'None' is a special built-in value in 
#     Python that represents the absence of a value or the lack of a meaningful result
#    
#    Here's an example to demonstrate the implicit return value of None:
#    
#    def greet(name):
#     print(f"Hello, {name}!")
# 
#    result = greet("Alice")
#    print(result)
#    
# 
# In this example, the greet() function takes a parameter name and prints a greeting message using that name. However, there is no explicit return statement in the function. When the function is called with the argument "Alice", it prints the greeting message but does not return any value. As a result, the variable result is assigned the value of None, and when it is printed, None is displayed.

# 9.How do you make a function variable refer to the global variable?
# Answer:->
#     To make a function variable refer to a global variable, you can use the global keyword to explicitly indicate that you want
#     to access or modify the global variable within the function scope. By using the global keyword, you inform Python that the 
#     variable being referenced is the same global variable and not a local variable with the same name.
#     
#    Example to demonstrate how to make a function variable refer to a global variable:
#    
#    count = 0  # Global variable
# 
#    def increment_count():
#      global count  # Declare 'count' as a global variable
#      count += 1    # Modify the global variable
# 
#    print(count)         # Output: 0
#    increment_count()
#    print(count)  # Output: 1
#    
#    In this example, the count variable is defined as a global variable outside the function. Within the increment_count() function, the global keyword is used to indicate that count is a global variable and not a local variable. This allows the function to access and modify the global variable directly.
# 
# After calling increment_count(), the value of the count global variable is incremented by 1. The subsequent print statement shows the updated value of count as 1

# 10.What is the data type of None?
# Answer:->
#     In Python, the data type of None is called NoneType. None represents the absence of a value or the lack of a meaningful
#     result. It is often used to indicate that a variable or expression does not have a specific value assigned.
# 
#    The NoneType is a built-in type in Python, and None is the sole value of that type. It is considered a singleton object, 
#    meaning that there is only one instance of None in a Python program.
#    
#    Example:
#        result = None
#        print(result)             # Output: None
#        print(type(result))       # Output: <class 'NoneType'>
#        print(result is None)     # Output: True
#        
#        

# 11.What does the sentence import areallyourpetsnamederic do?
# Answer:->
#     The sentence "import areallyourpetsnamederic" does not have any standard meaning or functionality in Python. In Python, the 
#     import statement is used to import modules, which are separate Python files containing reusable code. The 
#     "areallyourpetsnamederic" portion in the sentence does not correspond to any recognized module or Python syntax.
#     But if you create a module called "areallyourpetsnamederic" then it imports all the functions of "areallyourpetsnamederic" 
#     module. Otherwise,it will result in a ModuleNotFoundError because there is no module named "areallyourpetsnamederic" in the 
#     Python standard library or any other commonly used libraries.

# 12.If you had a bacon() feature in a spam module, what would you call it after importing spam?
# 
# Answer:->
#     If you have imported the "spam" module in your Python program and it contains a bacon() function, you can call the function by using its name directly after importing the module.
# 
# example:
# 
#    import spam
#    spam.bacon()
# 
# 
# In this example, the spam module is imported, and the bacon() function is called using spam.bacon(). The spam module acts as a namespace, and you can access the bacon() function within that namespace using the dot (`.`) operator.
# 
# Alternatively, you can use the "from" import statement to import the "bacon()" function directly without specifying the module name each time you call it. This allows you to call the function directly without referencing the module name.
# 
# example using the from import statement:
# 
# from spam import bacon
# bacon()
# 
# 
# In this example, the "bacon()" function is imported directly from the "spam" module using "from spam import bacon". After the import, you can call the "bacon()" function directly without referencing the module name.
# 
# 

# 13.What can you do to save a programme from crashing if it encounters an error?
# 
# Answer:->
# To save a program from crashing when it encounters an error, you can implement error handling techniques using exception handling. Exception handling allows you to catch and handle specific errors or exceptions that may occur during program execution, preventing the program from terminating abruptly.
# 
# In Python, you can use a try-except block to handle exceptions. The code within the try block is executed, and if an exception occurs, it is caught by the except block. By handling exceptions appropriately, you can execute alternative code or take corrective actions to prevent the program from crashing.
# 
# Example:
#     try:
#       # Code that may raise an exception
#       x = 10 / 0  # Division by zero - raises a ZeroDivisionError
#       print("This line will not be executed.")
#     except ZeroDivisionError:
#       # Exception handling code
#       print("An error occurred: Division by zero.")
# 

# 14.What is the purpose of the try clause? What is the purpose of the except clause?
# Answer:->
#     The try clause in Python is used to enclose a block of code that may potentially raise an exception. It allows you to specify code that you want to monitor for exceptions. The purpose of the try clause is to safeguard the code within it and handle any exceptions that may occur during its execution.
# 
# The try clause works together with the except clause. If an exception occurs within the try block, the execution of the try block is immediately halted, and the program flow jumps to the corresponding except clause.
# 
# The purpose of the except clause is to define the actions or code that should be executed when a specific exception occurs within the associated try block. It allows you to catch and handle specific exceptions, providing a way to gracefully recover from errors or perform alternative actions.
# 
# Example:
#     try:
#      # Code that may raise an exception
#      # ...
#     except ExceptionType:
#      # Code to handle the specific exception
#      # ...
# 
