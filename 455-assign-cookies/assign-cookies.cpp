class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(),g.end());
        sort(s.begin(),s.end());
        int greedy = 0;
        int sizei = 0;
        while(greedy<g.size() && sizei<s.size()){
            if(s[sizei]>=g[greedy]){
                greedy++;
            }
            sizei++;
        }
        return greedy;
    }
};