__author__ = 'lenovo'

def solution(A):
    length = len(A)
    B = [1] * length
    for i in range(2,length):
        B[i] = B[i-1] * A[i-1]

    temp = 1
    for i in range(length-2,0,-1):
        temp *= A[i+1]
        B[i] *= temp
    return B
