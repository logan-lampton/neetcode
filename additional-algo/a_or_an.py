# add "a" or "an" to beginning of word
# ["puzzle", "laptop", "apple", "napkin", "eye", "umbrella", "mouse"] =>
# ["a puzzle", "a laptop", "an apple", "a napkin", "an eye", "an umbrella", "a mouse"]

words = ["puzzle", "laptop", "apple", "napkin", "eye", "umbrella", "mouse"]


def a_or_an(array):
    vowels = ["a", "e", "i", "o", "u"]
    a_an_array = []
    for word in array:
        if word[0] in vowels:
            a_an_array.append(f"an {word}")
        else:
            a_an_array.append(f"a {word}")
    print(a_an_array)


a_or_an(words)



# return an array with only the vowels of each string
# ["puzzle", "laptop", "apple", "napkin", "eye", "umbrella", "mouse"] =>
# ["ue", "ao", "ae", "ai", "ee", "uea", "oue"]


# for each string, create a new array where each letter in the string is an element
# ["cat", "red", "glue", "pen", "chair"] =>
# [['c','a','t'], ['r','e','d'], ['g','l','u','e'], ['p','e','n'], ['c','h','a','i','r']]
