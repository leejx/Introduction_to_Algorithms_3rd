#maximum subarray of A[1...n] = max(A[1...n-1], A[i...n-1,n])

def liner_algorithm(A,n):
    index_ending_max = []
    first_to_index_max = []
    first_to_result = []
    ending_result = []
    result = [A[0]]
    for i in range(n):
        # maximum subarray ending at index j
        index_ending_max.append(A[i])
        # maximum subarray from 1 to j
        first_to_index_max.append(A[i])
        #result location ending at i
        ending_result.append([-1,i])
        #result location for each subarray from 1 to j
        # [left, right]
        first_to_result.append([-1,-1])
    for i in range(n):
        if i > 0:
            # update maximum subarray ending at index j
            # A[i...j]
            temp = index_ending_max[i-1] + A[i]
            if temp >= A[i]:
                index_ending_max[i] = temp
                ending_result[i] = [ending_result[i-1][0],i]
            else:
                ending_result[i] = [i,i]
        else:
            #maximum of A[1]
            ending_result[0] = [0,0]

    for i in range (n):
        if i < n-1 :
            temp = index_ending_max[i] + A[i+1]
        new_temp = index_ending_max[i]
        location = ending_result[i]
        if i > 0:
            # maximum subarray from i to j+1
            # A[1...n-1,n]
            if temp > index_ending_max[i]:
                new_temp = temp
                location = ending_result[i+1]
            # find the max between A[1...j] and A[i...j,j+1]
            if result[i-1] > new_temp:
                result.append(result[i-1])
                first_to_index_max[i] = first_to_index_max[i-1]
            else:
                result.append(new_temp)
                first_to_index_max[i] = location
        else:
            first_to_index_max[i] = [0,0]
    #print first_to_index_max

    return [first_to_index_max[n-1],result[n-1]]
if __name__=="__main__":
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print liner_algorithm(A,16)
