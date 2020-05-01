__author__ = 'lenovo'
def get_first_k(alist,k):
    right = len(alist) - 1
    left= 0
    while left <= right:
        mid = (right+left)//2
        if alist[mid] < k:
            left = mid + 1
        elif alist[mid] > k:
            right = mid - 1
        else:
            if mid == 0 or alist[mid-1] != k:
                return mid
            right = mid - 1
    return -1

def get_last_k(alist,k):
    right = len(alist) - 1
    left = 0
    while left <= right:
        mid = (left+right) // 2
        if alist[mid] < k:
            left = mid + 1
        elif alist[mid] > k:
            right = mid - 1
        else:
            if mid == len(alist)-1 or alist[mid+1] != k:
                return mid
            left = mid + 1
    return -1

def solution(alist,k):
    return get_last_k(alist,k) - get_first_k(alist,k) + 1

if __name__ == "__main__":
    print(solution([1,2,3,3,5,5,5,7],2))
