import unittest
import main

class TestMainFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(main.add(2, 3), 5)
        self.assertEqual(main.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(main.subtract(5, 3), 2)
        self.assertEqual(main.subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(main.multiply(2, 3), 6)
        self.assertEqual(main.multiply(-1, 3), -3)

    def test_divide(self):
        self.assertEqual(main.divide(6, 3), 2)
        self.assertAlmostEqual(main.divide(7, 3), 7/3)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            main.divide(5, 0)

if __name__ == "__main__":
    unittest.main()
