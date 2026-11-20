class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency_s = dict()
        frequency_t = dict()
        for i in range(len(s)):
            frequency_s[s[i]] = frequency_s.get(s[i], 0) + 1
        for i in range(len(t)):
            frequency_t[t[i]] = frequency_t.get(t[i], 0) + 1
        if frequency_s == frequency_t:
            return True
        return False
