class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # max array is 1000 and max k is also 1000
        all=set(range(1,2002))
        given=set(arr)
        missing=list(all - given)
        return missing[k-1]
        
