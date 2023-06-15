#!/usr/bin/env python
# coding: utf-8

# 1.What exactly is []?
# Answer:->
#     [] represents an empty list. It is a literal notation used to create a new list object with no elements. A list is a
#     mutable, ordered collection of items enclosed within square brackets [].
#     
#    Example:
#     my_list = []
#     print(my_list)  # Output: []

# 2.In a list of values stored in a variable called spam, how would you assign the value "hello" as the
# third value? (Assume [2, 4, 6, 8, 10] are in spam.)
# Answer:->
#     To assign the value 'hello' as the third value in a list stored in a variable called spam, you can use the indexing and assignment capabilities of lists,the list indices starts from 0 so, the third value would be stored in index 2.
#     
#    spam =[2, 4, 6, 8, 10]
#    spam[2] = "hello"
#    
# 

# ### Let's pretend the spam includes the list ['a','b','c','d'] for the next three queries.

# 3.What is the value of spam[int(int('3'* 2) / 11)]?
# Answer:->
#     "d" is the answer

# 4.What is the value of spam[-1]?
# Answer:->
#     "d" is the values of spam[-1]
#     

# 5.What is the value of spam[:2]?
# Answer:->
#     ['a', 'b'] is the value of spam[:2]

# ### Let's pretend bacon has the list [3.14,'cat', 11, 'cat', True] for the next three questions.

# 6.What is the value of bacon.index('cat')?
# Answer:->
#     1 is the value of bacon.index('cat') because by default in python the index() method is used to find the index of the first occurrence of 'cat' in bacon, which is at index 1. 

# 7.How does bacon.append(99) change the look of the list value in bacon?
# Answer:->
#     It will modify the bacon list by adding the value 99 to the end of the list. The append() method is used to add elements to a list.
#     bacon = [3.14, 'cat', 11, 'cat', True]
#     bacon.append(99)
#     print(bacon)  # Output: [3.14, 'cat', 11, 'cat', True, 99]

# 8.How does bacon.remove('cat') change the look of the list in bacon?
# Answer:->
#     bacon.remove('cat') on the list bacon will remove the first occurrence of the value 'cat' from the list.
#     and the resultant bacon list will be [3.14, 11, 'cat', True]

# 9.What are the list concatenation and list replication operators?
# Answer:->
#     the list concatenation operator is +, and the list replication operator is *. Here's a brief explanation of how they work:
# 
# 1.List Concatenation Operator (+):
# The list concatenation operator + allows you to combine two or more lists into a single list. It creates a new list by appending the elements of the second list to the end of the first list.
# 
# Example:
#     list1 = [1, 2, 3]
#     list2 = [4, 5, 6]
#     concatenated_list = list1 + list2
#     print(concatenated_list)  # Output: [1, 2, 3, 4, 5, 6]
#     
# 2.List Replication Operator (*):
# The list replication operator * allows you to create a new list by replicating an existing list a specified number of times. It duplicates the elements of the list and forms a new list.
# 
# Example:
#     list1 = [1, 2, 3]
#     replicated_list = list1 * 3
#     print(replicated_list)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]
# 

# 10.What is difference between the list methods append() and insert()?
# Answer:->
# 
#    The append() and insert() methods are both used to add elements to a list in Python, but they differ in how the elements are added:
# 
# 1.append() method:
# 
#    Syntax: list.append(element)
#    Purpose: Adds an element to the end of the list.
#    Modifies the list in-place by adding the element to the end.
#    Does not require specifying an index. The element is automatically added at the end of the list.
#    
#    Example:
#        my_list = [1, 2, 3]
#        my_list.append(4)
#        print(my_list)  # Output: [1, 2, 3, 4]
#  
# 2.insert() method:
#     Syntax: list.insert(index, element)
#     Purpose: Adds an element at a specific index in the list.
#     Modifies the list in-place by inserting the element at the specified index, pushing the existing elements one position to 
#     the right.
#     Requires specifying the index where the element should be inserted.
#     
#    Example:
#       my_list = [1, 2, 3]
#       my_list.insert(1, 4)
#       print(my_list)  # Output: [1, 4, 2, 3]
# 
# 

# 11.What are the two methods for removing items from a list?
# Answer:->
#        There are two common methods for removing items from a list:
#        1.remove() method:Removes the first occurrence of the specified element from the list.Modifies the list in-place by 
#        removing the element if it exists.
#            
#        Syntax: list.remove(element)
#        
#        If the element is not found in the list, a ValueError is raised.
#        
#        Example:
#            my_list = [1, 2, 3, 2, 4]
#            my_list.remove(2)
#            print(my_list)  # Output: [1, 3, 2, 4]
#            
#        2.pop() method:Removes and returns the element at the specified index from the list.Modifies the list in-place by 
#        removing the element at the specified index.If the index is not specified, pop() removes and returns the last element in
#        the list.
#        Raises an IndexError if the index is out of range.
#        
#        Syntax: list.pop(index)
#        
#        Example:
#         my_list = [1, 2, 3, 4]
#         popped_element = my_list.pop(1)
#         print(my_list)  # Output: [1, 3, 4]
#         print(popped_element)  # Output: 2
# 
# 
# 
# 

