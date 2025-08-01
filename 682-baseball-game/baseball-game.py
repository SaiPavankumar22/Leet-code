class Solution:
    def calPoints(self, operations: List[str]) -> int:
        k = []
        for i in range(0,len(operations)):
            if(operations[i] == "C"):
                k.pop()
            elif(operations[i] == "D"):
                k.append(int(k[-1])*2)
            elif(operations[i] == "+"):
                k.append(int(k[-1])+int(k[-2]))
            else:
                k.append(int(operations[i]))
        s = sum(k)
        return s
