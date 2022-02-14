# https://www.codewars.com/kata/57f222ce69e09c3630000212
# Level 8 kyu

# Directions:
# Check the provided array (x) for good ideas 'good' and bad ideas 'bad'. 
# If there are one or two good ideas, return 'Publish!'. 
# If there are more than 2 return 'I smell a series!'. 
# If there are no good ideas, as is often the case, return 'Fail!'.


# Function
def well(x):
    publish_list = []
    
    for idea in x:
        if idea == 'good':
            publish_list.append(idea)
    
    if len(publish_list) == 1 or len(publish_list) == 2:
        return 'Publish!'
    elif len(publish_list) >= 3:
        return 'I smell a series!'
    elif len(publish_list) == 0:
        return 'Fail!'


# Test Cases
import codewars_test as test
from solution import well

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(well(['bad', 'bad', 'bad']), 'Fail!')
        test.assert_equals(well(['good', 'bad', 'bad', 'bad', 'bad']), 'Publish!')
        test.assert_equals(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']), 'I smell a series!')