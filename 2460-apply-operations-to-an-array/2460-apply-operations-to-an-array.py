class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        
        result=[0]*len(nums)
        left=0
        right=1
        insert_index=0

        while right<len(nums) :
            if nums[left]==nums[right]:
                nums[left]=nums[left]*2
                nums[right]=0
            left+=1
            right+=1    

        for num in nums:
            if num!=0:
                result[insert_index]=num
                insert_index+=1

        return result            



