# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
# Level 6 kyu

# Directions:
# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.
# For example (Input --> Output):
# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 4 --> 0 (because 4 is already a one-digit number)


# Function
def persistence(n):
    # If the given number is already single digit then return 0.
    if n <= 9:
        return 0
    # Counter for how many times we have multiplied the given number.
    count: int = 0
    
    # Create an array from the given number
    numbers_list: list = [int(number) for number in str(n)]
    # Begin building answer by starting sum at the first item in the numbers_list.
    answer: int = numbers_list[0]
    # Delete that first number so to not repeat when multiplying in loop.
    numbers_list.pop(0)
    # Loop through numbers_list and multiply items.
    for number in numbers_list:
        answer: int = answer * number
    
    # That is a multplication cycle so add 1 to the counter.
    count: int = count + 1

    # Start while loop to get remaining persistant multipliers while the answer is larger than a single digit.
    while answer >= 9:
        # Turn that answer into another list of numbers
        numbers_list: list = [int(number) for number in str(answer)]
        
        # If 0 is in that list then the multiplying sum of that list will equal zero, persistance done, exit.        
        if 0 in numbers_list:
            return count + 1
        
        # Begin building answer by starting sum at the first item in the numbers_list.
        answer: int = numbers_list[0]
        # Delete that first number so to not repeat when multiplying in loop.
        numbers_list.pop(0)
        # Loop through numbers_list and multiply items.
        for number in numbers_list:
            answer: int = answer * number
        
        # Loop through numbers_list and multiply items.     
        count: int = count + 1
        
    return count


# Test Cases
import codewars_test as test
from solution import persistence

@test.describe("Persistent Bugger.")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(persistence(39), 3)
        test.assert_equals(persistence(4), 0)
        test.assert_equals(persistence(25), 2)
        test.assert_equals(persistence(999), 4)