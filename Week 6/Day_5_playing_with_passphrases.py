# https://www.codewars.com/kata/559536379512a64472000053
# Level 6 kyu

# Directions:
# Everyone knows passphrases. One can choose passphrases from poems, songs, movies names and so on but frequently they can be guessed due to common cultural references. 
# You can get your passphrases stronger by different means. 
# One is the following:
# choose a text in capital letters including or not digits and non alphabetic characters,
# shift each letter by a given number but the transformed letter must be a letter (circular shift),
# replace each digit by its complement to 9,
# keep such as non alphabetic and non digit characters,
# downcase each letter in odd position, upcase each letter in even position (the first character is in position 0),
# reverse the whole result.
# Example:
# your text: "BORN IN 2015!", shift 1
# 1 + 2 + 3 -> "CPSO JO 7984!"
# 4 "CpSo jO 7984!"
# 5 "!4897 Oj oSpC"
# With longer passphrases it's better to have a small and easy program. Would you write it?
# https://en.wikipedia.org/wiki/Passphrase


# Function
def play_pass(string, number):
    # Lists to store references for letters and numbers.
    alphabet_list: list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers_list: list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # List to store reversed_result.
    reversed_answer_list: list = []

    # For each character in the provided string.
    for index, character in enumerate(string):
        # Letter is in even position.
        if character in alphabet_list and index % 2 == 0:
            # Store position of current letter.
            letter_index: int = alphabet_list.index(character)
            # Use letter_index and number to find new letter in circular shift based on number provided.
            new_letter: str = alphabet_list[letter_index-(len(alphabet_list)-number)]
            # Add character to reversed answer list.
            reversed_answer_list.append(new_letter)
        # Letter is in odd position
        elif character in alphabet_list and index % 2 != 0:
            # Store position of current letter.
            letter_index: int = alphabet_list.index(character)
            # Use letter_index and number to find new letter in circular shift based on number provided.
            new_letter: str = alphabet_list[letter_index-(len(alphabet_list)-number)]
            # Add character to reversed answer list and make it lowercase since in an odd position.
            reversed_answer_list.append(new_letter.lower())
        # Replace each digit by its complement to 9.
        elif character in numbers_list:
            complement: int = (len(numbers_list) - 1) - int(character)
            reversed_answer_list.append(str(complement)) 
        # The character is a not a digit or letter, so do nothing to it.
        else:
            reversed_answer_list.append(character)   
    
    # Reverse reversed_answer_list and join into a string for correct answer
    answer: str = ''.join(reversed_answer_list[::-1])
    
    return answer
    

# Test Cases
test.assert_equals(play_pass("I LOVE YOU!!!", 1), "!!!vPz fWpM J")

test.assert_equals(play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2), 
    "4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO")