import unittest;
from leetcode.FindMedianSortedArrays.solution import Solution


class SolutionTest(unittest.TestCase):

    def test_sort(self):
        nums1 = [1, 3]
        nums2 = [2]
        so = Solution()
        result = so.combineSortedList(nums1, nums2)
        self.assertEqual([1,2,3],result)

    def test_sort2(self):
        nums1 = [1, 3, 5]
        nums2 = [2,4,6]
        so = Solution()
        result = so.combineSortedList(nums1, nums2)
        self.assertEqual([1,2,3,4,5,6],result)

    def test_sort3(self):
        nums2 = [1, 4]
        nums1 = [3,5,8,9,10]
        so = Solution()
        result = so.combineSortedList(nums1, nums2)
        self.assertEqual([1,3,4,5,8,9,10],result)

    def test_1(self):
        nums1 = [1, 3]
        nums2 = [2]

        so = Solution()
        median = so.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(2.0, median)

    def test_2(self):
        nums1 = [1, 2]
        nums2 = [3, 4]

        so = Solution()
        median = so.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(2.5, median)

    def test_3(self):
        nums1 = []
        nums2 = [1]

        so = Solution()
        median = so.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(1, median)
