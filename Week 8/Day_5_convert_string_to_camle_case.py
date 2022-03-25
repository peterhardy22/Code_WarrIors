# https://www.codewars.com/kata/517abf86da9663f1d2000003
# Level 6 kyu

# Directions:
# Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
# The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"


# Function
def to_camel_case(text):
    print(text)
    # If the input is empty, return empty string.
    if text == '':
        return ''
    else:
        # Create empty list to store answer.
        needs_edits_list: list = []
        # Determine if the input uses '-' or '_', and split string into a list accordingly.
        if '-' in text:
            text_list: list = text.split('-')
        else:
            text_list: list = text.split('_')

        # Find out if any '_' or '-' character's remain in any elements in the list.
        for text in text_list:
            # If they do, split that item on the character and append new list to needs_edits_list.
            if '_' in text:
                new_text_list: list = text.split('_')
                needs_edits_list.append(new_text_list)
            elif '-' in text:
                new_text: list = text.split('-')
                needs_edits_list.append(new_text_list)
            else:    
                needs_edits_list.append(text)
                
        # Create empty list to store answer items.
        answer: list = []
        # Clean up any items in the answer list that are lists themselves.
        for index, item in enumerate(needs_edits_list):
            # First word in answer does not get capitalized.
            if index == 0:
                # If item is a list, then only add the first item to the answer.
                if type(item) == list:
                    answer.append(item[0])
                    # Capitalize other reminaing items in list.
                    for i in item[1:]:
                        answer.append(i.capitalize())
                else:
                    answer.append(item)
            else:
                # If item is a list...
                if type(item) == list:
                    # Add each item and capitalize first letter.
                    for i in item:
                        answer.append(i.capitalize())
                else:
                    answer.append(item.capitalize())
        
        # Return answer as a string.
        return ''.join(answer)

# Test Cases
test.describe("Testing function to_camel_case")
test.it("Basic tests")
test.assert_equals(to_camel_case(''), '', "An empty string was provided but not returned")
test.assert_equals(to_camel_case("the_stealth_warrior"), "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value")
test.assert_equals(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value")
test.assert_equals(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")