__author__ = 'lenovo'

class Solution(object):
    @staticmethod
    def check_num(nums,str):
        n = 0
        for i in str:
            if i == nums:
                n+=1
        if n*2 <= len(str):
            return 0
        return nums


    @staticmethod
    def solution1(str):
        def partition(str,start,end):
            pivot = str[start]

            while start<end:
                while start<end and pivot<=str[end]:
                    end -= 1
                str[start] = str[end]

                while start<end and str[start]<=pivot:
                    start += 1
                str[end] = str[start]
            str[start] = pivot
            return start

        def helper(str,start,end):
            length = len(str)
            index = partition(str,start,end)
            if index == (length>>1):
                return str[index]
            elif index<(length>>1):
                return helper(str,index+1,end)
            else:
                return helper(str,start,index-1)
        # 获取到中位数
        num = helper(str,0,len(str)-1)
        # 判断中位数是否超过数组长度一半
        print(Solution.check_num(num,str))

    @staticmethod
    def solution2(str):
        res = None
        sum = 0
        for i in str:
            if sum == 0:
                res = i
                sum += 1
            elif res == i:
                sum += 1
            else:
                sum -= 1

        print(Solution.check_num(res,str))
if __name__ == "__main__":
    Solution.solution1([1, 2, 3,3,3,3])
    Solution.solution2([1, 2, 3,3,3,3])