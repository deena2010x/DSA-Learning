class solution(object):
    def infixToPrefix(self,s):
        def infixToPostfix(self,s):
            def priority(op):
                if op=='+' or op=='-':
                    return 1
                if op=='*' or op=='/':
                    return 2
                if op=='^':
                    return 3
                return 0
            n=len(s)
            st=[]
            s1=''
            for i in range(n):
                if s[i].isalnum():
                    s1+=s[i]
                elif s[i]=='(':
                    st.append(s[i])
                elif s[i]==')':
                    while st and st[-1]!='(':
                        s1+=st.pop()
                    if st and st[-1]=='(':
                        st.pop()
                else:
                    while st and priority(s[i])<=priority(st[-1]):
                        s1+=st.pop()
                    st.append(s[i])
            while st:
                s1+=st.pop()
            return s1
        s=s[::-1]
        s=' '.join(['(' if i==')' else ')' if i=='(' else i for i in s])
        return infixToPostfix(s)[::-1]
