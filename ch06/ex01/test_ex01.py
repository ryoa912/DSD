import unittest
import doctest
import src_ex01 as src


class TestEx01(unittest.TestCase):
        def test_thing(self):
                expected = "<class 'src_ex01.Thing'>"
                actual = str(src.Thing)
                self.assertEqual(expected, actual)
                example = src.Thing()
                print(example)

if __name__ == '__main__':
    unittest.main()