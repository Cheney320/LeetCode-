#
# @lc app=leetcode.cn id=784 lang=python3
#
# [784] 字母大小写全排列
#

# @lc code=start
class Solution:
    def letterCasePermutation(self, S):
        if not S: return []
        size = len(S)
        arr = list(S)
        res = []
        self.__dfs(arr, size, 0, res)
        return res

    def __dfs(self, arr, size, start, res):
        if start == size:
            res.append(''.join(arr))
            return
        self.__dfs(arr, size, start+1, res)
        # 如果是字母就变换大小写
        if arr[start].isalpha():
            arr[start] = chr(ord(arr[start])^(1<<5))
            self.__dfs(arr, size, start+1, res)
        
# @lc code=end

