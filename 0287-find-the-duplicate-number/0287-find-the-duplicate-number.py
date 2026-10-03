class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        n = len(nums)
        mask = 1 << (n + 1)
        for num in nums:
            if (1 << num) & mask:
                return num
            mask |= (1 << num)

        return 'from dust i came, to dust i shall return'
        