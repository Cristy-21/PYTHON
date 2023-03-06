# Declare a count_of_a function that accepts a list of strings.
# It should return a list with counts of how many “a” characters appear per string.
# Do NOT use list comprehension.
#
# EXAMPLES:
# count_of_a(["alligator", "aardvark", "albatross"])    => [2, 3, 2]
# count_of_a(["plywood"])                               => [0]
# count_of_a([])                                        => []

def count_of_a(lista):
    return list(map(lambda word: word.count("a"),lista))

print(count_of_a(["alligator", "aardvark", "albatross"]))
print(count_of_a(["plywood"]))
print(count_of_a([]))