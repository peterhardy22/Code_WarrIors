# https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991
# Level 6 kyu

# Directions:
# The input is a string str of digits. 
# Cut the string into chunks (a chunk here is a substring of the initial string) of size sz (ignore the last chunk if its size is less than sz).
# If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2, reverse that chunk; otherwise rotate it to the left by one position. 
# Put together these modified chunks and return the result as a string.
# If
# sz is <= 0 or if str is empty return ""
# sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".
# Examples:
# revrot("123456987654", 6) --> "234561876549"
# revrot("123456987653", 6) --> "234561356789"
# revrot("66443875", 4) --> "44668753"
# revrot("66443875", 8) --> "64438756"
# revrot("664438769", 8) --> "67834466"
# revrot("123456779", 8) --> "23456771"
# revrot("", 8) --> ""
# revrot("123456779", 0) --> "" 
# revrot("563000655734469485", 4) --> "0365065073456944"
# Example of a string rotated to the left by one position:
# s = "123456" gives "234561".


# Function
def revrot(string, size):
    # Invalid possibilities.
    if size <= 0 or string == '' or size > len(string):
        return ''
    
    # Store remainder of string to know how many characters to ignore when creating chunks.
    remainder_of_string: int = len(string) % size
    
    #  Get rid of left over characters
    if remainder_of_string != 0:
        string: str = string[:-remainder_of_string]
    
    # Create list of chunks based on size.
    chunks_list: list = [string[item:item+size] for item in range(0, len(string), size)]
    
    # Create empty list to store converted chunks.
    answer_list: list = []
    
    for chunk in chunks_list:
        # Create counter to storing sum of power of 3.
        counter: int = 0
        
        for number in chunk:
            counter: int = counter + (int(number) ** 3)
        # If the counter is divisible by 2...
        if counter % 2 == 0:
            # Reverse the chunk
            answer_list.append(chunk[::-1])
        else:
            # Rotate the chunk 1 character.
            answer_list.append(f'{chunk[1:]}{chunk[0]}')
            
    return ''.join(answer_list)

    

# Test Cases
def testing(actual, expected):
    test.assert_equals(actual, expected)
    
test.describe("revrot")
test.it("Basic tests")
testing(revrot("1234", 0), "")
testing(revrot("", 0), "")
testing(revrot("1234", 5), "")
s = "733049910872815764"
testing(revrot(s, 5), "330479108928157")