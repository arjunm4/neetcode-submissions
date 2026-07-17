class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = []
        anagram_map = defaultdict(int)

        for string in strs:
            seen = False
            for anagram in group_anagrams:
                if Counter(string) == anagram_map[anagram[0]]:
                    anagram.append(string)
                    seen = True
                    break
            if not seen:
                group_anagrams.append([string])
                anagram_map[string] = Counter(string)
        
        return group_anagrams