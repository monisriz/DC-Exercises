# Algorithm 1   FizzBuzz
# Conditions:
# a. If a number is a multiple of 3 AND 5, print FizzBuzz.
# b. If a number is a multiple of 3, print Fizz.
# c. If a number is a multiple of 5, print Buzz.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0 and i % 5 != 0:
            print("Fizz")
    elif i % 5 == 0 and i % 3 != 0:
            print("Buzz")
    else:
        print(i)
