
import doctest

def polynomial_evaluation(a,x):
    """1*1 + 5 * 2 + 3 * 4 + 2 * 8 = 1 + 10 + 12 + 16 = 23 + 16 = 39
    Example
    -------
    >>> polynomial_evaluation('1 5 3 2',2)
    39
    """
    a=a.split()
    _sum = 0
    last_x_i = 1
    for i in xrange(0,len(a)):
        if i != 0:
            x_i = x * last_x_i
        else:
            x_i = last_x_i
        _sum = _sum + int(a[i]) * x_i
        last_x_i = x_i
    return _sum
#
# def main():
#     print polynomial_evaluation('1 5 3 2',2)
#
# 
# if __name__ == '__main__' :
#     doctest.testmod(verbose=True)
