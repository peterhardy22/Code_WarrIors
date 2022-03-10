# https://www.codewars.com/kata/598106cb34e205e074000031
# Level 6 kyu

# Directions:
# Story
# The Pied Piper has been enlisted to play his magical tune and coax all the rats out of town.
# But some of the rats are deaf and are going the wrong way!
# How many deaf rats are there?
# Legend
# P = The Pied Piper
# O~ = Rat going left
# ~O = Rat going right
# Example
# ex1 ~O~O~O~O P has 0 deaf rats
# ex2 P O~ O~ ~O O~ has 1 deaf rat
# ex3 ~O~O~O~OP~O~OO~ has 2 deaf rats


# Function
def count_deaf_rats(town):
    # Variables.
    pied_piper: str = 'P'
    rat_going_left: str = 'O~'
    rat_going_right: str = '~O'
    rat_size: int = 2
    # Creates a list of rats to the left of the pied_piper and to the right of the pied_piper.
    rats_list: list = town.split(pied_piper)

    # List of rat_parts ('~' or 'O') to the left of pied_piper
    left_of_piper_list: list = [rat_part for rat_part in rats_list[0]]
    # Remove any empty strings within that rat_parts list.
    while(' ' in left_of_piper_list) :
        left_of_piper_list.remove(' ')
    # Join the elements of the list into a string.
    left_of_piper: str = ''.join(left_of_piper_list)
    # Split that string into a list where each element is 2 characters long (rat_size)
    left_list: list = [left_of_piper[index:index+rat_size] for index in range(0, len(left_of_piper), rat_size)]

    # List of rat_parts ('~' or 'O') to the right of pied_piper
    right_of_piper_list: list = [rat_part for rat_part in rats_list[1]] 
    # Remove any empty strings within that rat_parts list.
    while(' ' in right_of_piper_list) :
        right_of_piper_list.remove(' ')
    # Join the elements of the list into a string.
    right_of_piper: str = ''.join(right_of_piper_list)
    # Split that string into a list where each element is 2 characters long (rat_size)
    right_list: list = [right_of_piper[index:index+rat_size] for index in range(0, len(right_of_piper), rat_size)]

    # Store the count of rats going the wrong direction on the left and right side of the pied_piper    
    left_count: int = left_list.count(rat_going_left)
    right_count: int = right_list.count(rat_going_right)
    # Store sum of rats going in the wrong direction.
    answer: int = left_count + right_count
    
    return answer


# Test Cases
test.it("ex1")
test.assert_equals(count_deaf_rats("~O~O~O~O P"), 0)
  
test.it("ex2")
test.assert_equals(count_deaf_rats("P O~ O~ ~O O~"), 1)
  
test.it("ex3")
test.assert_equals(count_deaf_rats("~O~O~O~OP~O~OO~"), 2)