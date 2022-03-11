# https://www.codewars.com/kata/5526fc09a1bbd946250002dc
# Level 6 kyu

# Directions:
# You are given an array (which will have a length of at least 3, but could be very large) containing integers. 
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. 
# Write a method that takes the array as an argument and returns this "outlier" N.
# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)

# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)


# Function
def find_outlier(integers):
    # Create list of odd_numbers and even_numbers.
    odd_numbers: list = []
    even_numbers: list = []
    
    for number in integers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    
    # Store the length of each list for clarity.
    odd_count: int = len(odd_numbers)
    even_count: int = len(even_numbers) 
    
    # Determine which list has a longer length.
    # If there are more odd numbers than even numbers...
    if odd_count > even_count:
        # Store the even number that is the outlier.
        even_outlier: int = int(even_numbers[0])
        return even_outlier
    # There are more even numbers than odd numbers.
    else:
        # Store the odd number that is the outlier.
        odd_outlier: int = int(odd_numbers[0])
        return odd_outlier


# Test Cases
test.assert_equals(find_outlier([2, 4, 6, 8, 10, 3]), 3)
test.assert_equals(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
test.assert_equals(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)