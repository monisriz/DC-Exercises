from pprint import pprint as pp

class binarySearch():

    def binary_search(self, array, item):
        first = 0
        last = len(array)

        while first < last:
            midpoint = (first + last)//2
            # print("2midpoint is array[%s] = %s" % (midpoint,array[midpoint]))
            if array[midpoint] == item:
                return midpoint
            else:
                if item < array[midpoint]:
                    last = midpoint
                else:
                    first = midpoint + 1
        return False

if __name__ == "__main__":
    my_array = range(0, 100)
    main = binarySearch()
    result = main.binary_search(my_array, 0)
    print(result)
