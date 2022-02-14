# https://www.codewars.com/kata/5cd5ba1ce4471a00256930c0/train/python
# Level 7 kyu

# Directions:
# Implement a function which returns the last D digits of an integer N as a list.
# Special cases:
# If D > (the number of digits of N), return all the digits.
# If D <= 0, return an empty list.


# Function
def solution(n,d):
    if d > n:
        return [int(x) for x in str(n)]
    elif d <= 0:
        return []
    else:
        numbers_list = [int(x) for x in str(n)]
        return numbers_list[-d:]


# Test Cases
test.describe('Example tests')
test.assert_equals(solution(1,1),[1])
test.assert_equals(solution(123767,4),[3,7,6,7])
test.assert_equals(solution(0,1),[0])
test.assert_equals(solution(34625647867585,10),[5,6,4,7,8,6,7,5,8,5])

test.describe('d <= 0')
test.assert_equals(solution(1234,0),[])
test.assert_equals(solution(24134,-4),[])

test.describe('d > number of digits in n')
test.assert_equals(solution(1343,5),[1,3,4,3])