# https://www.codewars.com/kata/52774a314c2333f0a7000688
# Level 5 kyu

# Directions:
# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
# Examples:
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
# Constraints:
# 0 <= input.length <= 100
# Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. 
# Furthermore, the input string may be empty and/or not contain any parentheses at all. 
# Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).


# Function
def valid_parentheses(string):
    # If stirng is empty then its valid.
    if not string:
        return True
    
    # List that stores valid prenthesis for reference.
    valid_items: list = ['(', ')']
    # Create list to hold only parenthesis.
    parenthesis: list = []
    for character in string:
        if character in valid_items:
            parenthesis.append(character)
    # Convert list of perenthesis into a string
    parenthesis_string = ''.join(parenthesis) 
    
    # If there are an odd number of parenthesis' then it is invalid.
    if len(parenthesis_string) % 2 != 0:
        return False     
    
    # If there are an even number of parenthesis' it might be valid...
    if parenthesis_string.count('(') == parenthesis_string.count(')'):        
        # If a left parenthesis comes before a right parenthesis it is invalid.
        if parenthesis_string.find(')') < parenthesis_string.find('('):
            return False
        
        # The count of the right braces outweighs the count of the left braces, which renders it invalid.
        left_counter = 0
        right_counter = 0
        
        for index, character in enumerate(parenthesis):
            print(left_counter, right_counter)

            if right_counter <= left_counter:
                if character == '(':
                    left_counter = left_counter + 1
                else:
                    right_counter = right_counter + 1
            else:
                return False
        return True
    # Odd number of parenthesis so it cannot be valid.
    else:
        return False


# Test Cases
import codewars_test as test
from solution import valid_parentheses

@test.describe("Sample Tests")
def tests():
    @test.it("Sample tests")
    def sample_tests():
        test.assert_equals(valid_parentheses("  ("),False, "should work for '  ('")
        test.assert_equals(valid_parentheses(")test"),False, "should work for ')test'")
        test.assert_equals(valid_parentheses(""),True, "should work for ''")
        test.assert_equals(valid_parentheses("hi())("),False, "should work for 'hi())('")
        test.assert_equals(valid_parentheses("hi(hi)()"),True, "should work for 'hi(hi)()'")