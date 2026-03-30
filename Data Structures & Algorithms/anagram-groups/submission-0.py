class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_list = []
        output = {}
        for w in strs:
            sort_value = "".join(sorted(w))
            if sort_value not in output:
                output[sort_value] = []
            output[sort_value].append(w)
        return list(output.values())