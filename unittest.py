import unittest
from main import square_root, process_random_integer, list_divisibles

class TestFunctions(unittest.TestCase):

    # Tests for square_root function
    def test_square_root_positive(self):
        self.assertEqual(square_root(4), 2)
        self.assertAlmostEqual(square_root(2), math.sqrt(2))

    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            square_root(-1)

    # Tests for process_random_integer
    def test_process_random_integer(self):
        for _ in range(10):  # Run multiple tests
            try:
                result = process_random_integer()
                self.assertLessEqual(result, 4)
            except ValueError as e:
                self.assertIn("exceeds 4", str(e))

    # Tests for list_divisibles function
    def test_list_divisibles(self):
        self.assertEqual(list_divisibles(1), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(list_divisibles(2), [2, 4, 6, 8, 10])
        self.assertEqual(list_divisibles(3), [3, 6, 9])
        self.assertEqual(list_divisibles(11), [])

if __name__ == "__main__":
    unittest.main()
