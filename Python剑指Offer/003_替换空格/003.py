#__author__ = 'lenovo'
import datetime
import re

ret = re.compile(' ')


def timeti(func):

    def jishi(str):
        start = datetime.datetime.now()
        func(str)
        end = datetime.datetime.now()
        print("run: ", end - start)

    return jishi

@timeti
def rep1(str):
    str =  str.replace(' ','%20')
    print(str)

@timeti
def rep2(str):
    num = 0
    for s in str:
        if s == ' ':
           num += 1
    new_str = [' ']*(len(str)+2*num)

    j = 0
    for i in range(len(str)):
        if str[i] == ' ':
            new_str[j] = '%'
            new_str[j+1] = '2'
            new_str[j+2] = '0'
            j += 3
        else:
            new_str[j] = str[i]
            j += 1
    print(''.join(new_str))

print(rep2("We Are Happy"))