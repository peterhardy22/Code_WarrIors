# https://www.codewars.com/kata/582dace555a1f4d859000058
# Level 7 kyu

# Directions:
# You will be given an array of objects representing data about developers who have signed up to attend the next coding meetup that you are organising.
# Given the following input array:
# list1 = [
#   { 'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil', 'continent': 'Americas', 'age': 22, 'language': 'JavaScript', 'githubAdmin': 'yes' },
#   { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 49, 'language': 'Ruby', 'githubAdmin': 'no' },
#   { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 34, 'language': 'JavaScript', 'githubAdmin': 'yes' },
#   { 'firstName': 'Piotr', 'lastName': 'B.', 'country': 'Poland', 'continent': 'Europe', 'age': 128, 'language': 'JavaScript', 'githubAdmin': 'no' }
#   ]
# Write a function that when executed as findAdmin(list1, 'JavaScript') returns only the JavaScript developers who are GitHub admins:
# [
#   { 'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil', 'continent': 'Americas', 'age': 22, 'language': 'JavaScript', 'githubAdmin': 'yes' },
#   { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 34, 'language': 'JavaScript', 'githubAdmin': 'yes' }
# ]
# Notes:
# The original order should be preserved.
# If there are no GitHub admin developers in a given language then return an empty array [].
# The input array will always be valid and formatted as in the example above.
# The strings representing whether someone is a GitHub admin will always be formatted as 'yes' and 'no' (all lower-case).
# The strings representing a given language will always be formatted in the same way (e.g. 'JavaScript' will always be formatted with upper-case 'J' and 'S'.


# Function
def find_admin(list, language): 
    # Create empty list for storing GitHub admins.
    admin_list = []
    # Loop through each admin (dictionary) in the list.
    for admin in list:
        # If the admin has a match with the provided language and is a githubAdmin then they are a GitHub admin.
        if admin['language'] == language and admin['githubAdmin'] == 'yes':
            # Add that admin to the admin_list.
            admin_list.append(admin)
    # Return the admin's stored.
    return admin_list


# Test Cases
import codewars_test as test
from solution import find_admin

@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        list1 = [
          { 'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil', 'continent': 'Americas', 'age': 22, 'language': 'JavaScript', 'githubAdmin': 'yes' },
          { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 49, 'language': 'Ruby', 'githubAdmin': 'no' },
          { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 34, 'language': 'JavaScript', 'githubAdmin': 'yes' },
          { 'firstName': 'Piotr', 'lastName': 'B.', 'country': 'Poland', 'continent': 'Europe', 'age': 128, 'language': 'JavaScript', 'githubAdmin': 'no' }
        ]
        
        answer1 = [
          { 'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil', 'continent': 'Americas', 'age': 22, 'language': 'JavaScript', 'githubAdmin': 'yes' },
          { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 34, 'language': 'JavaScript', 'githubAdmin': 'yes' }
        ]

        test.assert_equals(find_admin(list1, 'JavaScript'), answer1)
        test.assert_equals(find_admin(list1, 'Ruby'), [])
        test.assert_equals(find_admin(list1, 'Python'), [])