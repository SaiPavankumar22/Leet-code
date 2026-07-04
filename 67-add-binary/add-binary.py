class Solution:
    def addBinary(self, a: str, b: str) -> str:
        la= len(a)-1
        lb = len(b)-1
        carry =0
        sum =0
        res = ""
        while(la>=0 or lb>=0 or carry==1):
            sum =0
            if(la>=0):
                sum+=int(a[la])
                la-=1
            if(lb>=0):
                sum+=int(b[lb])
                lb-=1
            if(carry==1):
                carry =0
                sum+=1
            if(sum ==1):
                res= "1"+res
            elif(sum==2):
                res="0"+res
                carry =1
            elif(sum ==0):
                res="0"+res
            else:
                res="1"+res
                carry =1
        return res