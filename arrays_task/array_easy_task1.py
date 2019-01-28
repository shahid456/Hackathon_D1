class Solution:
    def sortArrayByParity(self, A):
        result_even=[]
        result_odd=[]
        for x in A:
            if x%2==0:
                result_even.append(x)
            else:
                result_odd.append(x)
        return result_even+result_odd

