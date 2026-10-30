class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:

       new_num=sorted(nums)

       return new_num==nums  or new_num==nums[::-1]


            