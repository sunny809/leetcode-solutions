# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list1 = self.get_list_from_list_node(l1)
        list2 = self.get_list_from_list_node(l2)

        return self.getNumberFromList(list1) + self.getNumberFromList(list2);

    def getNumberFromList(self, input_list):
        result_num = 0

        for num_index in range(0, len(input_list)):
            num_index = len(input_list) - (num_index + 1)
            num = input_list[num_index]
            result_num = result_num + (num * (10 ** num_index))

        return result_num

    def get_list_from_list_node(self, ln):
        result = []

        while ln is not None:
            result.append(ln.val)
            ln = ln.next

        result.reverse()
        return result

    def get_list_from_number(self, input_num):

