class Solution:
    def minMoves(self, nums: List[int]) -> int:

        target=max(nums)
        move=0

        for num in nums:
            if target-num!=0:
                move+=target-num

        return move        
            
            
        