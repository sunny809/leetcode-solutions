class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result_str = ""
        for startIndex in range(0, len(s)):
            for innerIndex in range(startIndex + 1, len(s) + 1):
                current_str = s[startIndex:innerIndex]
                if self.isPalindrome(current_str):
                    if len(current_str) > len(result_str):
                        result_str = current_str
        return result_str

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