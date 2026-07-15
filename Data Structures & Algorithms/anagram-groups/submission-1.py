class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        seen_maps = {}
        for i in range(len(strs)):
            cur_map = frozenset(self.string_map(strs[i]).items())
            if cur_map in seen_maps:
                result[seen_maps[cur_map]].append(strs[i])
            else:
                seen_maps[cur_map] = len(result)
                result.append([strs[i]])
        return result

    def string_map(self, string):
        s_map = {}
        for i in range(len(string)):
            cur_s = s_map[string[i]] + 1 if string[i] in s_map else 1
            s_map[string[i]] = cur_s
        return s_map