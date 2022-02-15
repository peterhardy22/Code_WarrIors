# https://www.codewars.com/kata/5b39e91ee7a2c103300018b3
# Level 7 kyu

# Directions:
# Remove all consecutive duplicate words from a string, leaving only first words entries. 
# Example:
# Input: "alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"
# Output: "alpha beta gamma delta alpha beta gamma delta"


# Function
def remove_consecutive_duplicates(s):
    string_list = s.split()
    
    if len(string_list) <= 1:
        return s
    
    unique_list = []

    for index, word in enumerate(string_list):
        if (index <= len(string_list) and index >= 0):
            if word != string_list[index-1] and index != 0:
                unique_list.append(word)

    unique_list.insert(0,string_list[0])

    return " ".join(unique_list)


# Test Cases
import codewars_test as test
# TODO Write tests
import solution # or from solution import example

# test.assert_equals(actual, expected, [optional] message)
@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        test.assert_equals(remove_consecutive_duplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'), 'alpha beta gamma delta alpha beta gamma delta');