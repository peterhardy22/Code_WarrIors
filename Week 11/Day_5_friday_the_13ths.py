# https://www.codewars.com/kata/540954232a3259755d000039
# Level 6 kyu

# Directions:
# Create the function fridayTheThirteenths that accepts a start year and an end year (inclusive), 
# and returns all of the dates where the 13th of a month lands on a Friday in the given range of year(s).
# The return value should be a string where each date is seperated by a space. 
# The date should be formatted like 9/13/2014 where months do not have leading zeroes and are separated with forward slashes.
# If no end year is given, only return friday the thirteenths during the start year.

# Examples
# fridayTheThirteenths(1999, 2000) 
# returns "8/13/1999 10/13/2000"
  
# fridayTheThirteenths(2014, 2015) 
# returns "6/13/2014 2/13/2015 3/13/2015 11/13/2015"
  
# fridayTheThirteenths(2000)
# returns "10/13/2000"
# This kata was designed to use the built-in Date object. 
# Dates can often be finicky, so while there are other methods to get the correct dates, I can't guarantee they will work.


# Function
def friday_the_thirteenths(start, end = None):
    from datetime import date, timedelta
    # Store starting date in variable for clarity.
    start_date = date(start, 1, 1)
    # Choose ending date based on if end was provided.
    if end is None:
        end_date = date(start, 12, 31)
    else:
        end_date = date(end, 12, 31)
    # Store rate at which we want to iterate, which is 1 day at a time.
    delta = timedelta(days=1)
    # Create empty list for storing dates that are Friday the 13ths.
    answer_list: list = []
    # While the current date in the iteration is before the end date...
    while start_date <= end_date:
        # If the current date is a Friday the 13th then add it to our answer_list.
        if start_date.strftime("%A %d") == 'Friday 13':
            answer_list.append(start_date.strftime("%-m/%d/%Y"))
        # Add one day to current date to find next date and day of the week.
        start_date += delta
    # Return the answer_list as a string seperated by spaces.
    return ' '.join(answer_list)


# Test Cases
from solution import friday_the_thirteenths
import codewars_test as test

@test.describe("sample tests")
def sample_tests():
    @test.it("single year")
    def single_year():
        test.assert_equals(friday_the_thirteenths(2000), "10/13/2000")
    @test.it("two given years")
    def two_years():
        test.assert_equals(friday_the_thirteenths(1999, 2000), "8/13/1999 10/13/2000")