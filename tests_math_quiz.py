import unittest
from math_quiz import test_generate_Integer, random-arithmatic_Operator, calculate_numbers


class TestMathGame(unittest.TestCase):

    def test_generate_Integer(self):
        # Test if random numbers generated are within the specified range
        min = 1
        max = 10
        for _ in range(1000):  
            # Test a large number of random values
            rand_number = generate_Integer(min, max)
            self.assertTrue(min <= rand_number <= max)

    def test_random-arithmatic_Operator(self):
    """ test if the generated operated is one of the defined arithmetic operators """
        arithmetic_Operators = {random-arithmatic_Operator
            self.assertIn(arithmetic_Operators, valid_Operators)
        pass


    def test_calculate_numbers(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (-2,3, '-', -(-2)-3, -1),
                (9,1, '*', '9*1', 9)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                operation, answer = calculate_numbers(n1,n2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)
        pass

if __name__ == "__main__":
    unittest.main()
