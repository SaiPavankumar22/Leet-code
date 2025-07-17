class Solution {
public:
    int lengthOfLastWord(string s) {
        vector<string> g;
        string word;
        for (char c : s) {
            if (c == ' ') {
                g.push_back(word);
                word = "";
            } else {
                word += c;
            }
        }
        g.push_back(word); 

        int i = g.size() - 1;
        while (i >= 0 && g[i] == "") {
            i--;
        }
        if (i >= 0) {
            return g[i].length();
        }
        return 0;
    }
};