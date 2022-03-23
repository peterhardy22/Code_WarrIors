# https://www.codewars.com/kata/6210fb7aabf047000f3a3ad6
# Level 6 kyu

# Directions:
# In this task, you need to restore a string from a list of its copies.
# You will receive an array of strings. All of them are supposed to be the same as the original but, unfortunately, they were corrupted which means some of the characters were replaced with asterisks ("*").
# You have to restore the original string based on non-corrupted information you have. 
# If in some cases it is not possible to determine what the original character was, use "#" character as a special marker for that.
# If the array is empty, then return an empty string.
# Examples:
# input = [
#   "a*cde",
#   "*bcde",
#   "abc*e"
# ]
# result = "abcde"
# input = [
#   "a*c**",
#   "**cd*",
#   "a*cd*"
# ]
# result = "a#cd#"


# Function
def assemble(input):  
    # If input is empty return nothing.  
    if input == []:
        return ''    
    # Store first item in input list to use as a building block.
    answer_list: list = [character for character in input[0]]
    
    # Loop through everything but the first item in the input since it is our reference.
    for word in input[1:]:
        # Convert each item in the input list, into its own list with each character being an item.
        word_list: list = [character for character in word]
        # Loop through each character
        for index, character in enumerate(word_list):
            # If the character is not a '*', does not equal the character already in place, and that character its replacing is a '*'...
            if character != '*' and character != answer_list[index] and answer_list[index] == '*':
                # Replace the character.
                answer_list[index] = character
    # Convert answer_list into a string.
    answer: str = ''.join(answer_list)
    # Loop through each character to find any leftover '*'.
    for character in answer:
        if character == '*':
            # If found, convert to a '#'.
            answer = answer.replace('*', '#')
    
    return answer  


# Test Cases
import codewars_test as test
from solution import assemble

@test.describe('Example')
def test_group():
    @test.it('Should pass')
    def test_case():
        test.assert_equals(assemble(['H*llo, W*rld!', 'Hel*o, *or*d!', '*ello* World*']), 'Hello, World!');
        test.assert_equals(assemble(['.** . ." ."" ! ! .', '. . . ." **" ! * .', '* . .*.* ."" * ! .', '. . .*." .**** ! .', '**. * .* .*" ! ! .']), '. . . ." ."" ! ! .');
        test.assert_equals(assemble(['. . . .', '. . . .', '. . . .', '. . . .', '. . . .']), '. . . .');
        test.assert_equals(assemble(['12***6789', '**3456789', '12345**8*', '***456**9', '1*3*5*7*9', '*2*456789']), '123456789');
        test.assert_equals(assemble(['******', '******', '******', '******']), '######');
        test.assert_equals(assemble(['*#*#*#*#*#*#*#*', '*#*#*#*#*#*#*#*', '*#*#*#*#*#*#*#*', '*#*#*#*#*#*#*#*']), '###############');
        test.assert_equals(assemble([]), '');
