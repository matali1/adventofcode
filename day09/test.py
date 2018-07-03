import unittest

from garbage import parse_string

class MyTestCase(unittest.TestCase):

    def test_group1(self):
        result = parse_string("{}")
        self.assertEqual((1,0), result)

    def test_group2(self):
        result = parse_string("{{{}}}")
        self.assertEqual((6,0), result)

    def test_group3(self):
        result = parse_string("{{}}")
        self.assertEqual((3,0), result)

    def test_group4(self):
        result = parse_string("{{},{}}")
        self.assertEqual((5,0), result)

    def test_group5(self):
        result = parse_string("{{{}, {}, {{}}}}")
        self.assertEqual((16,0), result)

    def test_group6(self):
        result = parse_string("{<{},{},{{}}>}")
        self.assertEqual((1,10), result)

    def test_group7(self):
        result = parse_string("{<a>,<a>,<a>,<a>}")
        self.assertEqual((1,4), result)

    def test_group8(self):
        result = parse_string("{{<ab>},{<ab>},{<ab>},{<ab>}}")
        self.assertEqual((9,8), result)

    def test_group9(self):
        result = parse_string("{{<!!>},{<!!>},{<!!>},{<!!>}}")
        self.assertEqual((9,0), result)

    def test_group10(self):
        result = parse_string("{{<a!>},{<a!>},{<a!>},{<ab>}}")
        self.assertEqual((3,17), result)




if __name__ == '__main__':
    unittest.main()
