class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        s_lst = s.split(' ')
        return len(s_lst[-1])