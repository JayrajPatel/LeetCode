class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSub = nums[0]
        sum = 0

        for i in nums:
            if sum < 0:
                sum = 0
            sum += i
            maxSub = max(maxSub, sum)
        return maxSub