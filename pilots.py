'''
Created on 03-Jul-2015

@author: Venkatesh

MPILOT - Pilots
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return(raw_input())


def min_amount(slry_lst):
    first_ele = slry_lst.pop(0)
    temp = [(x[0], idx) for idx, x in enumerate(slry_lst)]
    temp.sort()
    slry_lst.insert(0, first_ele)
    total = 0
    for i in xrange(len(temp)):
        total += slry_lst.pop()[1]
        total += slry_lst.pop(temp[i][1])


def main():
    n = read_int()
    slry = [read_int_list() for _ in xrange(n)]
    print min_amount(slry)


if __name__ == '__main__':
    main()
