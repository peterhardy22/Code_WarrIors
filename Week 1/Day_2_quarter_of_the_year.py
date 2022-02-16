# https://www.codewars.com/kata/5ce9c1000bab0b001134f5af/train/python
# Level 8 kyu

# Directions:
# Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.
# Example: 
# Month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.


# Function
def quarter_of(month):
    if month in (1,2,3):
        return 1
    elif month in (4,5,6):
        return 2
    elif month in (7,8,9):
        return 3
    elif month in (10,11,12):
        return 4


# Test Cases
import codewars_test as test
from solution import quarter_of

@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(quarter_of(3), 1)
        test.assert_equals(quarter_of(8), 3)
        test.assert_equals(quarter_of(11), 4)