# Declare an invert function that accepts a dictionary object. 
# The function should return a new dictionary where the keys and values from the original dictionary are inverted. 
# Each key should now be a value, and each value should be a key. 
# Assume both the keys and values of the dictionary are immutable.
#
# my_dict = {
#   "A": "B", 
#   "C": "D",
#   "E": "F"
# }
#
# invert(my_dict) => {'B': 'A', 'D': 'C', 'F': 'E'}

def invert(dict):
    new_dict={}
    for key,value in dict.items():
        new_dict[value]=key
    return new_dict

my_dict = {
   "A": "B", 
   "C": "D",
   "E": "F"
 }

#print(invert(my_dict))
















# Declare a count_of_value function that accepts a dictionary and an integer.
# It should return a count of the number of times the integer appears 
# as a value among the dictionary’s values.
#
# my_dict = { "a" : 5, "b" : 3, "c" : 5 }
#
# count_of_value(my_dict, 5) => 2
# count_of_value(my_dict, 3) => 1

def count_of_value(diccionario,int):
    count=0
    for letter,number in diccionario.items():
        if number==int:
            count+=1
    return count
my_dict = { "a" : 5, "b" : 3, "c" : 5 }

#print(count_of_value(my_dict, 5))
#print(count_of_value(my_dict, 3))




















# Declare a sum_of_values that accepts a dictionary and a list of strings.
# The dictionary will have keys of strings and values of numbers.
#
# The function should return the sum of values for dictionary 
# keys that are also found in the list.
#
# NOTE: sum is a reserved keyword in Python. Don’t use it as a variable name.
#
# my_dict = { "a": 5, "b": 3, "c": 10 }
#
# sum_of_values(my_dict, ["a"])  => 5
# sum_of_values(my_dict, ["a", "c"])  => 15
# sum_of_values(my_dict, ["a", "c", "b"])  => 18
# sum_of_values(my_dict, ["z"])  => 0

def sum_of_values(dictt,lista):
    total=0
    for str,val in dictt.items():
        if str in lista:
            total+=val
    return total

my_dict = { "a": 5, "b": 3, "c": 10 }

print(sum_of_values(my_dict, ["a"]))
print(sum_of_values(my_dict, ["a", "c"]))
print(sum_of_values(my_dict, ["a", "c", "b"]))
print(sum_of_values(my_dict, ["z"]))

