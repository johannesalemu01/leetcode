class Solution:
    def canAliceWin(self, n: int) -> bool:

        alice_win=False

        subtract=10

        while n>=subtract:
            n-=subtract
            subtract-=1
            alice_win=not alice_win
            

     
        return alice_win

        

