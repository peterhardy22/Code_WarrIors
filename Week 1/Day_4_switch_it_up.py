# https://www.codewars.com/kata/5808dcb8f0ed42ae34000031/train/python
# Level 8 kyu

# Directions:
# When provided with a number between 0-9, return it in words.
# Input :: 1
# Output :: "One".
# If your language supports it, try using a switch statement.


# Function
def switch_it_up(number):
    if number == 0:
        return "Zero"
    elif number == 1:
        return "One"
    elif number == 2:
        return "Two"
    elif number == 3:
        return "Three"
    elif number == 4:
        return "Four"
    elif number == 5:
        return "Five"
    elif number == 6:
        return "Six"
    elif number == 7:
        return "Seven"
    elif number == 8:
        return "Eight"
    elif number == 9:
        return "Nine"


# Test Cases
import codewars_test as test
from solution import switch_it_up

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(switch_it_up(0), "Zero")
        test.assert_equals(switch_it_up(9), "Nine")