class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        n_str=str(n)
        product=1
        sum=0
        for i in n_str:
            sum += int(i)
            product *=int(i)

        return product - sum    



