from pprint import pprint as pp
class insertion_sort():

    def main(self, my_array):
        length = len(my_array)
        for i in range(length):
            # Keep track of current element
            temp = my_array[i]
            x = i - 1
            # Loop down the array until we hit the end, or a number that is bigger than temp
            while x >= 0 and my_array[x] > temp:
                # Move element up 1 position
                my_array[x + 1] = my_array[x]
                x = x - 1

            my_array[x + 1 ] = temp
        return my_array

if __name__ == "__main__":
    my_array = [9, 4, 2, 6, 1, 0, 3, 5]
    main = insertion_sort()
    result = main.main(my_array)
    print(result)
