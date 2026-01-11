class Solution {
public:
    unordered_set<string> res;
    void dfs(string part, string tile) {
        if (!part.empty()) {
            res.insert(part);
        }
        for (int i = 0; i < tile.size(); i++) {
            dfs(part + tile[i],
                tile.substr(0, i) + tile.substr(i + 1));
        }
    }
    int numTilePossibilities(string tiles) {
        dfs("", tiles);
        return res.size();
    }
};
