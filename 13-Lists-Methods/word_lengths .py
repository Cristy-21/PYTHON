# Define a word_lengths function that accepts a string. 
# It should return a list with the lengths of each word.
#
# EXAMPLES
# word_lengths("Mary Poppins was a nanny")  => [4, 7, 3, 1, 5]
# word_lengths("Somebody stole my donut")   => [8, 5, 2, 5]


def word_lengths(string):
    list=string.split(" ")
    len_list=[]
    for str in list:
        len_list.append(len(str))
    return len_list

print(word_lengths("Mary Poppins was a nanny"))
print(word_lengths("Somebody stole my donut"))
