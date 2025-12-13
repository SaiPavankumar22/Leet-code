class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        twenty =0
        for i in bills:
            if(i==5):
                fives+=1
            elif(i==10):
                if(fives>0):
                    tens+=1
                    fives-=1
                else:
                    return False
            else:
                if(fives>0 and tens>0):
                    fives-=1
                    tens-=1
                    twenty+=1
                elif(fives>=3):
                    fives-=3
                    twenty+=1
                else:
                    return False
        return True
