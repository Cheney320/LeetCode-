"""
反转字符串中的单词
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例 1:

输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc" 
注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# def reverseWords(s):
#     return ' '.join([word[::-1] for word in s.split()])


# def reverseWords(s):
#     return ' '.join(s.split()[::-1])[::-1]

# 利用栈的思想:将每一个单词进行入栈再出栈即进行了reverse，初始字符串加上空格，避免最后一个单词不能统一处理。
# 遍历字符串，如果遇到空格则出栈直到栈为空。最后返回字符串索引1以后即可，因为首字符为多余的空格。
def reverseWords(s):
    s += ' '
    stack,new_s = [],''
    for i in s:
        # 入栈
        stack.append(i)
        if i == ' ':
            # 出栈
            while stack:
                new_s += stack.pop()
             
    return new_s[1:]


s = input()
print(reverseWords(s))