import random
import unittest;


# from https://leetcode-cn.com/problems/two-sum/description/

class SolutionTest(unittest.TestCase):

    def get_random_array(self, _len, _range):
        result_array = []
        ran = random.Random()

        for index in range(0, _len):
            ran_num = ran.randint(0, _range)
            result_array.append(ran_num)

        return result_array

    def test_simple(self):
        ran_array = self.get_random_array(20, 100)
        print(ran_array)
