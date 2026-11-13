class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        counter_inc=1
        counter_dec=1
        result=1

        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                counter_inc+=1
                counter_dec=1         
            elif nums[i]<nums[i-1]:
                counter_dec+=1
                counter_inc=1
            else:
                counter_dec=1
                counter_inc=1

            result=max(result,counter_inc,counter_dec)

        return result        







