class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=int(len(s)/2)
        for i in range(n):
            j=len(s)-1-i
            t=s[j]
            s[j]=s[i]
            s[i]=t
        