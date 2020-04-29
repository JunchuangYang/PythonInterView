__author__ = 'lenovo'

def solution(n):

    res = [1]
    # 三个指针，分别求当前丑数乘以2,3,5的结果
    index2 ,index3 , index5 = 0, 0, 0
    for _ in range(1,n):
        curnum = min(res[index2]*2,min(res[index3]*3,res[index5]*5))
        res.append(curnum)
        if curnum == res[index2]*2:
            index2 += 1

        if curnum == res[index3]*3:
            index3 += 1

        if curnum == res[index5]*5:
            index5 += 1
    return res[-1]

if __name__ == "__main__":
    print(solution(1500))