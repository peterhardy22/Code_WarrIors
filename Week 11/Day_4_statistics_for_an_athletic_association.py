# https://www.codewars.com/kata/55b3425df71c1201a800009c
# Level 6 kyu

# Directions:
# You are the "computer expert" of a local Athletic Association (C.A.A.). 
# Many teams of runners come to compete. 
# Each time you get a string of all race results of every team who has run. 

# For example here is a string showing the individual results of a team of 5 runners:
# "01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17"

# Each part of the string is of the form: h|m|s where h, m, s (h for hour, m for minutes, s for seconds) are positive or null integer (represented as strings) with one or two digits. 
# Substrings in the input string are separated by , or ,.

# To compare the results of the teams you are asked for giving three statistics; range, average and median.
# Range : difference between the lowest and highest values. In {4, 6, 9, 3, 7} the lowest value is 3, and the highest is 9, so the range is 9 − 3 = 6.
# Mean or Average : To calculate mean, add together all of the numbers in a set and then divide the sum by the total count of numbers.
# Median : In statistics, the median is the number separating the higher half of a data sample from the lower half. The median of a finite list of numbers can be found by arranging all the observations from lowest value to highest value and picking the middle one (e.g., the median of {3, 3, 5, 9, 11} is 5) when there is an odd number of observations. If there is an even number of observations, then there is no single middle value; the median is then defined to be the mean of the two middle values (the median of {3, 5, 6, 9} is (5 + 6) / 2 = 5.5).

# Your task is to return a string giving these 3 values. For the example given above, the string result will be
# "Range: 00|47|18 Average: 01|35|15 Median: 01|32|34"
# of the form: "Range: hh|mm|ss Average: hh|mm|ss Median: hh|mm|ss"`
# where hh, mm, ss are integers (represented by strings) with each 2 digits.

# Remarks:
# if a result in seconds is ab.xy... it will be given truncated as ab.
# if the given string is "" you will return ""


# Function
def stat(string):
    # Return early.
    if string == '':
        return ''
    
    # Split string into a list.
    race_results_list: list = string.split(', ')
    # Create empty list to store results in total seconds.
    seconds_results_list: list = []
    
    # Iterate through list and add up each score into a total of seconds result.
    for result in race_results_list:
        results_list: list = result.split('|')
        hours: int = int(results_list[0]) * 3600
        minutes: int = int(results_list[1]) * 60
        total: int = hours + minutes + int(results_list[2])
        seconds_results_list.append(total)
    
    # Sort results in seconds from lowest to highest.
    seconds_results_list.sort()
    
    # Create calculations list.
    calculations_list: dict = []
    
    # Perform caluculations and add them to the calculations_list.
    # Calculate Range.
    range_range: int = seconds_results_list[-1] - seconds_results_list[0]
    calculations_list.append(range_range)
    # Calculate Average.
    average: int = int(sum(seconds_results_list) / len(seconds_results_list))
    calculations_list.append(average)
    # Calculate Median, depending on if length of list is even or odd.
    middle_element: float = float(len(seconds_results_list))/2
    if len(seconds_results_list) % 2 != 0:
        median: int = seconds_results_list[int(middle_element - .5)]
        calculations_list.append(median)
    else:
        median: int = (seconds_results_list[int(middle_element)] + seconds_results_list[int(middle_element-1)]) / 2
        calculations_list.append(median)
    
    # Create empty list for storing final results after being converted from total seconds.
    results_list: list = []
        
    # Convert each calculation back to the race results format
    for calculation in calculations_list:
        hours: float = calculation / 3600
        minutes: float = (hours - int(hours)) * 60
        seconds: float = (minutes - int(minutes)) * 60
        print(seconds)
        # Round up if seconds result is close enough to the next number.
        if seconds > int(seconds)+ 0.98:
            seconds = round(seconds, 0)
        # Convert seconds to 0 if the result from conversion is 60 and add that minute to minutes.
        if seconds == 60:
            seconds = 0
            minutes = minutes + 1
        
        # Add leading 0 in front of single digit numbers.
        hour = str(int(hours)).zfill(2)
        minute = str(int(minutes)).zfill(2)
        second = str(int(seconds)).zfill(2)
        
        # Build result string and add it to the results_list.
        result: str = f'{hour}|{minute}|{second}'
        results_list.append(result)
        
    return f'Range: {results_list[0]} Average: {results_list[1]} Median: {results_list[2]}'


# Test Cases
test.assert_equals(stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"), 
    "Range: 01|01|18 Average: 01|38|05 Median: 01|32|34")
test.assert_equals(stat("02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41"), 
    "Range: 00|31|17 Average: 02|26|18 Median: 02|22|00")