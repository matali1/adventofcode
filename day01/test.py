import unittest

from captcha import captcha, reduce, captcha_halway, reduce_halfway

class MyTestCase(unittest.TestCase):

    def test_captcha1(self):
        result = captcha("1122")
        self.assertEqual(3, result)

    def test_captcha2(self):
        result = captcha("1111")
        self.assertEqual(4, result)

    def test_captcha3(self):
        result = captcha("1234")
        self.assertEqual(0, result)

    def test_captcha5(self):
        result = captcha("1234xx")
        self.assertEqual(0, result)

    def test_captcha4(self):
        result = captcha("91212129")
        self.assertEqual(9, result)

    def test_captcha6(self):
        result = captcha("11221")
        self.assertEqual(4, result)

    def test_captcha7(self):
        result = captcha("111")
        self.assertEqual(3, result)

    def test_reduce1(self):
        result = reduce("1122")
        self.assertEqual("12", result)

    def test_reduce2(self):
        result = reduce("1111")
        self.assertEqual("1111", result)

    def test_reduce3(self):
        result = reduce("1234")
        self.assertEqual("", result)

    def test_reduce5(self):
        result = reduce("1234xx")
        self.assertEqual("x", result)

    def test_reduce4(self):
        result = reduce("91212129")
        self.assertEqual("9", result)

    def test_reduce5(self):
        result = reduce("11221")
        self.assertEqual("112", result)

    def test_reduce4(self):
        result = reduce("111")
        self.assertEqual("111", result)

    def test_hf_reduce1(self):
        result = reduce_halfway("1212")
        self.assertEqual("1212", result)

    def test_hf_reduce2(self):
        result = reduce_halfway("1221")
        self.assertEqual("", result)

    def test_hf_reduce3(self):
        result = reduce_halfway("123425")
        self.assertEqual("22", result)

    def test_hf_reduce4(self):
        result = reduce_halfway("123123")
        self.assertEqual("123123", result)

    def test_hf_reduce5(self):
        result = reduce_halfway("12131415")
        self.assertEqual("1111", result)

    def test_hf_captcha1(self):
        result = captcha_halway("1212")
        self.assertEqual(6, result)

    def test_hf_captcha2(self):
        result = captcha_halway("1221")
        self.assertEqual(0, result)

    def test_hf_captcha3(self):
        result = captcha_halway("123425")
        self.assertEqual(4, result)

    def test_hf_captcha4(self):
        result = captcha_halway("123123")
        self.assertEqual(12, result)

    def test_hf_captcha5(self):
        result = captcha_halway("12131415")
        self.assertEqual(4, result)


if __name__ == '__main__':
    unittest.main()
