class Solution(object):
    def nextGreaterElements(self,a):
        n=len(a)
        st=[]
        list1=[0]*n
        for i in range(2*n-1,-1,-1):
            val=a[i%n]
            while st and st[-1]<=val:
                st.pop()
            if i<n:
                if not st:
                    list1[i]=-1
                else:
                    list1[i]=st[-1]
            st.append(val)
        return list1
