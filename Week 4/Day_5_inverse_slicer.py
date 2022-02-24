# https://www.codewars.com/kata/586ec0b8d098206cce001141
# Level 7 kyu

# Directions:
# You're familiar with list slicing in Python and know, for example, that:

# ages = [12, 14, 63, 72, 55, 24]
# ages[2:4]
# [63, 72]
# ages[2:]
# [63, 72, 55, 24]
# ages[:3]
# [12, 14, 63]
# Write a function inverse_slice() that takes three arguments: a list items, an integer a and an integer b. 
# The function should return a new list with the slice specified by items[a:b] excluded. For example:
# inverse_slice([12, 14, 63, 72, 55, 24], 2, 4)
# [12, 14, 55, 24]
# The input will always be a valid list, a and b will always be different integers equal to or greater than zero, but they may be zero or be larger than the length of the list.


# Function
def inverse_slice(items, a, b):
    # Store items that need to be removed in a list.
    removal_items = items[a:b]
    # Create empty list for storing results we want returned.    
    result = []
    # If an item in items...
    for item in items:
        # ...does not exist in the removal_items list...
        if item not in removal_items:
            # ...then add it to our results_list.
            result.append(item)
    # Return the inverse_slice results.
    return result


# Test Cases
test.assert_equals(inverse_slice([12, 14, 63, 72, 55, 24], 2, 4), [12, 14, 55, 24])
test.assert_equals(inverse_slice([12, 14, 63, 72, 55, 24], 0, 3), [72, 55, 24])
test.assert_equals(inverse_slice(['Intuition', 'is', 'a', 'poor', 'guide', 'when', 'facing', 'probabilistic', 'evidence'], 5, 13), ['Intuition', 'is', 'a', 'poor', 'guide'])