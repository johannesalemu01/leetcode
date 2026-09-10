class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
       i=0
       for value in nums:
         if value !=val:
           nums[i]=value
           i +=1
        #  print(nums)  
       return i   
                
