class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        result = []
        # {"1":2 ,"2":3}
        for num in nums:
            if num not in freq_map:
                freq_map[num] = 1
            else:
                freq_map[num] += 1
        sorted_freq_map = sorted(freq_map.items(), key=lambda x:x[1],reverse=True)
        freq_dict = dict(sorted_freq_map)
        list_keys = list(freq_dict.keys())
            
        return list_keys[:k]    
            