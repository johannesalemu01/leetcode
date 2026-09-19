class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        
        squaredNums=[]
        
        pos=len(nums)

        for i,num in enumerate(nums):
            if num>=0:
                pos=i
                # neg=i-1
                break

        neg=pos-1

        while neg >=0 and pos <=len(nums)-1:
            if abs(nums[neg])>=abs(nums[pos]):
                squaredNums.append(abs(nums[pos])**2)
                pos+=1
            else:
                squaredNums.append(abs(nums[neg])**2) 
                neg-=1         

        while neg >=0:
            squaredNums.append(abs(nums[neg])**2)    
            neg-=1

        while pos <=len(nums)-1:
            squaredNums.append(abs(nums[pos])**2)    
            pos+=1 

        return  squaredNums     