import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(0,3), 0)
        self.assertEqual(mul(4, 3), 12)
        self.assertEqual(mul(-5, 8), -40)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(1,4),4)
        self.assertEqual(div(2, 4), 2)
        self.assertEqual(div(7, 2), 3.5)
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithmic(0, 10)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(1.5, 2.0), (1.5**2 + 2.0**2) ** 0.5)
    #     fill in code

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-5)
        self.asserEqual(square_root(9), 3)
        self.asserAlmostEqual(square_root(2), 2 ** 0.5)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()