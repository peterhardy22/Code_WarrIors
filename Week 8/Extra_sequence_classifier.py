# https://www.codewars.com/kata/5921c0bc6b8f072e840000c0
# Level 6 kyu

# Directions:
# A series or sequence of numbers is usually the product of a function and can either be infinite or finite.
# In this kata we will only consider finite series and you are required to return a code according to the type of sequence:
# Code	    Type	                Example
# 0	        unordered	            [3,5,8,1,14,3]
# 1	        strictly increasing	    [3,5,8,9,14,23]
# 2	        not decreasing	        [3,5,8,8,14,14]
# 3	        strictly decreasing	    [14,9,8,5,3,1]
# 4	        not increasing	        [14,14,8,8,5,3]
# 5	        constant	            [8,8,8,8,8,8]
# You can expect all the inputs to be non-empty and completely numerical arrays/lists - no need to validate the data; do not go for sloppy code, as rather large inputs might be tested.
# Try to achieve a good solution that runs in linear time; also, do it functionally, meaning you need to build a pure function or, in even poorer words, do NOT modify the initial input!


# Function
def sequence_classifier(array):
    # All items in the array are the same so the type is constant.
    if array[:-1] == array[1:]:
        return 5
    
    # Creates variables to store array in increasing and decreasing order.
    not_decreasing_array = sorted(array)
    not_increasing_array = sorted(array, reverse=True)
    
    # If the array is equal to the array sorted increasing, and their are no repeats, return 1.
    if not_decreasing_array == array and len(array) == len(set(array)):
        return 1
    # If the array is equal to the array sorted increasing, and their are repeats, return 2.
    elif not_decreasing_array == array:
        return 2
    # If the array is equal to the array sorted decreasing, and their are no repeats, return 3.
    elif not_increasing_array == array and len(array) == len(set(array)):
        return 3
    # If the array is equal to the array sorted decreasing, and their are repeats, return 4.
    elif not_increasing_array == array:
        return 4
    
    # Array is unsorted.
    return 0
    

# Test Cases
test.describe("Basic tests")
test.assert_equals(sequence_classifier([3,5,8,1,14,3]),0)
test.assert_equals(sequence_classifier([3,5,8,9,14,23]),1)
test.assert_equals(sequence_classifier([3,5,8,8,14,14]),2)
test.assert_equals(sequence_classifier([14,9,8,5,3,1]),3)
test.assert_equals(sequence_classifier([14,14,8,8,5,3]),4)
test.assert_equals(sequence_classifier([8,8,8,8,8,8]),5)
test.assert_equals(sequence_classifier([8,9]),1)
test.assert_equals(sequence_classifier([8,8,8,8,8,9]),2)
test.assert_equals(sequence_classifier([9,8]),3)
test.assert_equals(sequence_classifier([9,9,9,8,8,8]),4)