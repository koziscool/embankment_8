import time

def e16():
    return sum(int(c) for c in str(2**1000))

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 16 solution is:",  e16()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))