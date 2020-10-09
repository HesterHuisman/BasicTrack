def reverse(word):
    """Function which provides the word and the reverse of the word"""
    return word+word[::-1]


print(reverse("good"))
print(reverse("Python"))
print(reverse(""))
print(reverse("a"))
