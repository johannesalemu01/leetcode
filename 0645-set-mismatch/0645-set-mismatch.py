class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        
        count=Counter(nums)

        true_sum=0
        actual_sum=0

        result=[]

        for i in range(len(nums)+1):
            true_sum+=i
    #    actual=[1,2,3,4] =10.   
    #    dupl=[1,2,2,4] =9 
    # 10-9 + duplicate

        for key,value in count.items():
            actual_sum+=key*value

        for key,value in count.items():
            if value==2:
                missing=true_sum-actual_sum+key
                result.extend([key,missing])
        return result    


           




