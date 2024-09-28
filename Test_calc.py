import unittest
from Calculator import Calculator

class TestCalculator(unittest.TestCase):
  #setUp method is overridden from the parent class TestCase
  def setUp(self):
    self.calculator = Calculator()
  #Each test method starts with the keyword test_
  def test_add(self):
    self.assertEqual(self.calculator.add(3,5), 8)
  def test_subtract(self):
    self.assertEqual(self.calculator.subtract(7,2), 5)
  def test_multiply(self):
    self.assertEqual(self.calculator.multiply(4,8), 32)
  def test_divide(self):
    self.assertEqual(self.calculator.divide(25,5), 5)
# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()