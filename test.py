# -*- coding: utf-8 -*-

import time

TIMES = 100000000

def calc(times):
    for i in xrange(times):
        a = 1
        b = 2
        c = a + b

        d = 3
        e = 4
        f = e - d

        g = 5
        h = 6
        j = g * h

        k = 1
        l = 3
        m = l / k

        # print c, f, j, m

if __name__ == '__main__':
    start = time.time()
    calc(TIMES)
    stop = time.time()
    print '%.6f'%(stop - start)
