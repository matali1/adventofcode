import unittest

from knothash import knot_hash,result_produce,dense_hash,hex_signature


class MyTestCase(unittest.TestCase):
    #
    # def test_hash1(self):
    #     circular_list = [0, 1, 2, 3, 4]
    #     hash = [3,4,1,5]
    #     new_list,a,b = knot_hash(circular_list,hash)
    #     self.assertEqual(12, result_produce(new_list))
    # #
    # def test_hash2(self):
    #     circular_list = [0, 1, 2, 3, 4]
    #     hash = [3,4,1,5]
    #     result = knot_hash(circular_list,hash)
    #     self.assertEqual(0, result)
    #
    # def test_hash3(self):
    #     circular_list = [0, 1, 2, 3, 4]
    #     hash = [3,4,1,5]
    #     result = knot_hash(circular_list,hash)
    #     self.assertEqual(0, result)
    #
    def test_dense_has(self):
        lst =[65 , 27 , 9 , 1 , 4 , 3 , 40 , 50 , 91 , 7 , 6 , 0 , 2 , 5 , 68 , 22]
        result = dense_hash(lst)
        self.assertEqual([64],result)

    def test_dense_hash(self):
        lst =[65 , 27 , 9 , 1 , 4 , 3 , 40 , 50 , 91 , 7 , 6 , 0 , 2 , 5 , 68 , 22,65 , 27 , 9 , 1 , 4 , 3 , 40 , 50 , 91 , 7 , 6 , 0 , 2 , 5 , 68 , 22]
        result = dense_hash(lst)
        self.assertEqual([64,64],result)

    def test_signagure(self):
        result = hex_signature([64, 7, 255])
        self.assertEqual('4007ff',result)

if __name__ == '__main__':
    unittest.main()
