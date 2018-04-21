import unittest;
from leetcode.AddTwoNumbers.solution import Solution
from leetcode.AddTwoNumbers.solution import ListNode

# from https://leetcode-cn.com/problems/add-two-numbers/description/

class SolutionTest(unittest.TestCase):

    def genListNode(self, input_array):

        before_node = None
        first_node = None

        for index in range(0, len(input_array)):
            print(input_array[index])
            current_node = ListNode(input_array[index])

            if before_node is None:
                first_node = current_node
            else:
                before_node.next = current_node
            before_node = current_node

        return first_node


    def test_basic(self):
        l1 = [2,3,4]
        result_list_node = self.genListNode(l1)
        print (result_list_node)

        while result_list_node is not None:
            print(result_list_node.val)
            result_list_node = result_list_node.next

    def test_num_to_list(self):
        so = Solution()
        result = so.get_list_from_number(123)
        print(result)



    def test_simple(self):
        ln1 = self.genListNode([2,4,3])
        # 342
        ln2 = self.genListNode([5,6,4])
        # 465
        solution = Solution()
        result = solution.addTwoNumbers(ln1,ln2)
        # 342 + 465 = 807
        self.assertEqual(807,result)

    def test_1(self):
        ln1 = self.genListNode( [1,2,3])
        # 321
        ln2 = self.genListNode([3,4,5])
        # 543
        solution = Solution()
        result = solution.addTwoNumbers(ln1,ln2)
        # 321 + 543 = 864
        self.assertEqual(864,result)

    def test_2(self):
        ln1 = self.genListNode([7,0,0])
        # 7
        ln2 = self.genListNode([8,0,0])
        # 8
        solution = Solution()
        result = solution.addTwoNumbers(ln1,ln2)
        # 7 + 8 = 15
        self.assertEqual(15,result)


    def test_3(self):
        ln1 = self.genListNode([2,4,3])
        # 342
        ln2 = self.genListNode([5,6,4])
        # 465
        std = self.genListNode([7,0,8])
        solution = Solution()

        result = solution.addTwoNumbers(ln1,ln2)
        #
        print(result)
        self.assertEqual(std,result)
    # def test_1(self):
    #     self.data = [15,11,7,2]
    #     solution = Solution()
    #     result = solution.twoSum(self.data, 9)
    #     self.assertEqual([2,3],result)

    # def test_2(self):
    #     self.data = [4,4]
    #     solution = Solution()
    #     result = solution.twoSum(self.data, 8)
    #     self.assertEqual([0,1],result)
    #
    # def test_3(self):
    #     self.data = [0,4,3,0]
    #     # self.data.reverse()
    #     solution = Solution()
    #     result = solution.twoSum(self.data, 0)
    #     self.assertEqual([0,3],result)
    #
    # def test_4(self):
    #     self.data = [-3,4,3,90]
    #     # self.data.reverse()
    #     solution = Solution()
    #     result = solution.twoSum(self.data, 0)
    #     self.assertEqual([0,2],result)
