class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        ana=defaultdict(list)
        key=""
        result=[]
        for word in strs:
            key=''.join(sorted(word))
            ana[key].append(word)
        # print(ana)
        for values in ana.values():
            result.append(values)

        return result    
            

