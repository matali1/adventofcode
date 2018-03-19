import unittest

from checksum import checksum,find_evenly_distribute,checksum_evenly_distribute

class MyTestCase(unittest.TestCase):
    def test_checksum1(self):
        matrix = [[5,1,9,5],[7,5,3],[2,4,6,8]]
        result = checksum(matrix)
        self.assertEqual(18, result)

    def test_checksum2(self):
        matrix = [[5,1,9,5],[7,5,3]]
        result = checksum(matrix)
        self.assertEqual(12, result)

    def test_checksum3(self):
        matrix = [[5,1,9,5]]
        result = checksum(matrix)
        self.assertEqual(8, result)

    def test_checksum4(self):
        matrix = [[-1,-1]]
        result = checksum(matrix)
        self.assertEqual(0, result)

    def test_find_evenly_distribute1(self):
        row = [5,9,2,8]
        result = find_evenly_distribute(row)
        self.assertEqual((2,8), result)

    def test_find_evenly_distribute2(self):
        row = [9,4,7,3]
        result = find_evenly_distribute(row)
        self.assertEqual((3,9), result)

    def test_find_evenly_distribute3(self):
        row = [3,8,6,5]
        result = find_evenly_distribute(row)
        self.assertEqual((3,6), result)

    def test_checksum_evenly_distribute1(self):
        matrix = [[5,9,2,8],[9,4,7,3],[3,8,6,5]]
        result = checksum_evenly_distribute(matrix)
        self.assertEqual(9, result)

if __name__ == '__main__':
    unittest.main()
