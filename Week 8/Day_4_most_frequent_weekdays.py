# https://www.codewars.com/kata/56eb16655250549e4b0013f4
# Level 6 kyu

# Directions:
# What is your favourite day of the week? Check if it's the most frequent day of the week in the year.
# You are given a year as integer (e. g. 2001). 
# You should return the most frequent day(s) of the week in that year. 
# The result has to be a list of days sorted by the order of days in week (e. g. ['Monday', 'Tuesday'], ['Saturday', 'Sunday'], ['Monday', 'Sunday']). 
# Week starts with Monday.
# Input: Year as an int.
# Output: The list of most frequent days sorted by the order of days in week (from Monday to Sunday).
# Preconditions:
# Week starts on Monday.
# Year is between 1583 and 4000.
# Calendar is Gregorian.
# Examples (input -> output):
# * 2427 -> ['Friday']
# * 2185 -> ['Saturday']
# * 2860 -> ['Thursday', 'Friday']


# Function
def most_frequent_days(year):
    import datetime
    
    # Create list of days for referencing.
    days_list: list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Using datetime module, find the first week day of the provided year.
    first_day: str = datetime.datetime(year, 1,1).strftime("%A")

    # Hint: If not a leap year then the first day of the provided year is the most frequent weekday.
    #       7 * 52 = 364, therefore the first day always occurs 53 times instead of 52 like the other days.
    #       Leap years there are two days that occur 53 times. The first and second days of the year.
    # Determine if the provided year is a leap year.
    # Leap year determined by being visible by 4 or if ending in 00 is divisible by 400.
    if year % 4 == 0 or (str(year).endswith('00') and year % 400 == 0):
        for index, day in enumerate(days_list):
            # Use days_list for referencing day of the week order and index.
            if day == first_day:
                if index < 6:
                    first_day_index: int = index
                    second_day_index: int = index + 1
                    return [days_list[first_day_index], days_list[second_day_index]]
                # Self assign index so not to loop of out range.
                else:
                    return [days_list[0], days_list[6]]
    # Year is not a leap year, return first day of the year.          
    else:
        return [first_day]
        



# Test Cases
test.describe("Example Tests")

test.assert_equals(most_frequent_days(2427), ['Friday'])
test.assert_equals(most_frequent_days(2185), ['Saturday'])
test.assert_equals(most_frequent_days(1770), ['Monday'])
test.assert_equals(most_frequent_days(1785), ['Saturday'])
test.assert_equals(most_frequent_days(1984), ['Monday', 'Sunday'])
test.assert_equals(most_frequent_days(2000), ['Saturday', 'Sunday'])