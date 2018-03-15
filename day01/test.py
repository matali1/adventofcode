import unittest

from captcha import captcha,reduce
class MyTestCase(unittest.TestCase):

    def test_captcha1(self):
        result = captcha("1122")
        self.assertEqual(3,result)


    def test_captcha2(self):
        result = captcha("1111")
        self.assertEqual(1, result)


    def test_captcha3(self):
        result = captcha("1234")
        self.assertEqual(0, result)


    def test_captcha4(self):
        result = captcha("91212129")
        self.assertEqual(9, result)


    def test_reduce1(self):
        result = reduce("1122")
        self.assertEqual("12", result)


    def test_reduce2(self):
        result = reduce("1111")
        self.assertEqual("1", result)


    def test_reduce3(self):
        result = reduce("1234")
        self.assertEqual("", result)


    def test_reduce4(self):
        result = reduce("91212129")
        self.assertEqual("9", result)


if __name__ == '__main__':
    unittest.main()

