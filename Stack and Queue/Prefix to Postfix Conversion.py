class Solution(object):
    def prefixToPostfix(self,s):
        n=len(s)
        st=[]
        for i in range(n-1,-1,-1):
            if s[i].isalnum():
                st.append(s[i])
            else:
                a=st.pop()
                b=st.pop()
                st.append(a+b+s[i])
        return st[-1]
