# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001
# Level 6 kyu

# Directions:
# Complete the solution so that it splits the string into pairs of two characters. 
# If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
# Examples:
# 'abc' =>  ['ab', 'c_']
# 'abcdef' => ['ab', 'cd', 'ef']


# Function
def solution(string):
    # Store length of string in variable for clairty.
    string_length = len(string)
    # Create a list of paired characters ignoring the last element if a string is odd in length
    paired_list: list = [string[index] + string[index+1] for index in range(0, string_length-1, 2)]
    # If the string length is odd in length...
    if string_length % 2 == 1:
        # Add last element from string.
        paired_list.append(string[string_length-1])
        # Store last element in a variable.
        last_element = paired_list[-1]
        # Add _ to last_element in paired_list.
        paired_list[-1] = f'{last_element}_'
        return paired_list
    else:
        # String is even in length, return paired_list.
        return paired_list


# Test Cases
test.describe("Example Tests")

tests = (
    ("asdfadsf", ['as', 'df', 'ad', 'sf']),
    ("asdfads", ['as', 'df', 'ad', 's_']),
    ("", []),
    ("x", ["x_"]),
)

for inp, exp in tests:
    test.assert_equals(solution(inp), exp)