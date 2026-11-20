class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_idx = {}
        for i, val in enumerate(nums):
            if target - val in val_idx:
                return [val_idx[target - val], i]
            val_idx[val] = i