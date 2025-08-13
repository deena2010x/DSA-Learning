class Solution(object):
    def parseBoolExpr(self,s):
        def f(i):
            if s[i]=='t':
                return True,i+1
            if s[i]=='f':
                return False,i+1
            op=s[i]
            i+=2
            values=[]
            while s[i]!=')':
                val,i=f(i)
                values.append(val)
                if s[i]==',':
                    i+=1
            i+=1
            if op=='!':
                return (not values[0]),i
            elif op=='&':
                res=True
                for v in values:
                    res=res and v
                return res,i
            else:
                res=False
                for v in values:
                    res=res or v
                return res,i
        result,i=f(0)
        return result
