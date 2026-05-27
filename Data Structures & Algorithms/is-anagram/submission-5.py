class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_list = [char for char in s]
        t_list = [char for char in t]

        s_list.sort()
        t_list.sort()

        if s_list == t_list:
            return True
        else:
            return False
