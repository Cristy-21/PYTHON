# Declare a delete_all function that accepts a list of strings and a target string
# Remove all occurrences of the target string from the list and return it
#
# EXAMPLES
# delete_all([1, 3, 5], 3)  => [1, 5]
# delete_all([5, 3, 5], 5)  => [3]
# delete_all([4, 4, 4], 4)  => []
# delete_all([4, 4, 4], 6)  => [4, 4, 4]


def delete_all(list,number):
    for numbers in reversed(list):
        if numbers==number:
            list.remove(number)
    return list



# index 0 1 2 3 4
#lista 4,3,6,3,8
#new list 8,3,6,3,4
#eliminar 3

vuelta 1 - index 0 - 8,3,6,3,4
vuelta 2 - index 1 - 8,6,3,4
vuelta 3 - index 2 - 8,6,3,4


