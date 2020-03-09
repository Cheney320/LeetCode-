#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    # 滑动窗口法
    # def lengthOfLongestSubstring(self, s):
    #     n = len(s)
    #     i, j = 0, 0
    #     length = 0
    #     hashSet = set()
    #     while i < n and j < n:
    #         if s[j] not in hashSet:
    #             hashSet.add(s[j])
    #             j += 1
    #             length = max(length, j-i)
    #         else:
    #             hashSet.remove(s[i])
    #             i += 1
    #     return length

    # 优化的滑动窗口
    # 上述的方法最多需要执行 2n 个步骤。事实上，它可以被进一步优化为仅需要 n 个步骤。我们可以定义字符到索引的映射，而不是使用集合来判断一个字符是否存在。 当我们找到重复的字符时，我们可以立即跳过该窗口。
    # 如果s[j]在[i,j)范围内有与j'重复的字符，我们不需要逐渐增加i。我们可以直接跳过[i,j']范围内的所有元素，并将i变为j'+1。
    def lengthOfLongestSubstring(self, s):
        if len(s) == 1: return 1
        i, j = 0, 0
        length = 0
        n = len(s)
        while i < n and j < n:
            if s[j] in s[i:j]:
                i = i + s[i:j].find(s[j])+1   
            else:
                j += 1
                length = max(length, j-i)

        return length

# @lc code=end


if __name__ == "__main__":
    sol = Solution()
    s = 'aab'
    print(sol.lengthOfLongestSubstring(s))
