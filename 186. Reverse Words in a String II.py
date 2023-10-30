class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        str_list = ''.join(s).split(' ')
        str_list.reverse()
        ans = ' '.join(str_list)
        s[:] = list(ans)



# in place 逆序字符串
#字符串处理, 最后深度复制给str.
# Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]