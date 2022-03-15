# https://www.codewars.com/kata/52fb87703c1351ebd200081f
# Level 6 kyu

# Directions:
# Return the century of the input year. 
# The input will always be a 4 digit string, so there is no need for validation.
# Examples
# "1999" --> "20th"
# "2011" --> "21st"
# "2154" --> "22nd"
# "2259" --> "23rd"
# "1124" --> "12th"
# "2000" --> "20th"


# Function
def what_century(year):
    # Split year given in individual numbers.    
    year_list: list = [number for number in year]
    # Group first two numbers in list to get century.
    century: str = year_list[0] + year_list[1]
    # If the year provided is the first year of a new century, than that is the answer.
    answer: str = century
    # If the year provided is not the first year of a new century then add 1 to get the answer.
    if int(year) % 100 != 0:
        answer: int = str(int(century)+1)
    # Add endings depending on the century number.
    # 1-3 all centuries have unique endings.
    if answer == '1':
        return f'{answer}st'
    elif answer == '2':
        return f'{answer}nd'
    elif answer == '3':
        return f'{answer}rd'
    # 4-20 all centuries end in 'th'.
    elif int(answer) > 20:
        # For years 1-3 all centuries have unique endings.
        if answer.endswith('1'):
            return f'{answer}st'
        elif answer.endswith('2'):
            return f'{answer}nd'
        elif answer.endswith('3'):
            return f'{answer}rd'
        # years 4-9 all end in 'th'.
        else:
            return f'{answer}th'
    # years 4-9 all end in 'th'.    
    else:
        return f'{answer}th'


# Test Cases
import codewars_test as test
from solution import what_century

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(what_century("2011"), "21st", "With input '2011' solution produced wrong output");
        test.assert_equals(what_century("2154"), "22nd", "With input '2154' solution produced wrong output");
        test.assert_equals(what_century("2259"), "23rd", "With input '2259' solution produced wrong output");
        test.assert_equals(what_century("1234"), "13th", "With input '1234' solution produced wrong output");
        test.assert_equals(what_century("1023"), "11th", "With input '1023' solution produced wrong output");