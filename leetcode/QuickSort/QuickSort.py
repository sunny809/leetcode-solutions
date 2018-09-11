class QuickSort:
    def sort(self, inputArray):
        low = 0;
        hi = len(inputArray) - 1
        return self.partition(inputArray, low, hi)

    def partition(self, array, low, hi):
        i = low
        j = hi + 1
        mid = low
        midVal = array[mid]

        while True:
            print("i val", i)
            print("j val", j)

            # find the value bigger than mid
            while True:
                i = i + 1
                print("array val of i index", array[i])
                if array[i] > midVal:
                    break
                if i == hi:
                    break

            while True:
                j = j - 1
                print("array val of j index", array[j])
                if midVal < array[j]:
                    break
                if low == j:
                    break

            print("array val of j index", array[j])

            if i >= j: break

            array = self.exPos(array, i, j)

        return array

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
