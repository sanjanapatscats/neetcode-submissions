class Solution:
    def isValid(self, s: str) -> bool:
        ls=[]
        top=-1
        dic={'{': '}','(': ')','[': ']'}

        for ch in s:
            if ch in dic:
                ls.append(ch)
                top+=1
            else:
                if top>=0:
                    if dic[ls[top]] == ch:
                        top-=1
                        ls.pop()
                    else:
                        return False
                else:
                    return False
        if top==-1:
            return True
        else:
            return False
        