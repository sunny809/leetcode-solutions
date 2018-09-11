class QuickSort:

    def slove(self, inputArray):
        low = 0;
        hi = len(inputArray) - 1
        self.sort(inputArray, low, hi)
        return inputArray

    def sort(self, array, low, hi):

        if low >= hi:
            return

        j = self.partition(array, low, hi)

        self.sort(array, low, j - 1)
        self.sort(array, j + 1, hi)

    def partition(self, array, low, hi):
        i = low
        j = hi + 1
        mid = low
        midValue = array[mid]

        while True:
            print(array)
            print("i val", i)
            print("j val", j)

            # find the value bigger than mid
            while True:
                i = i + 1
                print("array val of i index", array[i])
                leftCurrentVal = array[i]
                if leftCurrentVal > midValue or i == hi:
                    break

            while True:
                j = j - 1
                print("array val of j index", array[j])
                rightCurrentVal = array[j]
                if rightCurrentVal < midValue or j == low:
                    break

            if i >= j:
                break

            self.exPos(array, i, j)


        self.exPos(array, low, j)

        return j

    def exPos(self, array, pos1, pos2):
        print('before' + str(array))
        print('exchange pos1 [' + str(pos1) + ']pos2[' + str(pos2) + ']')
        posVal1 = array[pos1]
        posVal2 = array[pos2]
        array[pos1] = posVal2
        array[pos2] = posVal1
        print('after' + str(array))
        return array

    def incr(self, num):
        num = num + 1
        return num

    def decr(self, num):
        num = num - 1
        return num
