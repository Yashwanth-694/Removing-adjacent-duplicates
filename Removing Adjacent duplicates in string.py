class Solution:
    def removeDuplicates(self, s: str) -> str:
        l=[s[0]]
        for i in range(1,len(s)):
            if len(l)==0 or l[len(l)-1]!=s[i]:
                l.append(s[i])
            else:
                l=l[:len(l)-1]
        s=''.join(l)
        return s
s=input('Enter String:')
obj=Solution()
ans=obj.removeDuplicates(s)
print(ans)
        
