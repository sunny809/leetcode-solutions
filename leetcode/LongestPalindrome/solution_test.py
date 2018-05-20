import unittest;

from leetcode.LongestPalindrome.solution import Solution


# from https://leetcode-cn.com/problems/add-two-numbers/description/

class SolutionTest(unittest.TestCase):



    def test_basic(self):
        input = "babad"

        so = Solution()
        result = so.longestPalindrome(input)
        self.assertEqual("bab", result )

    def test_the_basic(self):
        input = "abcba"

        so = Solution()
        result = so.isPalindrome(input)
        self.assertEqual(True, result)
