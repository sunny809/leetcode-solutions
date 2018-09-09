class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        returnResult = ''

        length = len(s)
        print('input:'+s)
        print(length)

        resultMatrix = []

        for index in range(len(s)):
            innerArray = []

            idx = index % numRows

            if index == 0 or idx == numRows - 1 :
                for innerIndex in range(index, index + numRows):
                    innerArray.append(s[innerIndex])
                print(innerArray)
                resultMatrix.append(innerArray)
            else:
                for innerIndex in range(0, numRows):
                    if idx == innerIndex:
                        innerArray.append(s[innerIndex])
                    else:
                        innerArray.append("")

                index += 1

                resultMatrix.append(innerArray)

        print(resultMatrix)

    def arrayToStr(self, inputArray):
        result = ""
        for outterIndex in range(len(inputArray)):
            innerArray = inputArray[outterIndex]
            for innderIndex in range(len(innerArray)):
                result = result + innerArray[innderIndex]

        return result

    def transfer(self, inputArray):
        print(inputArray)

        colNum = len(inputArray)
        rowNum = len(inputArray[0])

        # init the result array
        result = [[0 for col in range(colNum)] for row in range(rowNum)]

        for outterIndex in range(0, len(inputArray)):
            for innerIndex in range(0, len(inputArray[outterIndex])):
                result[innerIndex][outterIndex] = inputArray[outterIndex][innerIndex]

        print(result)
