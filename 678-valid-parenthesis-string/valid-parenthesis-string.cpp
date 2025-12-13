class Solution {
public:
    bool checkValidString(string s) {
        int mi_open = 0;
        int ma_open = 0;
        for(auto i:s){
            if(i=='('){
                mi_open++;
                ma_open++;
            }
            else if(i==')'){
                mi_open--;
                ma_open--;
            }
            else{
                mi_open--;
                ma_open++;
            }
            if(ma_open<0){
                return false;
            }
            mi_open = max(mi_open,0);
        }
        return mi_open == 0;
    }
};