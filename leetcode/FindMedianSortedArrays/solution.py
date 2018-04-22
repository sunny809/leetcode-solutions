class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        sortedList = self.combineSortedList(nums1,nums2)

        length = len(sortedList)

        startId = int(length / 2)

        median = 0

        if length % 2 == 1:
            median = sortedList[startId]
        else:
            median = (sortedList[startId - 1 ] + sortedList[startId]) / 2

        return float(median)

    def combineSortedList(self, num_list1, num_list2):

        if len(num_list1) == 0:
            return num_list2
        elif len(num_list2) == 0:
            return num_list1

        result_list = []
        num1_index = 0
        num2_index = 0


        while num1_index < len(num_list1) or num2_index < len(num_list2):

            num1 = num_list1[num1_index]
            num2 = num_list2[num2_index]

            if num1 < num2:
                result_list.append(num1)
                num1_index += 1
            elif num1 > num2:
                result_list.append(num2)
                num2_index += 1
            else:
                result_list.append(num1)
                result_list.append(num2)
                num1_index += 1
                num2_index += 1

            if num1_index == len(num_list1):
                while num2_index < len(num_list2):
                    result_list.append(num_list2[num2_index])
                    num2_index += 1

            if num2_index == len(num_list2):
                while num1_index < len(num_list1):
                    result_list.append(num_list1[num1_index])
                    num1_index += 1
            # if num2_index >= len(num_list2):


        return result_list
