import unittest;
from leetcode.Util.ArrayUtil import ArrayUtil
from leetcode.QuickSort.QuickSort import  QuickSort

# https://leetcode-cn.com/problems/zigzag-conversion/description/

class ArrayUtilTest(unittest.TestCase):

    def test_1(self):
        result = ArrayUtil.getRandomArray(100, 100)
        print(result)
        self.assertEquals(100, len(result))
