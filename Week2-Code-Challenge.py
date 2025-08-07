""""
Write a program that accepts user input to create a list of integers.
Then, compute the sum of all the integers in the list.
"""
integer_lists = input("Enter list of integers, separated by spaces: ")
# Convert the input string into a list of integers
integer_lists = list(map(int, integer_lists.split()))
print("List:", integer_lists)
sum_of_integers = sum(integer_lists)
print("Sum:", sum_of_integers)

""""
Create a tuple containing the names of five of your favorite books.
Then, use a for loop to print each book name on a separate line.
"""
tuple_names=('A','B','C','D','E')
for name in tuple_names:
    print(name)

""""
Write a program that uses a dictionary to store information about a person,
such as their name, age, and favorite color. Ask the user for input and store 
the information in the dictionary.
Then, print the dictionary to the console.
"""

# Create an empty dictionary
person_dict = {}

# Ask the user for information
person_dict["name"] = input("Enter your name: ")
person_dict["age"] = int(input("Enter your age: "))
person_dict["favorite_color"] = input("Enter your favorite color: ")

# Print the dictionary
print("Person Information:", person_dict)

""""
Write a program that accepts user input to create two sets of integers. 
Then, create a new set that contains only the elements that are common to both sets.
"""
first_set=input("Enter First Integers set, separated by spaces: ")
second_set=input("Enter Second Integers set, separated by spaces: ")
# Convert the input string into a list of integers
first_integers_set = set(map(int, first_set.split()))
print("Set 1:", first_integers_set)
second_integers_set = set(map(int, second_set.split()))
print("Set 2:", second_integers_set)
common_elements=first_integers_set.intersection(second_integers_set)
print("Common elements in Set 1 and Set 2: ",common_elements)

"""
Create a program that stores a list of words. 
Then, use list comprehension to create a new list that contains only 
the words that have an odd number of characters.
"""
# List of words
list_of_words = ["Word1", "Word2", "Python", "AI", "Code"]

# List comprehension to filter words with odd number of characters
odd_length_words = [word for word in list_of_words if len(word) % 2 == 1]

# Print the result
print("Words with an odd number of characters:", odd_length_words)
