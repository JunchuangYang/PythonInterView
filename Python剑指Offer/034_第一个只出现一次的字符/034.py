__author__ = 'lenovo'

def solution(str):
    dic = {}
    for i in range(len(str)):
        dic[str[i]] = dic.get(str[i],0) +1
    for i in range(len(str)):
        if dic[str[i]] == 1:
            return i
    return -1
if __name__=="__main__":
    print(solution("aaaaaaaaaaaaaaab"))