class Solution:
    def twoSum(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for outer_index in range(0, len(nums)):
            for inner_index in range (outer_index+1, len(nums)):
                outer_num = nums[outer_index]
                inner_num = nums[inner_index]
                if outer_num + inner_num == target:
                    return [outer_index, inner_index]

        return [0,0]