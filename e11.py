
import time
from string_literals import e11_raw_grid_string

def e11():
    num_lines = e11_raw_grid_string.strip().split("\n")
    numbers = []
    for l in num_lines:
        numbers.append( [ int(s) for s in l.strip().split(' ')])

    square_side, adjacency_length, max_prod = 20, 4, 0
    for i in xrange(square_side):
        for j in xrange(square_side):
            downProduct, rightProduct, rDiagProduct, lDiagProduct = 1, 1, 1, 1
            for k in xrange( adjacency_length ):
                if j + k < square_side:
                    rightProduct *= numbers[i][j+k]
                if i + k < square_side:
                    downProduct *= numbers[i+k][j]
                if i + k < square_side and j + k < square_side:
                    rDiagProduct *= numbers[i+k][j+k]
                if i + k < square_side and j - k >= 0:
                    lDiagProduct *= numbers[i+k][j-k]
                            
            max_prod = max( max_prod, rightProduct, downProduct, rDiagProduct, lDiagProduct )
    return max_prod

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 11 solution is:", e11()
    end = time.time()
    print "elapsed time is %.4f milliseconds" % (1000 * (end-start))
                            
                            
                            
                        
