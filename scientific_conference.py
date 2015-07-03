'''
Created on 03-Jul-2015

@author: Venkatesh
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def max_reports_can_attend(intervals):
    intervals.sort(key=lambda x: x[1])
    cnt, last = 0, 0
    for ele in intervals:
        if ele[0] > last:
            cnt += 1
            last = ele[1]
    return cnt


def main():
    n = read_int()
    intervals = [read_int_list() for _ in xrange(n)]
    print max_reports_can_attend(intervals)


if __name__ == '__main__':
    main()
