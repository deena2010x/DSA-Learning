class Solution(object):
    def postfixToInfix(self,s):
        n=len(s)
        st=[]
        for i in range(n):
            if s[i].isalnum():
                st.append(s[i])
            else:
                a=st.pop()
                b=st.pop()
                st.append('('+b+s[i]+a+')')
        return st[-1]
