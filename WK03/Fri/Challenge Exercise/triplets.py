# Special Pythagorean triplet
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.

def findpytrip(sum):

    for a in range(sum):
        for b in range(sum):
            c = sum - (a + b)
            if a < b and b < c and c**2 == a**2 + b**2:
                print("Pythagorean triplet: ",a,b,c)
                print("Product of a, b, c: ", a*b*c)
findpytrip(200)
