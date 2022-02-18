# https://www.codewars.com/kata/5808dcb8f0ed42ae34000031/train/python
# Level 8 kyu

# Directions:
# Write a function, gooseFilter / goose-filter / goose_filter / GooseFilter, that takes an array of strings as an argument and returns a filtered array containing the same elements but with the 'geese' removed.
# The geese are any strings in the following array, which is pre-populated in your solution:
# geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
# For example, if this array were passed as an argument:
# ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]
# Your function would return the following array:
# ["Mallard", "Hook Bill", "Crested", "Blue Swedish"]
# The elements in the returned array should be in the same order as in the initial array passed to your function, albeit with the 'geese' removed. 
# Note that all of the strings will be in the same case as those provided, and some elements may be repeated.


# Function
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    no_geese = []
    for bird in birds:
        if bird not in geese:
            no_geese.append(bird)
    return no_geese


# Test Cases
import codewars_test as test
from solution import goose_filter

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]),["Mallard", "Hook Bill", "Crested", "Blue Swedish"])
        test.assert_equals(goose_filter(["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"]),["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"])
        test.assert_equals(goose_filter(["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]),[])