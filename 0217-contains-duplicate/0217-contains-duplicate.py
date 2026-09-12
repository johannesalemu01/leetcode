class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:  
        duplicates=set(nums)
        if len(duplicates)!=len(nums):
            return True
        return False    
        
