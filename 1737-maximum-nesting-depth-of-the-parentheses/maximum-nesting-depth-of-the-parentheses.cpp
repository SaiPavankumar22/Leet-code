class Solution {
public:
    int maxDepth(string s) {
        int a =0;
        int res =0;
        for(auto i: s){
            if(i=='('){
                a++;
            }
            else if(i==')'){
                a--;
            }
            res = max(res,a);
        }
        return res;
    }
};