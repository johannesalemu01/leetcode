class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left=1
        # right=1
        # while right < len(nums)
        for right in range(1,len(nums)):
            if  nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left += 1
            #   nums.pop(right)

            # else:
            #   left +=1
            #   right +=1
        # print(nums)    
        return left  