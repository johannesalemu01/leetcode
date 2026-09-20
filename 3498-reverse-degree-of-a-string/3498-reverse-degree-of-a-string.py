class Solution:
    def reverseDegree(self, s: str) -> int:
        
        alpha=[]
        # product=1
        sum=0
        for i in range(ord('z'),ord('a')-1,-1):
            alpha.append(chr(i))

        for i,char in enumerate(s):
            i+=1
            product=(alpha.index(char)+1)*i
            sum+=product

        return sum



            
