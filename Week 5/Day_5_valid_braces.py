# https://www.codewars.com/kata/5277c8a221e209d3f6000b56
# Level 6 kyu

# Directions:
# Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.
# This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!
# All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.
# What is considered Valid?
# A string of braces is considered valid if all braces are matched with the correct brace.
# Examples
# "(){}[]"   =>  True
# "([{}])"   =>  True
# "(}"       =>  False
# "[(])"     =>  False
# "[({})](]" =>  False


# Function
def valid_braces(string):
    # If the length of the string is odd, then it is invalid.
    if len(string) % 2 != 0:
        return False
    # If the string starts with a closing brace, it is invalid.
    if string.startswith(')') or string.startswith('}') or string.startswith(']'):
        return False
    
    # Create a list from the sentence provided to seperate each brace.
    string_list: list = [brace for brace in string]
    
    # If there is not a corresponding closing brace for every oepning brace, then it is invalid.
    if string_list.count('(') != string_list.count(')'):
        return False
    if string_list.count('{') != string_list.count('}'):
        return False
    if string_list.count('[') != string_list.count(']'):
        return False
    
    # Counter for tallying leeft vs right brace types.
    left_p_count = 0 
    right_p_count = 0
    left_c_count = 0
    right_c_count = 0
    left_s_count = 0
    right_s_count = 0
    
    # If there are ever more right braces of a type than left braces, then it is invalid.
    for brace in string_list:        
        if right_p_count > left_p_count or right_c_count > left_c_count or right_s_count > left_s_count:
            return False
        elif brace == '(':
            left_p_count = left_p_count + 1
        elif brace == ')':
            right_p_count = right_p_count + 1
        elif brace == '{':
            left_c_count = left_c_count + 1
        elif brace == '}':
            right_c_count = right_c_count + 1
        elif brace == '[':
            left_s_count = left_s_count + 1
        elif brace == ']':
            right_s_count = right_s_count + 1
    
		# Loop through braces and if an open brace is ever follwed by another brace's closing brace, then it is invalid.
    for index, brace in enumerate(string_list):
        if index + 1 < len(string_list):
            if brace == '(' and string_list[index+1] == ']':
                return False
            elif brace == '(' and string_list[index+1] == '}':
                return False
            elif brace == '{' and string_list[index+1] == ']':
                return False
            elif brace == '{' and string_list[index+1] == ')':
                return False
            elif brace == '[' and string_list[index+1] == '}':
                return False
            elif brace == '[' and string_list[index+1] == ')':
                return False
            
    # Valid Braces.
    return True


# Test Cases
import codewars_test as test

try:
	from solution import valid_braces
except: # function name used to be in camelCase
	from solution import validBraces as valid_braces

def assert_valid(string):
    test.assert_equals(valid_braces(string), True, 'Expected "{0}" to be valid'.format(string))

def assert_invalid(string):
    test.assert_equals(valid_braces(string), False, 'Expected "{0}" to be invalid'.format(string))


@test.describe("Valid Braces")
def tests():
	@test.it("sample Tests")
	def sample_tests():
		assert_valid( "()" )
		assert_invalid( "(}" )
		assert_valid( "[]" )
		assert_invalid("[(])")
		assert_valid( "{}" )
		assert_valid( "{}()[]" )
		assert_valid( "([{}])" )
		assert_invalid( "([}{])" )
		assert_valid( "{}({})[]" )
		assert_valid( "(({{[[]]}}))" )
		assert_invalid( "(((({{" )
		assert_invalid( ")(}{][" )
		assert_invalid( "())({}}{()][][" )