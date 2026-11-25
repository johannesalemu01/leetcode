class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        freq=Counter(nums)

        answer=[]
        
        temp = sorted(freq.values(), reverse=True)

        freq_value=temp[0:k]

        for val,count in freq.items():
            if count in freq_value:
                answer.append(val)
            
        

        return answer
        