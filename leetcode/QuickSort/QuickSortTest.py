import unittest;
from leetcode.Util.ArrayUtil import ArrayUtil
from leetcode.QuickSort.QuickSort import QuickSort

# https://leetcode-cn.com/problems/zigzag-conversion/description/

class QuickSortTest(unittest.TestCase):

    def test(self):
        testInput = ArrayUtil.getRandomArray(10, 100)
        print(testInput)
        qs = QuickSort()
        result = qs.sort(testInput)
        print(result)

