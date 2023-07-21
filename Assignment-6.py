#!/usr/bin/env python
# coding: utf-8

# 1.What are keywords in python? Using the keyword library, print all the python keywords.
# Answer:->
#     Keywords in Python are reserved words that have special meanings and predefined functionality within the programming 
#     language. These keywords are part of the Python syntax and cannot be used as identifiers(variable names,function names,etc)
# 
# To print all the Python keywords, you can use the keyword library and its kwlist attribute. Here's an example:
# 
# import keyword
# all_keywords = keyword.kwlist
# print(all_keywords)
# 

# 2.What are the rules to create variables in python?
# Answer:->
#     In Python, variables are used to store and reference data. To create variables in Python, you need to follow these rules:
# 
# *Variable Naming:
# Variable names can contain letters (a-z, A-Z), digits (0-9), and underscores (_).
# The first character of a variable name cannot be a digit.
# Variable names are case-sensitive, meaning myVariable and myvariable are considered different variables.
# It is recommended to use descriptive and meaningful names to enhance code readability.
# Avoid using reserved keywords as variable names (e.g., if, for, while, etc.).
# 
# *Variable Assignment:
# Variables are assigned using the assignment operator (=).
# The assignment statement assigns a value to a variable, creating it if it doesn't exist.
# For example: x = 10 assigns the value 10 to the variable x.
# 
# *Datatypes:
# Python is dynamically typed, which means you don't need to declare the type of a variable explicitly.
# The type of a variable is determined by the value assigned to it.
# Variables can hold values of various data types, such as numbers, strings, lists, dictionaries, etc.
# 
# *Variable Reassignment:
# Variables can be reassigned to new values using the assignment operator (=).
# The new value can be of the same or a different data type.
# For example: x = 5; x = 'Hello'; x = [1, 2, 3] are valid reassignments of the variable x.

# 3.What are the standards and conventions followed for the nomenclature of variables in
# python to improve code readability and maintainability?
# 
# Answer:->
#     1.Use descriptive names: Choose variable names that are meaningful and describe the purpose or content of the variable.
#       This makes it easier for others (and your future self) to understand the code.
#     2.Use lowercase with underscores: For most variables, use all lowercase letters with underscores to separate words. 
#       This is known as snake_case.
#     3.Avoid single-letter names: Except for simple loop counters, avoid using single-letter variable names. 
#       Using descriptive names makes the code more self-explanatory.
#     4.Be consistent: Stick to a consistent naming style throughout your codebase. Consistency in naming helps readers
#       to quickly understand the code.
#     5.Use meaningful abbreviations: It's okay to use abbreviations if they are widely understood and add clarity.
#       Avoid cryptic abbreviations that might confuse readers.
#     6.Avoid reserved words: Don't use Python's reserved keywords (e.g., if, for, while, def, etc.) as variable names.
#     7.Use plural for collections: When naming collections (e.g., lists, sets, dictionaries), use plural names to indicate 
#       that they contain multiple items.
#     8.Constants in UPPERCASE: If you have constants, use UPPERCASE_WITH_UNDERSCORES for naming them.

# 4.What will happen if a keyword is used as a variable name?
# 
# Answer:->
#     If you use a Python keyword as a variable name, you will encounter a syntax error. Python keywords are reserved words 
#     that have specific meanings and functionalities in the language.
#     
#     Example: 
#         if = 10  # Trying to use "if" as a variable name
# 
#     # The above line will raise a syntax error:
#     # SyntaxError: invalid syntax

# 5.For what purpose def keyword is used?
# 
# Answer:->
#         The def keyword in Python is used to define user-defined functions. Functions are blocks of code that perform a 
#         specific task and can be called multiple times throughout the program. Using functions allows you to break down your 
#         code into smaller, more manageable pieces, promoting code reusability and organization.
#         
#         Example:
#             def add_numbers(a, b):
#                 sum_result = a + b
#                 return sum_result
# 
#             result = add_numbers(5, 10)
#             print(result)  # Output: 15
# 

# In[ ]:


6.What is the operation of this special character ‘\’?

Answer:->
        The special character '\' is known as the backslash or escape character.
        It serves several purposes and is used to represent certain special sequences in strings and characters.
        When the backslash is combined with other characters, it creates escape sequences that have specific meanings.
        
    1.Escape sequences in strings: The backslash is used to escape certain characters within strings that have special meanings. For example:

        '\n': Represents a newline character.
        '\t': Represents a tab character.
        '\': Represents a literal backslash character.
        \': Represents a single quote within a single-quoted string.
        \": Represents a double quote within a double-quoted string.
        
        Example:
                print("Hello\nWorld")
            # Output:
            # Hello
            # World

            print('I\'m learning Python.')
            # Output:
            # I'm learning Python.

        
    2.Raw strings: By prefixing a string with r or R, you can create a raw string.
      In a raw string, backslashes are treated as literal characters, and escape sequences are not interpreted.
        Example:
                print(r"C:\Users\user\Documents")
                # Output: C:\Users\user\Documents
                
    3.Unicode escape sequences: The backslash '\u' is used to represent Unicode characters using their hexadecimal code.
       
        Example:
                print('\u03B1')  # Greek letter alpha (α)
                # Output: α
    
    4.Line continuation: The backslash can be used to split long lines of code into multiple lines.
        
        Example:
            total = 10 + 20 + 30 +             40 + 50
            print(total)  # Output: 150



