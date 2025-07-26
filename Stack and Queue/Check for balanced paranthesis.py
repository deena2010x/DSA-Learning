class Solution(object):
    def isValid(self,s):
        st=[]
        dict1={')':'(','}':'{',']':'['}
        for i in s:
            if i in dict1.values():
                st.append(i)
            elif i in dict1:
                if not st or st[-1]!=dict1[i]:
                    return False
                st.pop()
        return not st
