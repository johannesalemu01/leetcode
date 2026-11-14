class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x=""

        n_str=str(n)
        sum_n=0

        for char in n_str:
            if int(char)!=0:
               x= x + char
               sum_n+=int(char)

        if not x:
            x="0"

        x=int(x)

        return x*sum_n


        

     
        