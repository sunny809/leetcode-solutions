import random

class ArrayUtil:
    @staticmethod
    def getRandomArray( length, max):

        resultArray = []

        for index in range(length):
            resultArray.append(random.randint(0,max))

        return resultArray