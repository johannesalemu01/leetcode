class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum=0
        prod=1
        final_sum=0

        str_n=str(n)

        for i in str_n:
            digit_sum+=int(i)
            prod*=int(i)

        final_sum=digit_sum+prod    


        if n%final_sum==0:
            return True 

        return False        

