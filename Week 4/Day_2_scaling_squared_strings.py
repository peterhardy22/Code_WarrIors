# https://www.codewars.com/kata/56ed20a2c4e5d69155000301
# Level 7 kyu

# Directions:
# You are given a string of n lines, each substring being n characters long. For example:
# s = "abcd\nefgh\nijkl\nmnop"
# We will study the "horizontal" and the "vertical" scaling of this square of strings.
# A k-horizontal scaling of a string consists of replicating k times each character of the string (except '\n').
# Example: 2-horizontal scaling of s: => "aabbccdd\neeffgghh\niijjkkll\nmmnnoopp"
# A v-vertical scaling of a string consists of replicating v times each part of the squared string.
# Example: 2-vertical scaling of s: => "abcd\nabcd\nefgh\nefgh\nijkl\nijkl\nmnop\nmnop"
# Function scale(strng, k, v) will perform a k-horizontal scaling and a v-vertical scaling.


# Function
def scale(string, k, v):
    if string == '':
        return ''
    else:
        # Create chunks of the string that are split on the \n.
        chunks: list = string.split('\n')
        # Empty list for storing chunks repeated k times.
        k_chunks: list = []
        
        for chunk in chunks:
            # Mulitply characters in each chunk k amount of times
            k_chunk: list = ''.join([character*k for character in chunk])
            # Add that new chunk to the k_chunks list.
            k_chunks.append(k_chunk)
            
        # Empty list for storing chunks repeated v times.
        v_chunks: list = []

        for chunk in k_chunks:
            # Create new chunk that adds the \n to the end then multiply that v amount of times.
            ender_chunk = (f'{chunk}\n') * v
            # Add that new chunk to the v_chunks list.
            v_chunks.append(ender_chunk)
        # Join all v_chunks to together and take away the last \n in the string.
        return ''.join(v_chunks)[:-1]


# Test Cases
def testing(actual, expected):
    test.assert_equals(actual, expected)

test.describe("scale")
test.it("Basic tests")
a = "abcd\nefgh\nijkl\nmnop"
r = "aabbccdd\naabbccdd\naabbccdd\neeffgghh\neeffgghh\neeffgghh\niijjkkll\niijjkkll\niijjkkll\nmmnnoopp\nmmnnoopp\nmmnnoopp"
testing(scale(a, 2, 3), r)
testing(scale("", 5, 5), "")
testing(scale("Kj\nSH", 1, 2),"Kj\nKj\nSH\nSH")