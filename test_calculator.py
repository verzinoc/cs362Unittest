import unittest
import calculator

class TestCalculator(unittest.TestCase):
   def test_1add(self):
      result = calculator.addition(3, 4)
      self.assertEqual(result, 7)

   def test_2add(self):
      result = calculator.addition(122, -1)
      self.assertEqual(result, 121)

   def test_3sub(self):
      result = calculator.subtraction(3, 4)
      self.assertEqual(result, -1)

   def test_4sub(self):
      result = calculator.subtraction(1999, 1999)
      self.assertEqual(result, 0)

   def test_5mul(self):
      result = calculator.multiplication(3, 0)
      self.assertEqual(result, 0)

   def test_6mul(self):
      result = calculator.multiplication(3, -4)
      self.assertEqual(result, -12)

   def test_7div(self):
      result = calculator.division(4, -2)
      self.assertEqual(result, -2)

   def test_8div(self):
      result = calculator.division(3, 0)
      self.assertEqual(result, "ERROR")


if __name__ == "__main__":
   unittest.main(verbosity=2)
