class Solution:
    palindrome_set = set()

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        for left in range(0, len(s)):
            for right in range(len(s), -1, -1):
                current_str = s[left:right]
                if len(current_str) <= len(result) or left >= right:
                    break;

                if self.isPalindromeNew(current_str):
                    result = current_str

        return result

    def isPalindrome(self, input):
        if input in self.palindrome_set:
            return True
        length = len(input)
        start_char = input[0:1]
        end_char = input[length - 1:length]
        if start_char == end_char:
            if length <= 3:
                self.palindrome_set.add(input)
                return True
            else:
                status = self.isPalindrome(input[1:length - 1])
                if status:
                    self.palindrome_set.add(input)
                    return True
                else:
                    return False
        else:
            return False

    def isPalindromeNew(self, input):

        if input in self.palindrome_set:
            return True
        fullLenght = len(input)

        is_odd = fullLenght % 2 == 1

        left = right = 0

        if (is_odd):
            left = int(fullLenght / 2) - 1
            right = int(fullLenght / 2) + 1
        else:
            # even
            left = int(fullLenght / 2)
            right = int(fullLenght / 2) + 1

        while left > 0 and right < fullLenght:
            leftChar = input[left: left+1]
            rightChar = input[right: right + 1]
            if leftChar == rightChar:
                self.palindrome_set.add(input[left:right])
            elif left != 0 and right != len(fullLenght):
                return False
            else:
                return True

            left-=1
            right+=1