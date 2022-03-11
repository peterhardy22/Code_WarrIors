# https://www.codewars.com/kata/569d488d61b812a0f7000015
# Level 6 kyu

# Directions:
# A stream of data is received and needs to be reversed.
# Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:
# 11111111  00000000  00001111  10101010
#  (byte1)   (byte2)   (byte3)   (byte4)
# should become:
# 10101010  00001111  00000000  11111111
#  (byte4)   (byte3)   (byte2)   (byte1)
# The total number of bits will always be a multiple of 8.
# The data is given in an array as such:
# [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]


# Function
def data_reverse(data):
    # Loop through string and break into 8 character bits.
    bit: int = 8
    bit_chunks: list = [data[index:index+bit] for index in range(0, len(data), bit)]
    
    # Reverse list of bit_chunks.
    reversed_bit_chunks = bit_chunks[::-1]
    
    # Turn list of bit_chunks in array of individual numbers.
    answer: list = [number for bit_chunk in reversed_bit_chunks for number in bit_chunk]

    return answer


# Test Cases
from solution import data_reverse
import codewars_test as test

@test.describe("Testing...")
def _():

    @test.it("fixed tests")
    def _():
        data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
        data2 = [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
        test.assert_equals(data_reverse(data1),data2)

        data3 = [0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1]
        data4 = [0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0]
        test.assert_equals(data_reverse(data3),data4)