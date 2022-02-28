# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272
# Level 6 kyu

# Directions:
# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
# You need to return the highest scoring word as a string.
# If two words score the same, return the word that appears earliest in the original string.
# All letters will be lowercase and all inputs will be valid.


# Function
def high(string: str) -> str:
    # Create list of alphabet letters.
    alphabet_list: list = list('abcdefghijklmnopqrstuvwxyz')
    # Create dictionary with alphabet letters as the key and score as the value.
    alphabet_score_dict: dict = {letter : (index+1) for index, letter in enumerate(alphabet_list)}
    # Store each word as its own string.
    word_list: list = string.split(' ')
    # Create empty dictionary to store the score of each word.
    word_score_dict: dict = {}
    # Loop through each word in the list of words.
    for word in word_list:
        # Create tracker for tallying up word score
        word_score: int = 0
        for character in word:
            # Store the score of each character based of the scores from the aplhabet score dictionary.
            score: int = alphabet_score_dict[character]
            # With each iteration add score of character to total word score.
            word_score: int = word_score + score
        # Add word as key and word score as value to dictionary.
        word_score_dict[word] = word_score
    # Sort dictionary by highest key value and store the first item in the dictionary.
    highest_scoring_word: str = sorted(word_score_dict, key=word_score_dict.get, reverse=True)[0]

    return highest_scoring_word


# Test Cases
# import codewars_test as test
# from solution import high

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(high('man i need a taxi up to ubud'), 'taxi')
#         test.assert_equals(high('what time are we climbing up the volcano'), 'volcano')
#         test.assert_equals(high('take me to semynak'), 'semynak')
#         test.assert_equals(high('aa b'), 'aa')
#         test.assert_equals(high('b aa'), 'b')
#         test.assert_equals(high('bb d'), 'bb')
#         test.assert_equals(high('d bb'), 'd')
#         test.assert_equals(high("aaa b"), "aaa")