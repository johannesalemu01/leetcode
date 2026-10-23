class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        
        count_stone_types=Counter(stones)
        count=0
        
        for char in jewels:
            if char in count_stone_types:
                count+=count_stone_types[char]
        return count        

