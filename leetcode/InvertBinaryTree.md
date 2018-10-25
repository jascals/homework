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
    public TreeNode invertTree(TreeNode root) {
        invert(root);
        return root;
    }
    
    private void invert(TreeNode node){
        if(node==null) return;
        
        // invert
        if(node.left!=null && node.right!=null){
            TreeNode temp = node.left;
            node.left = node.right;
            node.right = temp;
            invert(node.left);
            invert(node.right);
        }else if(node.left==null && node.right!=null){
            node.left = node.right;
            node.right=null;
            invert(node.left);
        }else if(node.left!=null && node.right==null){
            node.right = node.left;
            node.left=null;
            invert(node.right);
        }else{
            return;
        }
    }
}
```
