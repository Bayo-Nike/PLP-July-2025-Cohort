# empty list
my_list=[]
# To Append use append method
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After appended: ",my_list)
# insert 15 value at second position,i.e (index[1])
my_list.insert(1,15)
print("After inserted 15 value at second position: ",my_list)
another_list=[50,60,70]
# Extend my_list with another list
my_list.extend(another_list)
print("After Extended my_list with another list: ",my_list)
# Remove the last element from my_list
my_list.remove(my_list[-1])
print("After Removed the last element from my_list: ",my_list)
# Sort my_list in ascending order
my_list.sort()
print("After Sorted tin ascending order: ",my_list)
# Find and print the index of the value 30 in my_list.
print("Find and print the index of the value 30 in my_list: ",my_list.index(30))