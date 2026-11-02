class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        
        s1_list=s1.split(" ")
        s2_list=s2.split(" ")

        s1_count=Counter(s1_list)
        s2_count=Counter(s2_list)


        result=[]
        for word in s2_count:
            if word not in s1_count and s2_count[word]==1:
                result.append(word)

        for word in s1_count:

            if word not in s2_count and s1_count[word]==1 :
                result.append(word)

        return result        


