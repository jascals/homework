

```
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int diameterOfBinaryTree(TreeNode root) {
        if(root==null) return 0;
        
        int dis = maxDepthOfBinaryTree(root.left)+maxDepthOfBinaryTree(root.right);
        int disLeft = diameterOfBinaryTree(root.left);
        int disRight = diameterOfBinaryTree(root.right);
        
        return Math.max(Math.max(dis, disLeft), disRight);
    }
    
    public int maxDepthOfBinaryTree(TreeNode root){
        if(root==null) return 0;
        if(root.left==null&&root.right==null) return 1;
        int leftDepth = maxDepthOfBinaryTree(root.left);
        int rightDepth = maxDepthOfBinaryTree(root.right);
        return Math.max(leftDepth, rightDepth)+1;
    }
}
```
