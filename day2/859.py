"""
给定两个由小写字母构成的字符串 A 和 B ，
只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，
就返回 true ；否则返回 false 。
示例 1：

输入： A = "ab", B = "ba"
输出： true
示例 2：

输入： A = "ab", B = "ab"
输出： false
示例 3:

输入： A = "aa", B = "aa"
输出： true
示例 4：

输入： A = "aaaaaaabc", B = "aaaaaaacb"
输出： true
示例 5：

输入： A = "", B = "aa"
输出： false
 

提示：

0 <= A.length <= 20000
0 <= B.length <= 20000
A 和 B 仅由小写字母构成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/buddy-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
思路：
1. 字符串长度不相等, 直接返回false
2. 字符串相等的时候, 只要有重复的元素就返回true
3. A, B字符串有不相等的两个地方, 需要查看它们交换后是否相等即可.
"""

def buddyStrings(A, B):
    if len(A) != len(B):
        return False
    if A == B and len(set(A)) < len(A):
        return True
    dif = [(a,b) for a,b in zip(A, B) if a!=b]
    return len(dif) == 2 and dif[0] == dif[1][::-1]
        

A = input("输入A:")
B = input("输入B:")
print(buddyStrings(A, B))