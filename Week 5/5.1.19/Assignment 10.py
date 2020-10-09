def is_palindrome(the_word):
    def reverse(word):
        return word[::-1]
    if the_word == reverse(the_word):
        return (True)


print(is_palindrome("abba"))
not print(is_palindrome("abab"))
print(is_palindrome("tenet"))
not print(is_palindrome("banana"))
print(is_palindrome("straw warts"))
print(is_palindrome("a"))
print(is_palindrome(""))
