class Solution(object):
    def subArrayRanges(self,a):
        def pse(a):
            n=len(a)
            st=[]
            list1=[0]*n
            for i in range(n):
                while st and a[st[-1]]>a[i]:
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
                while st and a[st[-1]]>=a[i]:
                    st.pop()
                if st:
                    list1[i]=st[-1]
                else:
                    list1[i]=n
                st.append(i)
            return list1
        def pge(a):
            n=len(a)
            st=[]
            list1=[0]*n
            for i in range(n):
                while st and a[st[-1]]<a[i]:
                    st.pop()
                if st:
                    list1[i]=st[-1]
                else:
                    list1[i]=-1
                st.append(i)
            return list1
        def nge(a):
            n=len(a)
            st=[]
            list1=[0]*n
            for i in range(n-1,-1,-1):
                while st and a[st[-1]]<=a[i]:
                    st.pop()
                if st:
                    list1[i]=st[-1]
                else:
                    list1[i]=n
                st.append(i)
            return list1
        n=len(a)
        prev_min=pse(a)
        next_min=nse(a)
        prev_max=pge(a)
        next_max=nge(a)
        total_min=0
        total_max=0
        for i in range(n):
            left_min=i-prev_min[i]
            right_min=next_min[i]-i
            total_min+=nums[i]*left_min*right_min
            left_max=i-prev_max[i]
            right_max=next_max[i]-i
            total_max+=nums[i]*left_max*right_max
            total=total_max-total_min
        return total
