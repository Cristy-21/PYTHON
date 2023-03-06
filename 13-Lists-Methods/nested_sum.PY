# Define a nested_sum function that accepts a list of lists of numbers
# The function should return the sum of the values
# The list may contain empty lists
#
# nested_sum([[1, 2, 3], [4, 5]])            => 15
# nested_sum([[1, 2, 3], [], [], [4], [5]])  => 15
# nested_sum([[]])                           => 0

def nested_sum(lista):
    sum=0
    for list in lista:
        for number in list:
            sum+=number
    return sum

print(nested_sum([[1, 2, 3], [4, 5]]) )
print(nested_sum([[1, 2, 3], [], [], [4], [5]]))
print(nested_sum([[]]))