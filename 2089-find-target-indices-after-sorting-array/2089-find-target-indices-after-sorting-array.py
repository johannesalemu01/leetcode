class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        
        nums.sort()
        target_indices=[]

        for i,num in enumerate(nums):
            if num==target:
                target_indices.append(i)

        return target_indices        
