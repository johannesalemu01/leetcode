class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        actualSum=0
        sum=0
        for i in range(0,n+1):
            actualSum+=i

        for i in nums:
            sum+=i

        return actualSum-sum    