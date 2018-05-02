class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        for outter_index in range(0, len(s)):
            for inner_index in range(0, len(s)):
                print(outter_index + ":" + inner_index)

    def isPalindrome(self, input):
        length = len(input)
        half_length = int(length/2)

        for index in range(0, half_length):
            current_char = input[index]
            revise_char = input[index*2]
            if current_char == revise_char:
                continue
            else:
                return False

        return True