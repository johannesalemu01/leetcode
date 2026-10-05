class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        isomor={}

        pair_of_char=list(zip(s,t))
        
        for first,second in pair_of_char:
            if first in isomor:
                if isomor[first]!=second:
                    return False
            else:
                if second in isomor.values():
                    return False
                            
            isomor[first] = second


        return True        




            
