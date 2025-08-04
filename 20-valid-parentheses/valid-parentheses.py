class Solution:
    def isValid(self, s: str) -> bool:
        k = []
        for i in s:
            if(i == "("):
                k.append(")")
            elif(i == "["):
                k.append("]")
            elif(i == "{"):
                k.append("}")
            else:
                if( not k or k.pop()!=i):
                    return False
        return len(k) == 0

