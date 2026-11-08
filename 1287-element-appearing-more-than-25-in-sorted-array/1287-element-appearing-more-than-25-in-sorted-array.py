class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        
        n=len(arr)
        
        count=Counter(arr)

        for num,cnt in count.items():

            if cnt/n>0.25:
                return num
                


        