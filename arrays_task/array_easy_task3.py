class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        x=0
        l=len(nums)
        while x<l:
            if nums[x]==val:
                del nums[x]
                l=l-1
                x=x-1
            x+=1
        return len(nums)

A=Solution()
x=A.removeElement([3,3,1,3,2,5],3)
print(x)