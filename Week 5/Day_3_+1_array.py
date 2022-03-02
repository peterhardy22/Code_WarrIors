# https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9
# Level 6 kyu

# Directions:
# Given an array of integers of any length, return an array that has 1 added to the value represented by the array.
# The array can't be empty.
# Only non-negative, single digit integers are allowed.
# Return nil (or your language's equivalent) for invalid inputs.
# Examples:
# For example the array [2, 3, 9] equals 239, adding one would return the array [2, 4, 0].
# [4, 3, 2, 5] would return [4, 3, 2, 6]


# Function
def up_array(array: list):
    # If the array is empty return None.
    if not array:
        return None
    # If an integer in the array is less than 0 or more than 9 return none
    for integer in array:
        if integer < 0 or integer > 9:
            return None
    # Turn the array into a list of strings.
    array_of_strings: list = [str(integer) for integer in array]
    # Turn the list of strings into a string.
    array_string: str = ''.join(array_of_strings)
    # Turn that string into an integer.
    array_integer: int = int(array_string)
    # Add one to the integer.
    array_integer_plus_one: int = array_integer + 1
    # Convert integer back into an array.
    plus_one_array: list = [int(integer) for integer in str(array_integer_plus_one)]
    
    return plus_one_array


# Test Cases
# import codewars_test as test

# test.assert_equals(up_array([2,3,9]), [2,4,0])
# test.assert_equals(up_array([4,3,2,5]), [4,3,2,6])
# test.assert_equals(up_array([1,-9]), None)