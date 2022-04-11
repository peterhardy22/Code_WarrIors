# https://www.codewars.com/kata/514b92a657cdc65150000006
# Level 6 kyu

# Directions:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. 
# Additionally, if the number is negative, return 0 (for languages that do have them).
# Note: If the number is a multiple of both 3 and 5, only count it once.


# Function
def solution(number):
    # Create list of numbers based of given number.  
    numbers_list: list = list(range(3, number))
    # Create empty list to store numbers.
    answer_list: list = []
    # If integer in numbers_list is a multiple of 3 or 5 then add it to the answer_list.
    for integer in numbers_list:
        if integer % 3 == 0:
            answer_list.append(integer)
        elif integer % 5 == 0:
            answer_list.append(integer)
    # Return the sum of answer_list.
    return sum(answer_list)


# Test Cases
import codewars_test as test
from solution import solution

@test.describe("Sample tests")
def sample_tests():
    
    @test.it("Should return 3 for n=4")
    def _():
        test.assert_equals(solution(4), 3)
        
    @test.it("Should return 8 for n=6")
    def _():
        test.assert_equals(solution(6), 8)
    
    @test.it("Should return 60 for n=16")
    def _():
        test.assert_equals(solution(16), 60)
    
    @test.it("Should return 0 for n=3")
    def _():
        test.assert_equals(solution(3), 0)
    
    @test.it("Should return 3 for n=5")
    def _():
        test.assert_equals(solution(5), 3)
    
    @test.it("Should return 45 for n=15")
    def _():
        test.assert_equals(solution(15), 45)
    
    @test.it("Should return 0 for n=0")
    def _():
        test.assert_equals(solution(0), 0)
    
    @test.it("Should return 0 for n=-1")
    def _():
        test.assert_equals(solution(-1), 0)
    
    @test.it("Should return 23 for n=10")
    def _():
        test.assert_equals(solution(10), 23)
        
    @test.it("Should return 78 for n=20")
    def _():
        test.assert_equals(solution(20), 78)

    @test.it("Should return 9168 for n=200")
    def _():
        test.assert_equals(solution(200), 9168)
