class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = 1 + dic.get(nums[i],0)
        
        sorted_dic = dict(sorted(dic.items(), key=lambda item:item[1], reverse = True))
        return list(sorted_dic.keys())[:k]