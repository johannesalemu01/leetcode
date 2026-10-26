class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:

        target=[]

        for i,num in enumerate(nums):
            target.insert(index[i],num)

        return target    
           
