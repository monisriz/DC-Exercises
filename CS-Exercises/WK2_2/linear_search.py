from pprint import pprint as pp

class linearSearch():

    def main(self, array, item):
        for i in range(0,len(array)):
            if array[i] == item:
                return array[i]
        return False

if __name__ == "__main__":
    my_array = range(0, 100)
    main = linearSearch()
    result = main.main(my_array, 0)
    print(result)
