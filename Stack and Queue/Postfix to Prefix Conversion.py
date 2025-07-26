class Solution(object):
    def postfixToPrefix(self,s):
        n=len(s)
        st=[]
        for i in range(n):
            if s[i].isalnum():
                st.append(s[i])
            else:
                a=st.pop()
                b=st.pop()
                st.append(s[i]+a+b)
        return st[-1]
