# https://www.codewars.com/kata/56786a687e9a88d1cf00005d
# Level 7 kyu

# Directions:
# You are going to be given a word. 
# Your job will be to make sure that each character in that word has the exact same number of occurrences. 
# You will return true if it is valid, or false if it is not.
# For this kata, capitals are considered the same as lowercase letters. Therefore: "A" == "a"
# The input is a string (with no spaces) containing [a-z],[A-Z],[0-9] and common symbols. The length will be 0 < length < 100.
# Examples:
# "abcabc" is a valid word because "a" appears twice, "b" appears twice, and"c" appears twice.
# "abcabcd" is NOT a valid word because "a" appears twice, "b" appears twice, "c" appears twice, but "d" only appears once!
# "123abc!" is a valid word because all of the characters only appear once in the word.


# Function
def validate_word(word):
    # Word must not be an empty string and must be under 100 characters.
    if 0 < len(word) < 100:
        # Turn all characters in word to lower case.
        lower_word = word.lower()
        # Create a list of counts for how many times a charcter occurs in the word.
        occurances = [lower_word.count(character) for character in lower_word]
        # Turn occurances into a set since elements cannot be repeated.
        # If the length of that set only contains one elemnt that means all charcteers wre repeated equal times.
        if len(set(occurances)) == 1:
            return True
        # Else, the length of the set had more that one element and therefore some character in word was reapeated an unequal amount of times.
        else:
            return False
    # Word did not fit the length requirements.
    else:
        return False


# Test Cases
test.assert_equals(validate_word("abcabc"),True)
test.assert_equals(validate_word("Abcabc"),True)
test.assert_equals(validate_word("AbcabcC"),False)
test.assert_equals(validate_word("AbcCBa"),True)
test.assert_equals(validate_word("pippi"),False)
test.assert_equals(validate_word("?!?!?!"),True)
test.assert_equals(validate_word("abc123"),True)
test.assert_equals(validate_word("abcabcd"),False)
test.assert_equals(validate_word("abc!abc!"),True)
test.assert_equals(validate_word("abc:abc"),False)