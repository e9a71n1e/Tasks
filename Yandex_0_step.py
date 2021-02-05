# У вас есть список конфет разных типов, вам нужно собрать одинаковые наборы для своих друзей.
# Какому максимальному числу друзей вы сможете собрать наборы так, чтобы раздарить все конфеты.
# Реализуйте функцию на питоне, которая принимает на вход список конфет и отдает максимальное число друзей. Формат входных данных - список строк.

# ТЕСТ: ['a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c'] ОТВЕТ:1
# ТЕСТ: ['a', 'b', 'c', 'a', 'b', 'c', 'c', 'c'] ОТВЕТ:2


# input candy names:

sweets = [candy for candy in input("Enter space-separated candy names (without quotes): ").split()] 

from functools import reduce
from math import gcd  # greatest common divisor

# we need grouping by candy names and get greatest common divisor to get a maximum number of friends
# reduce here is just for pairwise computation of gcd

print(reduce(gcd, [sweets.count(x) for x in set(sweets)]))
