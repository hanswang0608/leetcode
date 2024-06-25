struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    TreeNode* bstToGst(TreeNode* root) {
        dfs(root, 0);
        return root;
    }

    int dfs(TreeNode* root, int greater) {
        if (root == nullptr) {
            return 0;
        }
        int right = dfs(root->right, greater);
        int rootVal = root->val;
        root->val += right + greater;
        return dfs(root->left, root->val) + rootVal + right;
    }
};