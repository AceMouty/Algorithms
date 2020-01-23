#!/usr/bin/python

import sys


"""
111
4
1 3
    v
[0, 1, 2 ,3]
n == 0 
ret 1
n == 1
ret 1

num
arr = [0] * num
[2, 2]
============
1 1 1 1
1 1 2
1 2 1
2 1 1
2 2
1 3
3 1

2
======= 
1 1
2

3
=========
1 1 1
1 2
2 1
3
"""

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    if n == 0:
        return 1
    elif n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         num_cookies = int(sys.argv[1])
#         print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
#             ways=eating_cookies(num_cookies), n=num_cookies))
#     else:
#         print('Usage: eating_cookies.py [num_cookies]')

print(eating_cookies(4))
