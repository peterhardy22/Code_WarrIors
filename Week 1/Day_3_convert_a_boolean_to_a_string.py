# https://www.codewars.com/kata/551b4501ac0447318f0009cd/train/python
# Level 8 kyu

# Directions:
# Implement a function which convert the given boolean value into its string representation.
# Only valid inputs will be given.


# Function
def boolean_to_string(b):
    if b == True:
        return 'True'
    else:
        return 'False'


# Test Cases
import codewars_test as test
from solution import boolean_to_string

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(boolean_to_string(True), "True")
        test.assert_equals(boolean_to_string(False), "False")