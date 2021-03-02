"""This file contains a little challenge that the interviewer proposed to
the developer. 

Contains:
- a function that receives a list of numbers and returns a list of tuples,
each tuple containing the original value and it's square.
- a class that contains a unit test for the created function.

How to execute the test:
- Run in the console "python interview_challenge.py"
"""

import unittest


def square_list(numbers):
    """This function receives a list of numbers, and returns a list of tuples,
    each tuple contains in the first position the original number given by the
    input list, and the second position contains the square of that number.

    Args:
        numbers ([list]): list of numbers. Example input [1,2,3]

    Returns:
        [List[Tuples[numeric]]]: List of tuples of numbers. Example output [(1,1),(2,4),(3,9)]]
    """
    final_list = []
    for n in numbers:
        final_list.append((n, n**2))
        
    return final_list


class TestFunction(unittest.TestCase):
    """Class that has a unique unit test for the above function
    """
    def test_1(self):
        returned_list = square_list([1,2,3])
        expected_list = [(1, 1), (2, 4), (3, 9)]
        self.assertListEqual(returned_list, expected_list)

if __name__ == '__main__':
    unittest.main()
