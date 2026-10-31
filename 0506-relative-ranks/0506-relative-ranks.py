class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        new_score=sorted(score)
        rank={}
        result=[]


        for i,scr in enumerate(new_score[::-1]):
            if i==0:
                rank[scr]="Gold Medal"  
            elif i==1:    
                rank[scr]="Silver Medal" 
            elif i==2:    
                rank[scr]="Bronze Medal"

            else:
                rank[scr]=str(i+1)  


        for scr in score:
            result.append(rank[scr])

        return result    



        return rank        

        