# https://www.codewars.com/kata/572b6b2772a38bc1e700007a/train/python
# Level 8 kyu

# Directions:
# You'll be given a string, and have to return the sum of all characters as an int. 
# The function should be able to handle all ASCII characters.
# Examples:
# uniTotal("a") == 97
# uniTotal("aaa") == 291


# Function
def uni_total(s):
    if len(s) == 0:
        return 0
    elif len(s) >= 2:
        letters = list(s)
        sum = 0
        for letter in letters:
            print(letter)
            sum += ord(letter)
        return sum
    else:
        return ord(s)


# Test Cases
test.describe("Basic tests")
test.it("Should work with Single Letters")
test.assert_equals(uni_total("a"), 97)
test.assert_equals(uni_total("b"), 98)
test.assert_equals(uni_total("c"), 99)
test.it("no chars should return zero")
test.assert_equals(uni_total(""), 0)
test.it("should work with multiple letters")
test.assert_equals(uni_total("aaa"), 291)
test.assert_equals(uni_total("abc"), 294)
test.it("should work with sentences and spaces")
test.assert_equals(uni_total("Mary Had A Little Lamb"),1873)
test.assert_equals(uni_total("Mary had a little lamb"),2001)
test.assert_equals(uni_total("CodeWars rocks"),1370)
test.assert_equals(uni_total("And so does Strive"),1661)