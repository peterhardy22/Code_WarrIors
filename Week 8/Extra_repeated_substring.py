# https://www.codewars.com/kata/5491689aff74b9b292000334
# Level 6 kyu

# Directions:
# For a given nonempty string s find a minimum substring t and the maximum number k, such that the entire string s is equal to t repeated k times.
# The input string consists of lowercase latin letters.
# Your function should return :
# a tuple (t, k) (in Python)
# an array [t, k] (in Ruby and JavaScript)
# in C, return k and write to the string t passed in parameter
# Example #1:
# s = "ababab";
# the answer is
# ("ab", 3)
# Example #2:
# s = "abcde"
# the answer is
# ("abcde", 1)
# because for this string "abcde" the minimum substring t, such that s is t repeated k times, is itself.


# Function
def f(string):
    # Create empty list to store answer.
    answer_list = []
    # Loop through the given string...
    for character in string:
        # If that character is not in answer_list then add it.
        if character not in answer_list:
            answer_list.append(character)
    # Turn answer_list into a string to know what repeated chunk we should look for.
    answer = ''.join(answer_list)
    # If the first chunk in the given string does not equal the second chunk, it does not repeat...    
    if answer != string[len(answer_list):(len(answer_list) * 2)]:
        # Return entire given string.
        return (string, 1)
    # Repetition count determined by how many times the chunk appears in the given string. 
    count = int(len(string)/len(answer_list))
        
    return (answer, count)
    

# Test Cases
test.assert_equals(f("ababab"), ("ab", 3));
test.assert_equals(f("abcde"), ("abcde", 1));