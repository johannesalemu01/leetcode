class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count_hills=0
        count_valleys=0
        left,right=1,2
        prev=nums[0]
        while right<len(nums):
            # print(f"nums[left]={nums[left]}")
            if right==len(nums):
                break    
            if nums[left]!=nums[right] and nums[left]!=prev:
                
                if prev < nums[left]>nums[right]:
                    count_hills+=1
                    prev= nums[left]
                    left=right
                    right+=1
                elif prev > nums[left]< nums[right]:
                    count_valleys+=1
                    prev= nums[left]
                    left=right
                    right+=1
                else:
                    prev= nums[left]
                    left=right   
                    right+=1
            else:
                if nums[left] == prev:
                    left = right
                right +=1    
                

        # print(count_hills)        
        # print(count_valleys)        
        return count_hills+count_valleys                
                    
