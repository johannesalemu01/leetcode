class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        nums.sort(reverse=True,key=abs)
        sum_add=0
        for i,num in enumerate(nums):
            if i< len(nums)/2:
                sum_add+=num*num
            else:
                sum_add-=num*num  

        return sum_add            

