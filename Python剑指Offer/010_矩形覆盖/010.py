__author__ = 'lenovo'

def rectCover(num):
    if num == 1:
        return 1
    if num == 2:
        return 2
    return rectCover(num-1) + (num-2)

if __name__ == '__main__':
    print(rectCover(3))
    print(rectCover(4))
    print(rectCover(5))