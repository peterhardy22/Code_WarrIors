# https://www.codewars.com/kata/56747fd5cb988479af000028/train/python
# Level 7 kyu

# Directions:
# Return the middle character of the word. 
# If the word's length is odd, return the middle character. 
# If the word's length is even, return the middle 2 characters.


# Function
def get_middle(s):
    if (len(s) % 2) == 0:
        character_position_2 = int(len(s)/2)
        character_position_1 = character_position_2 - 1
        middle_characters = f'{s[character_position_1]}{s[character_position_2]}'
        return middle_characters
    else:
        return s[int(len(s)/2)]


# Test Cases
test.assert_equals(get_middle("test"),"es")
test.assert_equals(get_middle("testing"),"t")
test.assert_equals(get_middle("middle"),"dd")
test.assert_equals(get_middle("A"),"A")
test.assert_equals(get_middle("of"),"of")