#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            max_sum = max(max_sum, nums[i])
        return max_sum
# @lc code=end



if __name__ == "__main__":
    s = Solution()
    # nums = [-2,1,-3,4,-1,2,1,-5,4]
    nums = [1,2,3,-1,4,5,6]
    print(s.maxSubArray(nums))
