class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        result=[]

        for num in nums:
            result.append(num)

        nums.extend(result)

        return nums   

