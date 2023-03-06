# Define a to_dictionary function that accepts a list argument. 
# The function should return a dictionary where the keys are the strings and the values are their original index positions in the list.
#to_dictionary(detectives) => {'Sherlock Holmes': 0, 'Hercule Poirot': 1, 'Nancy Drew': 2}


def to_dictionary(lista):
    dictionary={}
    for index,elemnt in enumerate(lista):
        dictionary[elemnt]=index
    return dictionary

detectives = ["Sherlock Holmes", "Hercule Poirot", "Nancy Drew"]
print(to_dictionary(detectives))

