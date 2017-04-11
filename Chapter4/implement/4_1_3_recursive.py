#import doctest
#left_result = [left, right, sum]
left_result = right_result = current_result = [-1000000,-1000000,-1000000]
def Cross_subarray(A, left, mid, right):
    # """
    # >>> Cross_subarray([-1,11,2,3],0,2,4)
    # [1,3,16]
    # """
    temp_sum = 0
    left_sum = -1000000
    right_sum = -1000000
    max_left = left
    max_right = right
    for i in range(mid, -1, left-1):
        temp_sum = temp_sum + A[i]
        if temp_sum >= left_sum:
            left_sum = temp_sum
            max_left = i
    temp_sum = 0
    for i in range(mid+1, right):
        temp_sum = temp_sum + A[i]
        if temp_sum >= right_sum:
            right_sum = temp_sum
            max_right = i
    return [max_left, max_right, left_sum + right_sum]

def Recursive(A, left, right):
    # """
    # >>> A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    # >>> Recursive(A, 0, 16)
    # [43, 7, 10]
    # """
    if left == right and left < len(A):
        return [left, right, A[left]]
    elif left == len(A):
        return [left, right, A[left-1]]
    else:
        mid = (left + right)/2
        left_result = Recursive(A, left, mid)
        right_result = Recursive(A, mid+1, right)
        current_result = Cross_subarray(A, left, mid, right)
        if left_result[2] >= right_result[2] and left_result[2] >=current_result[2]:
            return[left_result[0],left_result[1],left_result[2]]
        elif right_result[2] >= left_result[2] and right_result[2] >=current_result[2]:
            return[right_result[0], right_result[1], right_result[2]]
        else:
            return[current_result[0], current_result[1], current_result[2]]

    return
if __name__=="__main__":
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print Recursive(A, 0, 16)
