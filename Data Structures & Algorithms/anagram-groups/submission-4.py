class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = []
        anagram_map = defaultdict(list)

        for string in strs:
            string_map = [0] * 26
            for char in string:
                string_map[ord(char) - ord("a")] += 1
            anagram_map[tuple(string_map)].append(string)

        for group in anagram_map.values():
            group_anagrams.append(group)

        return group_anagrams