# 12.Describe how list values and string values are identical.
# Answer:->
# 
# There are several similarities that make them behave similarly in certain aspects:
# 
# Indexing: Both lists and strings support indexing, allowing you to access individual elements or characters by their position within the sequence. The indexing starts from 0 for the first element.
# 
# Slicing: Both lists and strings support slicing, which allows you to extract sub-sequences by specifying a range of indices. Slicing allows you to retrieve a portion of the sequence.
# 
# Iteration: You can iterate over both lists and strings using loops or other iterable operations. This enables you to access each element or character in the sequence one by one.
# 
# Length: Both lists and strings have a length, which can be obtained using the len() function. It returns the number of elements in a list or the number of characters in a string.
# 
# Immutability (strings only): Strings are immutable, meaning they cannot be modified after they are created. Similarly, individual elements of a list (if they are immutable objects) cannot be modified, but the list as a whole can be changed by adding, removing, or replacing elements.
# 

# 13.What's the difference between tuples and lists?
# Answer:->
# 
#   Tuples and lists are both used to store collections of items, but they have some key differences:
# 
#    Mutability: Lists are mutable, meaning you can add, remove, or modify elements after the list is created. Tuples, on the 
#    other hand, are immutable, which means they cannot be modified once they are created. You cannot add, remove, or change 
#    individual elements in a tuple.
# 
#    Syntax: Lists are represented by square brackets [] and elements are separated by commas. Tuples, on the other hand, are 
#    represented by parentheses () or can be created without any delimiters, with elements also separated by commas.
# 
#    Example of a list: my_list = [1, 2, 3]
#    Example of a tuple: my_tuple = (1, 2, 3) or my_tuple = 1, 2, 3
# 
#    Usage: Lists are commonly used when you have a collection of items that may need to be modified, sorted, or accessed 
#    individually. They are more versatile and allow you to perform operations such as appending, inserting, or deleting 
#    elements. Tuples, on the other hand, are often used to represent collections of related data that should remain unchanged, 
#    such as coordinates (x, y) or a person's name and age.
# 
#    Performance: Tuples are generally slightly more memory-efficient and faster to iterate over compared to lists. This is 
#    because tuples are immutable, allowing Python to optimize their storage and processing. However, the performance difference 
#    may not be significant for small collections, and in most cases, the choice between tuples and lists should be based on 
#    their intended use and required functionality.

# 14.How do you type a tuple value that only contains the integer 42?
# Answer:->
#     To create a tuple with a single value of integer 42, you need to include a trailing comma after the value to differentiate 
#     it from a regular parentheses grouping. 
#     
#     Example:
#     my_tuple = (42,)
# In this example, the comma after 42 indicates that it is a tuple with a single element. Without the comma, it would be treated as an integer value rather than a tuple.

# 15.How do you get a list value's in tuple form? How do you get a tuple value's list form?
# Answer:->
#  To convert a list into a tuple, you can use the tuple() function. 
#    
#   Example:
#    my_list = [1, 2, 3, 4, 5]
#    my_tuple = tuple(my_list)
# In this example, the tuple() function is used to convert my_list into a tuple my_tuple. The resulting tuple will contain the same elements as the original list.
# 
#  To convert a tuple into a list, you can use the list() function.
#  Example:
#      my_tuple = (1, 2, 3, 4, 5)
#      my_list = list(my_tuple)
# In this example, the list() function is used to convert my_tuple into a list my_list. The resulting list will contain the same elements as the original tuple.

# 16.Variables that "contain" list values are not necessarily lists themselves. Instead, what do they
# contain?
# Answer:->
#     Variables that "contain" list values are not necessarily lists themselves. Instead, they can contain references or pointers to list objects in memory. This concept is commonly known as a reference or pointer to an object.
# 
# In many programming languages, including Python, variables can hold references to objects rather than directly containing the objects themselves. When a variable is assigned a list value, it stores a reference to the memory location where the list is stored.
# 
# Example:
#     my_list = [1, 2, 3]
# 
# In this code, the variable my_list is assigned a list value [1, 2, 3]. However, the variable itself does not directly contain the list. Instead, it holds a reference to the memory location where the list object [1, 2, 3] is stored.

# 17.How do you distinguish between copy.copy() and copy.deepcopy()?
# Answer:->
#     copy.copy(): This function creates a shallow copy of an object. A shallow copy creates a new object but references the same elements as the original object. In other words, the top-level object is copied, but the nested objects are still shared between the original and the copied object.
# 
# For example:
# 
#     import copy
#     original_list = [1, 2, [3, 4]]
#     copied_list = copy.copy(original_list)
#     original_list[0] = 10
#     original_list[2][0] = 30
#     print(original_list)  # Output: [10, 2, [30, 4]]
#     print(copied_list)    # Output: [1, 2, [30, 4]]
# 
# In this example, changing the value of original_list[0] affects only the original list, but modifying original_list[2][0] affects both the original and copied lists because the nested list is shared.
# 
# 
#    copy.deepcopy(): This function creates a deep copy of an object. A deep copy creates a completely independent copy of the object and all the nested objects. It means that any modifications made to the original object or its nested objects will not affect the deep copy, and vice versa.
# 
# For example:
# 
#     import copy
#     original_list = [1, 2, [3, 4]]
#     deepcopied_list = copy.deepcopy(original_list)
#     original_list[0] = 10
#     original_list[2][0] = 30
#     print(original_list)     # Output: [10, 2, [30, 4]]
#     print(deepcopied_list)   # Output: [1, 2, [3, 4]]
#     
# In this example, both the modification of original_list[0] and original_list[2][0] only affect the original list. The deep copied list remains unchanged because it is an independent copy.
