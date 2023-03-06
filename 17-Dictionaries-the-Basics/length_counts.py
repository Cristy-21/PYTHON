# Define a length_counts function that accepts a list of strings. 
# The function should return a dictionary where the keys represent a length and the values represent how many strings have that length.
#
#
# sa_countries = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]
# length_counts(sa_countries) => # {6: 1, 9: 2, 7: 2, 4: 1}
# There is 1 string with 6 letters, 2 strings with 9 letters, 2 strings with 7 letters, and 1 string with 4 letters.

def length_counts(lista):
    dictionary={}
    for element in lista:
        leng=len(element)
        count=dictionary.get(leng,0)
        dictionary[leng]=count+1
    return dictionary

sa_countries = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru","Ecuadou"]
print(length_counts(sa_countries))
