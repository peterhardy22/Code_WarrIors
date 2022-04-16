# https://www.codewars.com/kata/602afedfd4a64d0008eb4e6e
# Level 6 kyu

# Directions:
# What date corresponds to the nth day of the year?
# The answer depends on whether the year is a leap year or not.
# Write a function that will help you determine the date if you know the number of the day in the year, as well as whether the year is a leap year or not.
# The function accepts the day number and a boolean value isLeap as arguments, and returns the corresponding date of the year as a string "Month, day".
# Only valid combinations of a day number and isLeap will be tested.
# Examples:
# With input `41, false` => return "February, 10"
# With input `60, false` => return "March, 1
# With input `60, true` => return "February, 29"
# With input `365, false` => return "December, 31"
# With input `366, true` => return "December, 31"


# Function
def get_day(day, is_leap): 
    from datetime import datetime, timedelta
    # If not a leap year or is a leap year and day is before 60th (February 29th) calculate date normally.
    if is_leap == False or (is_leap == True and day < 60):
        answer: str = datetime.strptime(str(day), "%j").strftime("%B, %-d")
        return answer
    
    if is_leap == True:
        # If day is 60th, then answer is February, 29.
        if day == 60:
            return 'February, 29'
        # Day is past February 29th, so calculate answer using time delta subtraction.
        else:
            answer: str = datetime.strptime(str(day), "%j").strftime("%B, %-d")
            # Convert answer back to a datetime object for using timedelta.
            date_obj = datetime.strptime(answer, '%B, %d')
            # Subtract a day from the result due to leap year silliness.
            answer = date_obj - timedelta(days=1)
            # Converet answer back to a string.
            return answer.strftime("%B, %-d")


# Test Cases
import codewars_test as test
from solution import get_day

@test.describe("Solution")
def test_group():
    @test.it("Basic tests")
    def test_case():
        test.assert_equals(get_day(15, False), "January, 15")
        test.assert_equals(get_day(41, False), "February, 10")
        test.assert_equals(get_day(59, False), "February, 28")
        test.assert_equals(get_day(60, False), "March, 1")
        test.assert_equals(get_day(60, True), "February, 29")
        test.assert_equals(get_day(365, False), "December, 31")
        test.assert_equals(get_day(366, True), "December, 31")