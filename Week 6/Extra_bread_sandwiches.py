# https://www.codewars.com/kata/622a6a822494ab004b2c68d2
# Level 6 kyu

# Directions:
# If you're not familiar with the fantastic culinary delights of the British Isles you may not know about the bread sandwich.
# The idea is very simple - if you have a slice of bread between two other slices of bread, then it's a bread sandwich. 
# Additionally, if you have a bread sandwich between two other slices of bread, you get a bread sandwich sandwich, and so on.
# In this kata, we will define the following terms like so:
# Sandwich - Two slices of bread which may or may not have a filling
# Bread Sandwich - Two slices of bread which contains one slice of bread in the middle as a filling
# You will need to build two functions:
# Given the number of slices of bread, return the phrase used to refer to the sandwich
#  2 - 'sandwich'
#  5 - 'bread sandwich sandwich'
# The reverse function - given the name of the sandwich, return how many slices of bread there are in the sandwich
# 'bread sandwich' - 3
# 'sandwich sandwich' - 4
# You should return None if there is no input / the input is invalid / there is no sandwich
# Maximum 100 slices of bread


# Function
def slices_to_name(number):
    # If the provided number is a string or less than 1, the input is invalid.
    if type(number) == str or number <= 1:
        return None
    elif number == 2:
        return 'sandwich'
    elif number == 3:
        return 'bread sandwich'
    # If the number provided is even and larger than 2.
    elif number % 2 == 0 and number >= 3:
        # Number of sandwiches equals thee number provided divided by 2.
        sandwiche: str = (int(number/2)) * 'sandwich '
        # Remove space after the last sandwich.
        return sandwiche[:-1]
    # If the number provided is odd and larger than 3.
    elif number % 2 != 0 and number >= 3:
        # Find out how many sandwiches to crete by subtracting a bread (1).
        multiplier: int = (number - 1)
        sandwiche: str = (int(multiplier/2)) * 'sandwich '
        return f'bread {sandwiche}'[:-1]

def name_to_slices(name):
    # If the name provided is an integer, or an empty string, or just a slice of bread, or None, it is invalid.
    if type(name) == int or name == '' or name == 'bread' or name is None:
        return None
    # Convert name to a list for easier looping.
    name_list: list = name.split(' ')
    print(name_list)
    # If an item in the name_list is not either bread or sandwich, it is invalid.    
    for item in name_list:
        if item != 'bread' and item != 'sandwich':
            return None
    # If name_list only consist of sanwiches...
    if name_list and all(item == "sandwich" for item in name_list):
        # The answer is the length of name_list multiplied by each slice in a sandwich (2).
        answer: int = len(name_list) * 2
        return answer
    
    if name == 'bread sandwich':
        return 3
    # If the length of name_list is odd and the list doe not begin with bread, it is invalid.
    elif len(name_list) % 2 != 0 and name_list[0] != 'bread':
        return None
    # If the length of name_list is odd and the list does begin with bread...
    elif len(name_list) % 2 != 0 and name_list[0] == 'bread':
        # The answer is the length of name_list minus 1 then multiplied by 2 for the bread count.
        # Plus 1 more slice of bread from the beginning.
        answer: int = ((len(name_list) - 1) * 2) + 1
        return int(answer)
    # If the length of name_list is even and bread is not in the list...
    elif len(name_list) % 2 == 0 and 'bread' not in name_list:
        # The answer is numbere of sandwiches multiplied by each slice of bread (2).
        answer: int = len(name_list) * 2
        return int(answer)
    # If the length of name_list is even and the list does begin with bread...
    elif len(name_list) % 2 == 0 and name_list[0] == 'bread':
        # The answer is the length of name_list minus 1 then multiplied by 2 for the bread count.
        # Plus 1 more slice of bread from the beginning.
        answer: int =((len(name_list) - 1) * 2) + 1
        return answer
    else:
        return None
    

# Test Cases
from solution import slices_to_name, name_to_slices
import codewars_test as test

@test.describe("slices_to_name")
def tests():
    @test.it("should return the name of the sandwich")
    def test_slices_to_name():
        test.assert_equals(slices_to_name(0), None)
        test.assert_equals(slices_to_name(1), None)
        test.assert_equals(slices_to_name(-2), None)
        test.assert_equals(slices_to_name('bread'), None)
        test.assert_equals(slices_to_name(2), 'sandwich')
        test.assert_equals(slices_to_name(3), 'bread sandwich')
        test.assert_equals(slices_to_name(11),'bread sandwich sandwich sandwich sandwich sandwich')
        test.assert_equals(slices_to_name(8), 'sandwich sandwich sandwich sandwich')
        
        
@test.describe("name_to_slices")
def tests():
    @test.it("should return the number of slices")
    def test_name_to_slices():
        test.assert_equals(name_to_slices(12), None)
        test.assert_equals(name_to_slices(''), None)
        test.assert_equals(name_to_slices('sandwich bread sandwich'), None)
        test.assert_equals(name_to_slices('sand wich'), None)
        test.assert_equals(name_to_slices('bread sandwich'), 3)
        test.assert_equals(name_to_slices('sandwich sandwich sandwich sandwich'), 8)
        test.assert_equals(name_to_slices('bread'), None)
        test.assert_equals(name_to_slices('bread sandwich sandwich sandwich'), 7)