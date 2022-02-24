# https://www.codewars.com/kata/5827bc50f524dd029d0005f2
# Level 7 kyu

# Directions:
# You will be given an array of objects (associative arrays in PHP) representing data about developers who have signed up to attend the next coding meetup that you are organising. The list is ordered according to who signed up first.
# Your task is to return one of the following strings:
# < firstName here >, < country here > of the first Python developer who has signed up; or
# There will be no Python developers if no Python developer has signed up.
# For example, given the following input array:
# list1 = [
#   { "first_name": "Mark", "last_name": "G.", "country": "Scotland", "continent": "Europe", "age": 22, "language": "JavaScript" },
#   { "first_name": "Victoria", "last_name": "T.", "country": "Puerto Rico", "continent": "Americas", "age": 30, "language": "Python" },
#   { "first_name": "Emma", "last_name": "B.", "country": "Norway", "continent": "Europe", "age": 19, "language": "Clojure" }
# ]
# Your function should return Victoria, Puerto Rico.
# Notes:
# The input array will always be valid and formatted as in the example above.


# Function
def get_first_python(users):
    # Loop through each dictionoary (user) in the users list.
    for developer in users:
        # Store language as a variable for clarity.
        language: str = developer['language']
        # If that user's language is Python...
        if language == 'Python':
            # Store first_name and country as variables for clarity.
            first_name: str = developer['first_name']
            country: str = developer['country']
            # Return first_name and country of developer.
            return f'{first_name}, {country}'
    # No Python developers in users list.
    return 'There will be no Python developers'


# Test Cases
test.describe("Basic tests")
list1 = [
  { "first_name": "Mark", "last_name": "G.", "country": "Scotland", "continent": "Europe", "age": 22, "language": "JavaScript" },
  { "first_name": "Victoria", "last_name": "T.", "country": "Puerto Rico", "continent": "Americas", "age": 30, "language": "Python" },
  { "first_name": "Emma", "last_name": "B.", "country": "Norway", "continent": "Europe", "age": 19, "language": "Clojure" }
]

list2 = [
  { "first_name": "Kseniya", "last_name": "T.", "country": "Belarus", "continent": "Europe", "age": 29, "language": "JavaScript" },
  { "first_name": "Amar", "last_name": "V.", "country": "Bosnia and Herzegovina", "continent": "Europe", "age": 32, "language": "Ruby" }
]

list3 = [
  { "first_name": "Sofia", "last_name": "P.", "country": "Italy", "continent": "Europe", "age": 41, "language": "Clojure" },
  { "first_name": "Jayden", "last_name": "P.", "country": "Jamaica", "continent": "Americas", "age": 42, "language": "JavaScript" },
  { "first_name": "Sou", "last_name": "B.", "country": "Japan", "continent": "Asia", "age": 43, "language": "Python" },
  { "first_name": "Rimas", "last_name": "C.", "country": "Jordan", "continent": "Asia", "age": 44, "language": "Java" }
]

test.assert_equals(get_first_python(list1), "Victoria, Puerto Rico")
test.assert_equals(get_first_python(list2), "There will be no Python developers")
test.assert_equals(get_first_python(list3), "Sou, Japan")
test.assert_equals(get_first_python(list1+list3), "Victoria, Puerto Rico")
test.assert_equals(get_first_python(list3+list1), "Sou, Japan")