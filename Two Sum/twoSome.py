class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hmap = {}
        
        for i, num in enumerate(nums):
            if target - num in hmap:
                return ([hmap[target - num], i])
            elif num not in hmap:
                hmap[num] = i