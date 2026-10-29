class Solution:
    def countBinarySubstrings(self, s: str) -> int:
       
        prev_len=0
        curr_len=1
        total=0
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                curr_len+=1

            else:
                prev_len=curr_len
                curr_len =1    

            if prev_len >=curr_len:
                total+=1

        return total        



                

                    




        # 00110011

        # 0110