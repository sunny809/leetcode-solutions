import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class Solution:

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        current_length = len(s)
        new_lenght = current_length * 2;

        str_array = self.prepare_str_array(s)

        result = ""

        id = 0
        mx = 0

        for i in range(0, new_lenght):


    def prepare_str_array(self, s):
        current_length = len(s)
        new_lenght = current_length * 2;
        new_s = []
        # new_s.append("$")
        new_s.append("#")
        for index in range(0, current_length):
            new_s.append(s[index:index + 1])
            new_s.append("#")

        return new_s
