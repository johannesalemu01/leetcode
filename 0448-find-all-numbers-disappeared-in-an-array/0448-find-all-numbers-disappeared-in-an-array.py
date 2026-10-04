class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        
        check=set(nums)
        result=[]
        sum=0
        n=len(nums)
        for i in  range(1,n+1):
            if i not in check:
                result.append(i) 

        return result        

           
