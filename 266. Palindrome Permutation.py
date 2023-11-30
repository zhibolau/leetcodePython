class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """
    def canPermutePalindrome(self, s):
        # write your code here
        lookup={}
        count=0
        for elem in s:
            lookup[elem]=lookup.get(elem, 0)+1
        for val in lookup.values():
            count+=val%2
        return count<=1