__author__ = 'lenovo'

def solution(num):
    n = num // 2
    start = end = 0
    res = []
    while start<n and end < n:
        total = (end + start)*(end - start + 1)/2
        if total == num:
            r = []
            for i in range(start,end+1):
                r.append(i)
            res.append(r[:])
            end += 1
        elif total < num:
            end += 1
        elif total > num:
            start += 1
    return res

if __name__ == "__main__":
    print(solution(100))