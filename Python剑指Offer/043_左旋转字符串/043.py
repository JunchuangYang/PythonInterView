__author__ = 'lenovo'

def solution(str,n):
    if not str:
        return None
    length = len(str)
    n = n%length # 防止n大于字符串length
    return str[n:] + str[:n]

if __name__ == "__main__":
    print(solution('abcderfgh',11))