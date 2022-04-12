# https://www.codewars.com/kata/51b6249c4612257ac0000005
# Level 6 kyu

# Directions:
# Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. 
# You don't need to validate the form of the Roman numeral.
# Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. 
# So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). 
# The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.
# Example:
# solution('XXI') # should return 21


# Function
def solution(roman):    
    # Store Roman numerals in a dictionary iwht corresponding values.
    roman_dict: dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    # Create empty list to store converted roman numerals.
    answer_list: list = []
    
    # Convert roman numerals to corresponding numbers value.
    for numeral in roman:
        if numeral in roman_dict.keys():
            answer_list.append(roman_dict[numeral])
    
    # Reverse list to determine if subtracting needs to occur for non-roman numeral dates (i.e IV = 4, not 6).
    reversed_answer_list: list = answer_list[::-1]
    
    # Create counter for building year date.
    counter: int = 0
    
    # Loop through list:
    for index, number in enumerate(reversed_answer_list):
        # Make sure looping stays within index range.
        if index < (len(reversed_answer_list) - 1):
            # If number is larger than number to the right, subtract both numbers and add to counter.
            if number > reversed_answer_list[index+1]:
                counter: int = counter + (number - reversed_answer_list[index+1]) - reversed_answer_list[index+1]
            # Add both numbers and add to counter.
            else:
                counter: int = counter + number
    # Add last item in list
    counter: int = counter + reversed_answer_list[-1]
    
    return counter


# Test Cases
test.describe("Example Tests")
test.assert_equals(solution('XXI'), 21, 'XXI should == 21')
test.assert_equals(solution('I'), 1, 'I should == 1')
test.assert_equals(solution('IV'), 4, 'IV should == 4')
test.assert_equals(solution('MMVIII'), 2008, 'MMVIII should == 2008')
test.assert_equals(solution('MDCLXVI'), 1666, 'MDCLXVI should == 1666')