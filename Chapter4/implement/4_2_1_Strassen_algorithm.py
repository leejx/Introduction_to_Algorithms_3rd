from numpy import *
def Strassen(A,B):
    n = A.shape[1]
    n_half = n/2
    C_11 = C_12 = C_22 = C_21 = mat(zeros((n_half,n_half)))
    if n == 1:
        c = A[0,0] * B[0,0]
        return c
    else:

        B_11 = B[0:n_half,0:n_half]
        B_12 = B[0:n_half,n_half:n]
        B_21 = B[n_half:n,0:n_half]
        B_22 = B[n_half:n,n_half:n]
        A_11 = A[0:n_half,0:n_half]
        A_12 = A[0:n_half,n_half:n]
        A_21 = A[n_half:n,0:n_half]
        A_22 = A[n_half:n,n_half:n]

        S_1 = B_12 - B_22
        S_2 = A_11 + A_12
        S_3 = A_21 + A_22
        S_4 = B_21 - B_11
        S_5 = A_11 + A_22
        S_6 = B_11 + B_22
        S_7 = A_12 - A_22
        S_8 = B_21 + B_22
        S_9 = A_11 - A_21
        S_10 = B_11 + B_12

        P_1 = Strassen(A_11, S_1)
        P_2 = Strassen(S_2, B_22)
        P_3 = Strassen(S_3, B_11)
        P_4 = Strassen(A_22, S_4)
        P_5 = Strassen(S_5, S_6)
        P_6 = Strassen(S_7, S_8)
        P_7 = Strassen(S_9, S_10)

        C_11 = P_5 + P_4 - P_2 + P_6
        C_12 = P_1 + P_2
        C_21 = P_3 + P_4
        C_22 = P_5 + P_1 - P_3 - P_7

    return [[C_11,C_12],[C_21,C_22]]

if __name__=="__main__":
    A=[[1,3],[7,5]]
    B=[[6,8],[4,2]]
    C=[[1,1],[1,1]]
    matrix_a = mat(A)
    matrix_b = mat(B)
    matrix_c = mat(C)
    print Strassen(matrix_a,matrix_b)
