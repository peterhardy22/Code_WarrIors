# https://www.codewars.com/kata/55c45be3b2079eccff00010f
# Level 6 kyu

# Directions:
# Your task is to sort a given string. Each word in the string will contain a single number. 
# This number is the position the word should have in the result.
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
# If the input string is empty, return an empty string. 
# The words in the input String will only contain valid consecutive numbers.
# Examples
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
# ""  -->  ""


# Function
def order(sentence):
    # Nothing in, nothing out.
    if sentence == '':
        return ''
    # Create list of each word in the provided sentence.
    sentence_list: list = sentence.split(' ')
    # Create empty list for storing answer that is the same length as sentence_list.
    answer_list: list = [' '] * len(sentence_list)
    # For each word in the sentence...
    for index, word in enumerate(sentence_list):
        # For each character in the word...
        for character in word:
            # If the character is a number...
            if character.isdigit():
                # Store that number for positioning in answer.
                position: int = int(character)
        # If the word's position is 1, make it the first index in the answer.
        if position == 1:
            answer_list[0] = word
        # Else the word's indexing is determined by its position minus 1.
        else:
            answer_list[position - 1] = word
    # Convert answer_list back into a string.
    answer: str = ' '.join(answer_list)
    
    return answer
    

# Test Cases
test.assert_equals(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
test.assert_equals(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
test.assert_equals(order(""), "")