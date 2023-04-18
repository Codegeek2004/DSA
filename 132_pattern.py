class Solution(object):
    def find132pattern(self, n):
        st=[]
        s=n[0]
        for i in range(len(n)):
            k=[s,n[i]]
            if(len(st)==0):
                st.append(k)
            else:
                while(len(st)!=0 and st[-1][1]<=n[i]):
                    st.pop()
                if(len(st)!=0 and st[-1][0]<n[i]):
                    return True
            s=min(s,n[i])
            k=[s,n[i]]
            st.append(k)
        return False
            