# 7.Give an example of the following conditions:
# (i) Homogeneous list
# (ii) Heterogeneous set
# (iii) Homogeneous tuple
# 
# Answer:->
#     (i) Homogeneous list:
#             A homogeneous list is a list that contains elements of the same data type. In Python, lists can contain elements 
#             of different data types, but a homogeneous list contains elements that are all of the same type. 
#             
#             Here's an example:
#                 # Homogeneous list of integers
#                 int_list = [1, 2, 3, 4, 5]
# 
#                 # Homogeneous list of strings
#                 string_list = ["apple", "banana", "orange"]
# 
#                 # Homogeneous list of booleans
#                 bool_list = [True, False, True, True]
#                 
#      (ii) Heterogeneous set:
#            A heterogeneous set is a set that contains elements of different data types. In Python sets, elements are unique 
#            and unordered, and they can be of different types. 
#            
#            Here's an example of a heterogeneous set:
#             # Heterogeneous set with integers, strings, and booleans
#             heterogeneous_set = {1, "apple", True, 2, "banana", False}
#             
#      (iii) Homogeneous tuple:
#             A homogeneous tuple is a tuple that contains elements of the same data type. Tuples are similar to lists, 
#             but they are immutable, meaning their elements cannot be modified after creation. 
#             
#             Here's an example of a homogeneous tuple:
#             # Homogeneous tuple of integers
#             int_tuple = (10, 20, 30, 40, 50)
# 
#             # Homogeneous tuple of strings
#             string_tuple = ("John", "Jane", "Jim")
# 
#             # Homogeneous tuple of booleans
#             bool_tuple = (True, False, True)
# 
# 

# 8. Explain the mutable and immutable data types with proper explanation & examples.
# 
# Answer:->
#     data types can be classified into two categories: mutable and immutable. The distinction between mutable and immutable
#     data types lies in how they behave when their values are modified after creation.
# 
# 1.Mutable Data Types:
#     Mutable data types are objects whose state or content can be changed after they are created. When you modify a mutable 
#     object, the object itself remains at the same memory location, and only its internal data is modified. This means that you
#     can add, remove, or modify elements within the object without creating a new object. Some common examples of mutable data 
#     types in Python include lists, dictionaries, and sets.
#     
#     Example of a mutable data type - List:
#     
#     # Creating a list
#     my_list = [1, 2, 3, 4]
# 
#     # Modifying the list
#     my_list[2] = 10
#     print(my_list)  # Output: [1, 2, 10, 4]
# 
#     # Appending an element
#     my_list.append(5)
#     print(my_list)  # Output: [1, 2, 10, 4, 5]
# 
#     # Removing an element
#     my_list.remove(2)
#     print(my_list)  # Output: [1, 10, 4, 5]
#     
#    
# 2.Immutable Data Types:
#     Immutable data types, on the other hand, are objects whose state cannot be changed after they are created. When you modify 
#     an immutable object, a new object is created with the modified value. The original object remains unchanged. Immutable 
#     objects provide some level of data integrity and safety since their values cannot be accidentally changed.
#     Common examples of immutable data types in Python include integers, floats, strings, and tuples.
# 
# Example of an immutable data type - String:
# 
#     # Creating a string
#     my_string = "Hello"
# 
#     # Attempting to modify the string
#     my_string[2] = "t"  # This will raise a TypeError
# 
#     # Concatenating strings to create a new one
#     new_string = my_string + " World"
#     print(new_string)  # Output: "Hello World"
# 
# 

# In[1]:


#9.Write a code to create the given structure using only for loop.
#                *
#               ***
#              *****
#             *******
#            *********

# Define the number of rows in the pattern
num_rows = 5

# Loop through each row
for i in range(num_rows):
    # Print spaces before the first asterisk
    for j in range(num_rows - i - 1):
        print(" ", end="")
    
    # Print asterisks for the current row
    for k in range(2 * i + 1):
        print("*", end="")
    
    # Move to the next line for the next row
    print()

           
    
        


# In[3]:


#10. Write a code to create the given structure using while loop.
#           |||||||||
#            |||||||
#             |||||
#              |||
#               |

# Define the number of rows in the pattern
num_rows = 5

# Initialize variables for spaces and bars
spaces = 0
bars = num_rows * 2 - 1

# Loop through each row
while bars >= 1:
    # Print spaces before the vertical bars
    for i in range(spaces):
        print(" ", end="")
    
    # Print the vertical bars
    for j in range(bars):
        print("|", end="")
    
    # Move to the next line for the next row
    print()
    
    # Update spaces and bars for the next row
    spaces += 1
    bars -= 2


# In[ ]:




