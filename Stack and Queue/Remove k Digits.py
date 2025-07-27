class Solution(object):
    def removeKdigits(self,a,k):
        n=len(a)
        st=[]
        for i in range(n):
            while st and k>0 and st[-1]>a[i]:
                st.pop()
                k-=1
            st.append(a[i])
        while k>0:
            st.pop()
            k-=1
        s=''.join(st).lstrip('0')
        if s:
            return s
        return '0'
