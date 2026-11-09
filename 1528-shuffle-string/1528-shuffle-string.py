class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        
        shuffled_list=[0]*len(s)
        for char,index in zip(s,indices):
            print(index)
            shuffled_list[index]=char  

        return "".join(shuffled_list)


