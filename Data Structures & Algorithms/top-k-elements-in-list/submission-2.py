class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        top_2_keys = sorted(counts,key = counts.get, reverse = True)[:k]
        return top_2_keys