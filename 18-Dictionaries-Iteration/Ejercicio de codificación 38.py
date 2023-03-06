# Declare a common_elements function that accepts a dictionary
# It should return a list with all of the elements that are found
# as both a key and a value in the dictionary
#
# HINT: Use the in operation to check for inclusion in a view or list object
#
# my_dict = {
#   "A": "K",
#   "B": "D",
#   "C": "A",
#   "D": "Z"
# }
#
# common_elements(my_dict) => ["A", "D"]

def common_elements(dict):
    lista=[]
    for key in dict:
        if key in dict.values():
            lista.append(key)
    return lista
my_dict = {
   "A": "K",
   "B": "D",
   "C": "A",
   "D": "Z"
 }

print(common_elements(my_dict))

