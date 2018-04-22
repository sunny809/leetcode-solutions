class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        char_list = []

        longest = 0;
        for index in range(0, len(s)):

            current_char = s[index:index + 1]

            if char_list.count(current_char) > 0:
                char_index = char_list.index(current_char)
                char_list = char_list[char_index+1 :]

            char_list.append(current_char)

            if longest < len(char_list):
                longest = len(char_list)


        return longest