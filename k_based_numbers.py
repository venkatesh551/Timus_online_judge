'''
Created on 29-Jun-2015

@author: Venkatesh
'''

from __future__ import print_function


def read_int():
    return int(raw_input())


def main():
    n = read_int()
    k = read_int()
    result = k
    for _ in xrange(n-1):
        result *= (k - 1)
    print (result * (n-1))

if __name__ == '__main__':
    main()
