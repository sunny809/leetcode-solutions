class Solution:
    def sort(self, input_array):

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for start_index in range(0, len(input_array)):
            for end_index in range(1, len(input_array)):
