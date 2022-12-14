# method 1

# def is_palidrome(word):
#     reversed_word=word[::-1]
#     if word == reversed_word:
#         return True
#     return False



# method 2
def is_palidrome(word):
    if word == word[::-1]:
        return True
    return False


# mathod 3
def is_palidrome(word):
    return word==word[::-1]
print(is_palidrome("naman"))
print(is_palidrome("horse"))
