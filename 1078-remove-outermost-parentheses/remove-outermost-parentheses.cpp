class Solution {
public:
    string removeOuterParentheses(string s) {
        string ch;
        int scale = 0;
        for(auto a: s){
            if(a=='('){
                if(scale >0){
                    ch+=a;
                }
                scale++;
            }
            else if(a==')'){
                scale--;
                if(scale>0){
                    ch+=a;
                }
            }
        }
        return ch;
    }
};