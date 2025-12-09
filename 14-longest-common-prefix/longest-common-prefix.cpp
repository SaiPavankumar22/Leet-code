class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        sort(strs.begin(),strs.end());
        string st = strs[0];
        string en = strs[strs.size()-1];
        string res ="";
        int mi = min(st.size(),en.size());
        for(int i =0;i<mi;i++){
            if(st[i]!=en[i]){
                return res;
            }
            res = res+st[i];
        }
        return res;
    }
};