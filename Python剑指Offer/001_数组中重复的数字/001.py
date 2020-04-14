#__author__ = 'lenovo'

def duplicate(array):
    n = len(array)
    i = 0
    while i<n:
        if i != array[i]:
            if array[i] != array[array[i]]:
                temp = array[i]
                array[i] = array[array[i]]
                array[temp] = temp
            else:
                return array[i]
        else:
            i += 1
    return False

print(duplicate([2,3,1,1,2,5,3]))