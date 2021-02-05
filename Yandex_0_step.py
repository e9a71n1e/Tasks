# input candy names:

sweets = [candy for candy in input("Enter space-separated candy names (without quotes): ").split()] 

from functools import reduce
from math import gcd  # greatest common divisor

# we need group by candy names and get greatest common divisor to get a maximum number of friends
# reduce here is just for pairwise computation of gcd

print(reduce(gcd, [sweets.count(x) for x in set(sweets)]))
