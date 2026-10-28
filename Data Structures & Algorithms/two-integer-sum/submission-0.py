class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}
        for i, n in enumerate(nums):
            t_num = target - n
            if t_num in tracker:
                return [tracker[t_num], i]
            tracker[n] = i