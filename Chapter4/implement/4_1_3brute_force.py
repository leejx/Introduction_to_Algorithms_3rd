
import doctest
#二维数组，需要一个一个赋值，初始化只能分配一个1＊N的数组，每个元素是列表，需要再对每个列表分配空间
def brute_force(A, n):
    """
    >>> A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    >>> n=16
    >>> brute_force(A,n)
    [43, 7, 10]
    """
    result = []
    sum_list = [[] for i in range(n)]
    max_value = 0
    low = 0
    high = 0
    for i in range(n):
        for j in range(0, n):
            if j <= i :
                sum_list[i].append(A[i])
            else:
                temp = int(sum_list[i][j-1]) + int(A[j])
                sum_list[i].append(temp)
                #print "(%d,%d)=%d +%d =%d, temp=%d" %(i,j,sum_list[i][j-1],A[j],sum_list[i][j],temp)
    for i in range(n):
        for j in range(i, n):
            if sum_list[i][j] > max_value:
                max_value = sum_list[i][j]
                low = i
                high = j
    result = [max_value, low, high]
    return result



# if __name__ == '__main__' :
#     doctest.testmod(verbose=True)
