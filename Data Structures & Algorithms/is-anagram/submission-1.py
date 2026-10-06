class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        freq1=dict(Counter(s))
        freq2=dict(Counter(t))
        if freq1==freq2:
            return True
        return False
        