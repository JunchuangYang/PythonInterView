__author__ = 'lenovo'

count = 0

def merge_sort(alist):
    length = len(alist)
    if length == 1:
        return alist
    mid = length // 2
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])
    return sort(left,right)

def sort(left,right):
    left_length = len(left)
    right_length = len(right)
    l , r = 0,0
    res = []
    while l<left_length and r<right_length:
        if  left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            global count
            count += left_length-l
            res.append(right[r])
            r += 1
    res+=left[l:]
    res+=right[r:]
    return res

if __name__ == "__main__":
    alist = [1,2,3,4,5,6,7,0]
    print(merge_sort(alist))
    print(count)