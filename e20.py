        
import time

factorial = lambda n: reduce( lambda x, y: x*y, [1]+range(1, n+1))

def e20():
    return sum(int(c) for c in str(factorial(100)))

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 20 solution is:",  e20()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
