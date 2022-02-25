# https://www.codewars.com/kata/5266876b8f4bf2da9b000362
# Level 6 kyu

# Directions:
# You probably know the "like" system from Facebook and other pages. 
# People can "like" blog posts, pictures or other items. 
# We want to create the text that should be displayed next to such an item.
# Implement the function which takes an array containing the names of people that like an item. 
# It must return the display text as shown in the examples:
# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"


# Function
def likes(names):
    # Store length of names list as a variable for clarity.
    names_length = len(names)
    # Base return statements off of names_length.
    if names == []:
        return 'no one likes this'
    elif names_length == 1:
        return f'{names[0]} likes this'
    elif names_length == 2:
        return f'{names[0]} and {names[1]} like this'
    elif names_length == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    # If names_length is longer than 3 names...
    else:
        return f'{names[0]}, {names[1]} and {names_length - 2} others like this'


# Test Cases
import codewars_test as test
from solution import likes

@test.it('Basic tests')
def _():
    test.assert_equals(likes([]), 'no one likes this')
    test.assert_equals(likes(['Peter']), 'Peter likes this')
    test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
    test.assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
    test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')