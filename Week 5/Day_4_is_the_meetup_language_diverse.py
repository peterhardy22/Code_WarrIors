# https://www.codewars.com/kata/58381907f8ac48ae070000de
# Level 6 kyu

# Directions:
# You will be given an array of objects representing data about developers who have signed up to attend the next web development meetup that you are organising. Three programming languages will be represented: Python, Ruby and JavaScript.
# Your task is to return either:
# True if the number of meetup participants representing any of the three programming languages is ** at most 2 times higher than the number of developers representing any of the remaining programming languages**; or
# False otherwise.
# For example, given the following input array:
# list1 = [
#     { 'firstName': 'Daniel', 'lastName': 'J.', 'country': 'Aruba', 'continent': 'Americas', 'age': 42, 'language': 'Python' },
#     { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 22, 'language': 'Ruby' },
#     { 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 43, 'language': 'Ruby' },
#     { 'firstName': 'Hanna', 'lastName': 'L.', 'country': 'Hungary', 'continent': 'Europe', 'age': 95, 'language': 'JavaScript' },
#     { 'firstName': 'Jayden', 'lastName': 'P.', 'country': 'Jamaica', 'continent': 'Americas', 'age': 18, 'language': 'JavaScript' },
#     { 'firstName': 'Joao', 'lastName': 'D.', 'country': 'Portugal', 'continent': 'Europe', 'age': 25, 'language': 'JavaScript' }
#     ]
# Your function should return false as the number of JavaScript developers (3) is 3 times higher than the number of Python developers (1). It can't be more than 2 times higher to be regarded as language-diverse.
# Notes:
# The strings representing all three programming languages will always be formatted in the same way (e.g. 'JavaScript' will always be formatted with upper-case 'J' and 'S'.
# The input array will always be valid and formatted as in the example above.
# Each of the 3 programming languages will always be represented.


# Function
def is_language_diverse(list: list): 
    # Create empty list for storing count of languages.
    javascript_list: list = []
    python_list: list = []
    ruby_list: list = []
    
    for developer in list:
        # Store language in a variable for clairty.
        language: str = developer['language']
        # For each language, add it to its specified language list.
        if language == 'JavaScript':
            javascript_list.append(language)
        elif language == 'Python':
            python_list.append(language)
        else:
            ruby_list.append(language)
    # Create list to store the counts of each language.
    count_list: list = []
    # Add length of each language list as its count.
    count_list.append(len(javascript_list))
    count_list.append(len(python_list))
    count_list.append(len(ruby_list))
    # Sort the count_list from highest count to lowest.
    sorted_count: list = sorted(count_list, reverse=True)
    # If the largest count divided by the next largest count is larger than 2, then its not diverse.   
    if sorted_count[0] / sorted_count[1] > 2.0:
        return False
    # If the largest count divided by the third largest count is larger than 2, then its not diverse.   
    elif sorted_count[0] / sorted_count[2] > 2.0:
        return False
    # For the meetup the language is diverse.
    else:
        return True


# Test Cases
import codewars_test as test
from solution import is_language_diverse

@test.describe('Sample Test Cases')
def example_tests():

    @test.it('Example Test Case')
    def example_test_case():
        list1 = [
          { 'firstName': 'Daniel', 'lastName': 'J.', 'country': 'Aruba', 'continent': 'Americas', 'age': 42, 'language': 'Python' },
          { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 22, 'language': 'Ruby' },
          { 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 43, 'language': 'Ruby' },
          { 'firstName': 'Hanna', 'lastName': 'L.', 'country': 'Hungary', 'continent': 'Europe', 'age': 95, 'language': 'JavaScript' },
          { 'firstName': 'Jayden', 'lastName': 'P.', 'country': 'Jamaica', 'continent': 'Americas', 'age': 18, 'language': 'JavaScript' },
          { 'firstName': 'Joao', 'lastName': 'D.', 'country': 'Portugal', 'continent': 'Europe', 'age': 25, 'language': 'JavaScript' }
        ]
        
        list2 = [
          { 'firstName': 'Daniel', 'lastName': 'J.', 'country': 'Aruba', 'continent': 'Americas', 'age': 42, 'language': 'Python' },
          { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 22, 'language': 'Ruby' },
          { 'firstName': 'Hanna', 'lastName': 'L.', 'country': 'Hungary', 'continent': 'Europe', 'age': 95, 'language': 'JavaScript' },
          { 'firstName': 'Jayden', 'lastName': 'P.', 'country': 'Jamaica', 'continent': 'Americas', 'age': 18, 'language': 'JavaScript' },
          { 'firstName': 'Joao', 'lastName': 'D.', 'country': 'Portugal', 'continent': 'Europe', 'age': 25, 'language': 'JavaScript' }
        ]
        
        list3 = [
          { 'firstName': 'Daniel', 'lastName': 'J.', 'country': 'Aruba', 'continent': 'Americas', 'age': 42, 'language': 'Python' },
          { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 22, 'language': 'Ruby' },
          { 'firstName': 'Jayden', 'lastName': 'P.', 'country': 'Jamaica', 'continent': 'Americas', 'age': 18, 'language': 'JavaScript' },
          { 'firstName': 'Joao', 'lastName': 'D.', 'country': 'Portugal', 'continent': 'Europe', 'age': 25, 'language': 'JavaScript' }
        ]
        
        list4 = [
          { 'firstName': 'Daniel', 'lastName': 'J.', 'country': 'Aruba', 'continent': 'Americas', 'age': 42, 'language': 'Python' },
          { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 22, 'language': 'Ruby' },
          { 'firstName': 'Joao', 'lastName': 'D.', 'country': 'Portugal', 'continent': 'Europe', 'age': 25, 'language': 'JavaScript' }
        ]

        test.assert_equals(is_language_diverse(list1), False)
        test.assert_equals(is_language_diverse(list2), False)
        test.assert_equals(is_language_diverse(list3), True)
        test.assert_equals(is_language_diverse(list4), True)

