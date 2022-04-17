# https://www.codewars.com/kata/59da47fa27ee00a8b90000b4
# Level 6 kyu

# Directions:
# Given a string of integers, return the number of odd-numbered substrings that can be formed.
# For example, in the case of "1341", they are 1, 1, 3, 13, 41, 341, 1341, a total of 7 numbers.
# solve("1341") = 7.


# Function
def solve(string):  
    # Main iteration to get all possible substrings of the string.
    combinations: list = [string[number: j] for number in range(len(string)) for j in range(number + 1, len(string) + 1)]
    
    # Only add the odd numbers from results to answer_list.
    answer_list: list = [number for number in combinations if int(number) % 2 != 0]
    
    # Sort list from lowest to largest.
    answer_list.sort()
    
    # Return the length of the answer_list.
    return len(answer_list)


# Test Cases
test.it("Basic tests")
test.assert_equals(solve("1347"),7)
test.assert_equals(solve("1357"),10)
test.assert_equals(solve("13471"),12)
test.assert_equals(solve("134721"),13)
test.assert_equals(solve("1347231"),20)
test.assert_equals(solve("13472315"),28)