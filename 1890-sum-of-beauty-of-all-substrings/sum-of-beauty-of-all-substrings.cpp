class Solution {
public:
    int beautySum(string s) {
        int res = 0;
        for (int i = 0; i < (int)s.size(); ++i) {
            unordered_map<char,int> freq;
            for (int j = i; j < (int)s.size(); ++j) {
                freq[s[j]]++;

                int ma = 0, mi = INT_MAX;
                for (const auto& kv : freq) {
                    ma = max(ma, kv.second);
                    mi = min(mi, kv.second);
                }
                res += (ma - mi);
            }
        }
        return res;
    }
};
