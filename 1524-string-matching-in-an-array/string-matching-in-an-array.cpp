class Solution {
public:
    vector<string> stringMatching(vector<string>& words) {
        set<string> res;
        for(int i = 0; i < words.size(); i++){
            for(int j = i + 1; j < words.size(); j++){
                if(words[i] == words[j]){
                    continue;
                }
                else if(words[i].find(words[j]) != string::npos){
                    res.insert(words[j]);
                }
                else if(words[j].find(words[i]) != string::npos){
                    res.insert(words[i]);
                }
            }
        }
        return vector<string>(res.begin(), res.end());
    }
};