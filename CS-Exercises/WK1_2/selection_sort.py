from pprint import pprint as pp
class selection_sort():

    def main(self, my_array):
        length = len(my_array)
        # Loop through the whole array
        for i in range(length):
            # Set min_index to current element
            min_index = i
            # Loop through the array, but start at i + 1.
            # Elements before i + 1 are sorted already
            for x in range(i + 1, length):
                # Update min_index if we found a smaller number
                if my_array[min_index] > my_array[x]:
                    min_index = x
            # if our smallest number isnt the current number, swap
            if i != min_index:
                temp = my_array[i]
                my_array[i] = my_array[min_index]
                my_array[min_index] = temp
        return my_array

if __name__ == "__main__":
    my_array = [9, 4, 2, 6, 1, 0, 3, 5]
    main = selection_sort()
    result = main.main(my_array)
    print(result)
