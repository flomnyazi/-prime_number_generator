import unittest
from prime_number_generator import prime
class Testprimegenerator(unittest.TestCase):
    def test_number_equals_zero(self):
    	self.assertFalse(prime(0))
    def test_number_equals_one(self):
    	self.assertFalse(prime(1))
    def test_number_equals_two(self):
    	self.assertFalse(prime(2))
    def test_number_divided_by_two(self):
    	self.assertFalse(prime(4))
    def test_number_divided_by_test_number(self):
        self.assertTrue(prime(7))	

if __name__ == "__main__":
    unittest.main()
