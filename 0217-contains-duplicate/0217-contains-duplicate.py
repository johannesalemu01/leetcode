class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:    
        duplicates={}
        for i in nums:
            duplicates[i]=duplicates.get(i,0)+1
        for num,count in duplicates.items():
            if count>1:
                return True
        return False        
        
