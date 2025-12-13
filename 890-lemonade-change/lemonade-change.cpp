class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int fives = 0;
        int tens = 0;
        int twenty = 0;
        for(auto i:bills){
            if(i==5){
                fives++;
            }
            else if(i==10){
                if(fives>0){
                    fives--;
                    tens++;
                    }
                else{
                    return false;
                }
            }
            else{
                if(fives>0 && tens>0){
                    fives--;
                    tens--;
                    twenty++;
                }
                else if(fives>=3){
                    fives = fives -3;
                }
                else{
                    return false;
                }
            }
        
        }
        return true;
    }
};