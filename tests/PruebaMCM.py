# test_mcm_library.py

import unittest
from src.logica.MCM import lcm_two, lcm_three


class TestLCMFunctions(unittest.TestCase):

    def test_lcm_two(self):
        self.assertEqual(lcm_two(4, 6), 12)
        self.assertEqual(lcm_two(15, 20), 60)
        self.assertEqual(lcm_two(7, 5), 35)

    def test_lcm_three(self):
        self.assertEqual(lcm_three(4, 6, 8), 24)
        self.assertEqual(lcm_three(3, 5, 7), 105)
        self.assertEqual(lcm_three(5, 10, 15), 30)


if __name__ == "__main__":
    unittest.main()