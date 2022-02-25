# https://www.codewars.com/kata/56541980fa08ab47a0000040
# Level 7 kyu

# Directions:
# In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from a to m.
# The colors used by the printer are recorded in a control string. 
# For example a "good" control string would be aaabbbbhaijjjm meaning that the printer used three times color a, four times color b, one time color h then one time color a...
# Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.
# You have to write a function printer_error which given a string will return the error rate of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. 
# Don't reduce this fraction to a simpler expression.
# The string has a length greater or equal to one and contains only letters from ato z.
# Examples:
# s="aaabbbbhaijjjm"
# printer_error(s) => "0/14"
# s="aaaxbbbbyyhwawiwjjjwwm"
# printer_error(s) => "8/22"


# Function
def printer_error(string):
    # Create list that stores colors that do not exist.
    not_colors_list: list = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # Store length of string in a variable for clarity.
    string_length: int = len(string)
    # Find the count for how many times a color appears in the string that exists in the not_colors_list.
    error_count: int = len([character for character in string if character in not_colors_list ])
    
    return f'{error_count}/{string_length}'


# Test Cases
import codewars_test as test

@test.describe("printer_error")
def basic_tests():
    @test.it('Example Test Cases')
    def example_test_cases():
        s="aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
        test.assert_equals(printer_error(s), "3/56")
        s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
        test.assert_equals(printer_error(s), "6/60")
        s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"
        test.assert_equals(printer_error(s) , "11/65")