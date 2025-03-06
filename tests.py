import unittest
from sort_package import sort


class TestSortFunction(unittest.TestCase):
    def test_bulky(self):
        self.assertEqual(sort(100, 100, 100, 19), "SPECIAL")

    def test_heavy(self):
        self.assertEqual(sort(50, 50, 50, 21), "SPECIAL")

    def test_both_bulky_and_heavy(self):
        self.assertEqual(sort(100, 100, 100, 21), "REJECTED")

    def test_standard(self):
        self.assertEqual(sort(30, 40, 50, 10), "STANDARD")

    def test_bulky_by_dimension(self):
        self.assertEqual(sort(150, 50, 50, 10), "SPECIAL")

    def test_heavy_by_mass(self):
        self.assertEqual(sort(10, 10, 10, 30), "SPECIAL")


if __name__ == "__main__":
    unittest.main()