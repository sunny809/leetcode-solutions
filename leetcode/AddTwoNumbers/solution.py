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

        result_num = self.getNumberFromList(list1) + self.getNumberFromList(list2)
        return self.get_list_from_number(result_num);

    def getNumberFromList(self, input_list):
        result_num = 0

        for num_index in range(0, len(input_list)):
            num_index = len(input_list) - (num_index + 1)
            num = input_list[num_index]
            result_num = result_num + (num * (10 ** num_index))
            # print (result_num)

        # result_num_list = self.get_list_from_number(result_num)

        return result_num

    def get_list_from_list_node(self, ln):
        result = []

        while ln is not None:
            result.append(ln.val)
            ln = ln.next

        # print(result)
        # result.reverse()
        # print (result)
        return result

    def get_list_from_number(self, input_num):
        result = []

        num_str = str(input_num)

        for num_index in range(0, len(num_str)):
            current = num_str[num_index: num_index + 1]
            result.append(current)

        result.reverse()
        return self.gen_list_node(result)

    def gen_list_node(self, input_array):

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
