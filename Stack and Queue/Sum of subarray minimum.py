class Solution(object):
    def sumSubarrayMins(self,a):
        def pse(a):
            n=len(a)
            st=[]
            list1=[0]*n
            for i in range(n):
                while st and a[st[-1]]>=a[i]:
                    st.pop()
                if st:
                    list1[i]=st[-1]
                else:
                    list1[i]=-1
                st.append(i)
            return list1
        def nse(a):
            n=len(a)
            st=[]
            list1=[0]*n
            for i in range(n-1,-1,-1):
                while st and a[st[-1]]>a[i]:
                    st.pop()
                if st:
                    list1[i]=st[-1]
                else:
                    list1[i]=n
                st.append(i)
            return list1
        n=len(a)
        mod=10**9+7
        prev=pse(a)
        next=nse(a)
        total=0
        for i in range(n):
            left=i-prev[i]
            right=next[i]-i
            total+=(a[i]*left*right)%mod
            total%=mod
        return total
