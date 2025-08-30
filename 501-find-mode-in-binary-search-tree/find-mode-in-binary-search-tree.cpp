/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> findMode(TreeNode* root) {
        if (!root) {
            return {};
        }
        
        vector<int> lis;
        
        function<void(TreeNode*)> recur = [&](TreeNode* node) {
            if (!node) return;
            lis.push_back(node->val);
            recur(node->left);
            recur(node->right);
        };
        
        recur(root);
        
        unordered_map<int, int> count;
        for (int val : lis) {
            count[val]++;
        }
        
        int maxFreq = 0;
        for (const auto& pair : count) {
            maxFreq = max(maxFreq, pair.second);
        }
        
        vector<int> result;
        for (const auto& pair : count) {
            if (pair.second == maxFreq) {
                result.push_back(pair.first);
            }
        }
        
        return result;
    }
};