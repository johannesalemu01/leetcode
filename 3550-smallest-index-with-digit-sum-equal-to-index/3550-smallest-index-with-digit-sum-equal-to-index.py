class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
    

      
        for i,num in enumerate(nums):
            sum=0
            for digit in str(num):
                    sum+=int(digit)
            if sum==i:
                return i

        return -1
       

                
     

       