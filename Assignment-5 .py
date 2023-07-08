#!/usr/bin/env python
# coding: utf-8

# ### Assignement-5
# 

# 1.What does an empty dictionary's code look like?
# Answer:->
#     dict = {}
#     

# 2.What is the value of a dictionary value with the key 'foo' and the value 42?
# Answer:->
#     {'foo':42}
# 

# 3.What is the most significant distinction between a dictionary and a list?
# Answer:->
#      the key distinctions between dictionaries and lists are:
# 
# Organization: Lists are ordered collections, maintaining the order of elements based on their indices. Dictionaries are unordered and use keys to access values.
# 
# Accessing Elements: Lists are accessed by numerical indices, while dictionaries are accessed by unique keys.
# 
# Element uniqueness: Lists allow duplicate elements, while dictionaries require unique keys.
# 
# Purpose: Lists are commonly used when the order of elements matters or when you need a simple collection of items. Dictionaries are useful when you want to store and retrieve data based on specific keys or when you need to associate values with particular identifiers.

# 4.What happens if you try to access spam['foo'] if spam is {'bar': 100}?
# Answer:->
#     If you try to access spam['foo'] and spam is { 'bar': 100 }, you will get a KeyError because the key 'foo' does not exist in the dictionary spam.

# 5.If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
# 
# Answer:->
#         In terms of functionality, both expressions are equivalent for dictionaries because the in operator checks for 
#         membership in the keys of a dictionary by default. However, there is a slight difference in efficiency and readability:
# 
#    'cat' in spam directly performs the membership check within the dictionary and is generally considered more efficient 
#    because it doesn't need to create an intermediate list of keys.
# 
#    'cat' in spam.keys() explicitly retrieves the list of keys using spam.keys() and then checks for membership. Although it 
#    produces the same result, it involves an additional step of creating a list of keys, which could be less efficient for large 
#    dictionaries. It may be useful when you specifically need access to the list of keys.

# 6.If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
# 
# Answer:->
#     
#    The expressions 'cat' in spam and 'cat' in spam.values() have different meanings and produce different results when used 
#    with a dictionary.
# 
# > 'cat' in spam checks if the key 'cat' exists in the dictionary spam. It returns a Boolean value True if the key is present as one of the keys in the dictionary, and False otherwise. This expression checks for the presence of the key within the dictionary's keys.
# 
# > 'cat' in spam.values() checks if the value 'cat' exists in the dictionary spam. It returns a Boolean value True if the value is present as one of the values in the dictionary, and False otherwise. This expression checks for the presence of the value within the dictionary's values.

# 7.What is a shortcut for the following code?
# if 'color' not in spam:
# spam['color'] = 'black'
# 
# Answer:->
#     A shortcut for the given code is to use the dict.setdefault() method. The setdefault() method allows you to set a default 
#     value for a key in a dictionary only if the key doesn't already exist. Here's how you can use it as a shortcut:
#     
#    spam.setdefault('color', 'black')
#     

# 8.How do you "pretty print" dictionary values using which module and function?
# 
# Answer:->
#         To "pretty print" dictionary values in Python, you can use the pprint module, specifically the pprint() function. 
#         The pprint module provides a way to format and display complex data structures, such as dictionaries, in a more 
#         readable and organized manner.
# 
# Here's an example of how to use pprint to pretty print dictionary values:
# 
#     import pprint
#     my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
#     pprint.pprint(my_dict)
# 
