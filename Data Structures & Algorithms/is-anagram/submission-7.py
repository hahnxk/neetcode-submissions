class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths don't match, return False
        if len(s) != len(t):
            return False
        # Create two dictionaries for both strings
        countS, countT = {}, {}
        # Loop through strings to add (char, count) pairs to dictionaries
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        # Check if the dictionaries match
        for c in countS:
            # countT.get(c, 0) to ensure program doesn't crash in case char c does not exist
            if countS[c] != countT.get(c, 0):
                return False

        return True