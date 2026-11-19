class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        result=[]
        left=0
        right=1
        nums.append(float('inf'))
        while right < len(nums):
            if nums[right-1] + 1 != nums[right]:
                if left == right - 1:
                    result.append(str(nums[left]))
                else:
                    result.append(f'{nums[left]}->{nums[right-1]}')
                left = right
            right += 1

        return result        

     