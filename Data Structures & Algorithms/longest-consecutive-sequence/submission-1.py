class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_streak = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                j = num
                while j + 1 in nums_set:
                    j += 1
                max_streak = max(max_streak, j - num + 1)
        return max_streak