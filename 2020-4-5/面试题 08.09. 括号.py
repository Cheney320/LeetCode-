"""
括号。设计一种算法，打印n对括号的所有合法的（例如，开闭一一对应）组合。

说明：解集不能包含重复的子集。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bracket-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def generateParenthesis(self, n):
        res = []
        state = ''
        left, right = n, n   # left和right分别代表(和)剩余的个数
        self.__backtrack(left, right, state, res)
        return res

    def __backtrack(self, left, right, state, res):
        if left > right:
            return
        if right == 0:   # 用完
            res.append(state)

        if left > 0:
            self.__backtrack(left-1, right, state+'(', res)
        if right > 0:
            self.__backtrack(left, right-1, state+')', res)

        
if __name__ == "__main__":
    n = 3
    s = Solution()
    print(s.generateParenthesis(n))
        
        
