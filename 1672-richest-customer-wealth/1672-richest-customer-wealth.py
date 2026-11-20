class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:

        max_sum=0

        for customer in accounts:
            max_sum=max(max_sum,sum(customer))

        return max_sum    
        