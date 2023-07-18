# add "a" or "an" to beginning of word
# ["puzzle", "laptop", "apple", "napkin", "eye", "umbrella", "mouse"] =>
# ["a puzzle", "a laptop", "an apple", "a napkin", "an eye", "an umbrella", "a mouse"]

words = ["puzzle", "laptop", "apple", "napkin", "eye", "umbrella", "mouse"]


def a_or_an(array):
    vowels = ["a", "e", "i", "o", "u"]
    a_an_array = []
    for word in array:
        if word[0].lower() in vowels:
            a_an_array.append(f"an {word}")
        else:
            a_an_array.append(f"a {word}")
    return a_an_array


print(a_or_an(words))


# return an array with only the vowels of each string
# ["puzzle", "laptop", "apple", "napkin", "eye", "umbrella", "mouse"] =>
# ["ue", "ao", "ae", "ai", "ee", "uea", "oue"]

words_list = ["puzzle", "laptop", "apple", "napkin", "eye", "umbrella", "mouse"]


def only_vowels(array):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    vowels_array = []
    for word in array:
        string = ""
        for letter in word:
            if letter in vowels:
                string += letter
        vowels_array.append(string)
    return vowels_array


print(only_vowels(words_list))

# for each string, create a new array where each letter in the string is an element
# ["cat", "red", "glue", "pen", "chair"] =>
# [['c','a','t'], ['r','e','d'], ['g','l','u','e'], ['p','e','n'], ['c','h','a','i','r']]

word_list = ["cat", "red", "glue", "pen", "chair"]

# For Loops:
# def single_element(array):
#     element_array = []
#     for word in array:
#         letter_array = []
#         for letter in word:
#             letter_array.append(letter)
#         element_array.append(letter_array)
#     return element_array


# Using the list method:
def single_element(array):
    element_array = []
    for word in array:
        element_array.append(list(word))
    return element_array


print(single_element(word_list))
