class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = []

        for string in strs:
            seen = False
            for anagram in group_anagrams:
                if Counter(string) == Counter(anagram[0]):
                    anagram.append(string)
                    seen = True
                    break
            if not seen:
                group_anagrams.append([string])
        
        return group_anagrams