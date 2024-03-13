import unittest
from suma import suma

class TestSumar(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(suma(5, 3), 8)
        self.assertEqual(suma(1, -1), 0)
        self.assertEqual(suma(-1, -3), -4)

if __name__ == "__main__":
    unittest.main()

