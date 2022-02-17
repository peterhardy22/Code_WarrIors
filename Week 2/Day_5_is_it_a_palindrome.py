# https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/train/python
# Level 8 kyu

# Directions:
# Write a function that checks if a given string (case insensitive) is a palindrome.


# Function
def is_palindrome(string):
    if string.lower() == string[::-1].lower():
        return True
    else:
        return False


# Test Cases
@test.describe('sample tests')
def sample_tests():
    test.assert_equals(is_palindrome('a'), True)
    test.assert_equals(is_palindrome('aba'), True)
    test.assert_equals(is_palindrome('Abba'), True)
    test.assert_equals(is_palindrome('malam'), True)
    test.assert_equals(is_palindrome('walter'), False)
    test.assert_equals(is_palindrome('kodok'), True)
    test.assert_equals(is_palindrome('Kasue'), False)