from pprint import pprint as pp

class binarySearch():

    # def binary_search_recursion(self, array, item):
    #     if len(array) == 0:
    #         return False
    #     else:
    #         midpoint = len(array)//2
    #         print("1midpoint is array[%s] = %s" % (midpoint,array[midpoint]))
    #         if array[midpoint]==item:
    #             # print("FOUND")
    #             return midpoint
    #         else:
    #             if item<array[midpoint]:
    #                 return self.binary_search_recursion(array[:midpoint],item)
    #             else:
    #                 return self.binary_search_recursion(array[midpoint+1:],item)
    def binary_search_recursion(self, array, element, mini=0, maxi=None):
      """recursive binary search."""

      maxi = len(array) - 1 if maxi is None else maxi

      if mini == maxi:
        return array[mini] == element
      else:
        median = (maxi + mini)//2
        if array[median] == element:
          return median
        elif array[median] > element:
          return self.binary_search_recursion(array, element, mini, median)
        else:
          return self.binary_search_recursion(array, element, median+1, maxi)

if __name__ == "__main__":
    my_array = range(10, 100)
    main = binarySearch()
    result = main.binary_search_recursion(my_array, 10)
    print(result)
