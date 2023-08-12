class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pairs = dict()
        for word in strs:
            sorted_str = ''.join(sorted(word))
            pairs[sorted_str] = []
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in pairs:
                pairs[sorted_word].append(word)
                
        out = []
        for key in pairs:
            out.append(pairs[key])
        return out
            
            
        