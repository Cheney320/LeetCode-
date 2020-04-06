"""
无重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合，字符串每个字符均不相同。

示例1:

 输入：S = "qwe"
 输出：["qwe", "qew", "wqe", "weq", "ewq", "eqw"]
示例2:

 输入：S = "ab"
 输出：["ab", "ba"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-i-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def permutation(self, S):
        if not S: return []
        res = []
        path = ''
        self.__backtrack(S, path, res)
        return res

    def __backtrack(self, S, path, res):
        if S == '':
            res.append(path)
            return 
        for i in range(len(S)):
            cur = S[i]
            self.__backtrack(S[:i]+S[i+1:], path+cur, res)


if __name__ == "__main__":
    S = "qwe"
    s = Solution()
    print(s.permutation(S))