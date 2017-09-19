# Exercise 4

import json
import matplotlib.pyplot as plot

def openfile(f):
    with open(f, 'r') as fh:
        data = json.load(fh)

    plot.plot(data['data'])
    plot.show()
filename = input("Enter the file name: ")
openfile(filename)
