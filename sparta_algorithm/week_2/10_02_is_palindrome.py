input = "abcba"


def is_palindrome(string):
    n = len(string)

    if string[0] != string[-1]:
        return False
    if n <= 1:
        return True

    return is_palindrome(string[1:-1])


print(is_palindrome(input))