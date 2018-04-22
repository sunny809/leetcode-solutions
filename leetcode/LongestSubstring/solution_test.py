import unittest;
from leetcode.LongestSubstring.solution import Solution


# from https://leetcode-cn.com/problems/add-two-numbers/description/

class SolutionTest(unittest.TestCase):



    def test_basic(self):
        input = "abcabcbb"

        so = Solution()
        length = so.lengthOfLongestSubstring(input)
        self.assertEqual(3, length)

    def test_1(self):
        input = "bbbbbb"

        so = Solution()
        length = so.lengthOfLongestSubstring(input)
        self.assertEqual(length, 1)

    def test_2(self):
        input = "pwwkew"

        so = Solution()
        length = so.lengthOfLongestSubstring(input)
        self.assertEqual(length, 3)

    def test_3(self):
        input = "aab"

        so = Solution()
        length = so.lengthOfLongestSubstring(input)
        self.assertEqual(length,2)

    def test_4(self):
        input = "dvdf"

        so = Solution()
        length = so.lengthOfLongestSubstring(input)
        self.assertEqual(3, length)

    def test_5(self):
        input = "jbpnbwwd"

        so = Solution()
        length = so.lengthOfLongestSubstring(input)
        self.assertEqual(4, length)

    def test_6(self):
        input = "bpfbhmipx"
        so = Solution()
        length = so.lengthOfLongestSubstring(input)
        self.assertEquals(7, length)

    