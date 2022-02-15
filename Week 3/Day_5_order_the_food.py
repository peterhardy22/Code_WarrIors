# https://www.codewars.com/kata/583952fbc23341c7180002fd/train/python
# Level 7 kyu

# Directions:
# You will be given an array of objects representing data about developers who have signed up to attend the next coding meetup that you are organising.
# Your task is to return an object which includes the count of food options selected by the developers on the meetup sign-up form.
# Example:
# list1 = [
#     { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C', 'meal': 'vegetarian' },
#     { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript', 'meal': 'standard' },
#     { 'firstName': 'Ramona', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby', 'meal': 'vegan' },
#     { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C', 'meal': 'vegetarian' },
# ]
# Return:
# { 'vegetarian': 2, 'standard': 1, 'vegan': 1 }
# Notes:
# The order of the meals count in the object does not matter.
# The count value should be a valid number.
# The input array will always be valid and formatted as in the example above.
# there are 5 possible meal options and the strings representing the selected meal option will always be formatted in the same way, as follows: 
# 'standard', 'vegetarian', 'vegan', 'diabetic', 'gluten-intolerant'.


# Function
def order_food(lst): 
    meal_list = [person['meal'] for person in lst]
    # .count() returns the number of times a value appears in a list.
    answer = {meal : meal_list.count(meal) for meal in meal_list}
    
    return answer


# Test Cases
import codewars_test as test
from solution import order_food

@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        list1 = [
            { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C', 'meal': 'vegetarian' },
            { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript', 'meal': 'standard' },
            { 'firstName': 'Ramona', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby', 'meal': 'vegan' },
            { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C', 'meal': 'vegetarian' },
        ]
        
        answer = { 'vegetarian': 2, 'standard': 1, 'vegan': 1 }
        
        test.assert_equals(order_food(list1), answer)