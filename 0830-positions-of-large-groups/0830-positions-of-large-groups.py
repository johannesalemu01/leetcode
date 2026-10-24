class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:

        result=[]
        i=0

        while i< len(s):
            k=i

            while k<len(s) and s[i]==s[k]:
                k+=1

            if k-i >=3:
                result.append([i,k-1])   
            i=k
               

        return result        

        