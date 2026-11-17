class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        
        nums_count={}


        nums_sort=sorted(nums)

        output=[]



        for i,num in enumerate(nums_sort):
            if num not in nums_count:
                nums_count[num]=i

        for num in nums:
            output.append(nums_count[num])

        return output    


  

