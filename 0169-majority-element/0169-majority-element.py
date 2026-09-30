class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        count=(Counter(nums))
        # print(list(count.items()))
        n=len(nums)
        for num,freq in list(count.items()):
            if freq>n/2:
                return num