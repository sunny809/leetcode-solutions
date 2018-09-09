import unittest;
from leetcode.ZigZag.solution import Solution

# https://leetcode-cn.com/problems/zigzag-conversion/description/

class SolutionTest(unittest.TestCase):

    def test_1(self):
        input = 'PAYPALISHIRING'
        solution = Solution()
        result = solution.convert(input , 3)
        self.assertEqual("PAHNAPLSIIGYIR",result)

    def test_2(self):
        input = 'PAYPALISHIRING'
        solution = Solution()
        result = solution.convert(input, 4);
        self.assertEqual("PINALSIGYAHRPI", result)

    def test_arrayToStr(self):
        input = [['1','2','3','4'],['5','6','7','8'],['9','10','11','12'],['13','14','15','16']]
        solution = Solution();
        result = solution.arrayToStr(input)
        print(result)

    def test_transfer(self):
        input = [['1','2','3','4'],['5','6','7','8'],['9','10','11','12']]
        solution = Solution();
        result = solution.transfer(input)
        print(result)
# if __name__ == '__main__':
#     unittest.main()