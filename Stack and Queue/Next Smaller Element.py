 class Solution(object):
    def nextSmallerElement(self,a):
        n=len(a)
        st=[]
        list1=[0]*n
        for i in range(n-1,-1,-1):
            while st and st[-1]>=a[i]:
                st.pop()
            if not st:
                list1[i]=-1
            else:
                list1[i]=st[-1]
            st.append(a[i])
        return list1
