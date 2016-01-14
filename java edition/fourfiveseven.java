public class fourfiveseven{
    public static void main(String[] args){
        TreeNode a1 = new TreeNode(1);
        TreeNode a2 = new TreeNode(2);
        TreeNode a3 = new TreeNode(3);
        a1.left = a2;
        a1.right = a3;

        System.out.println(maxPathSum2(a1));
        System.out.println(maxPathSum2(null));
    }
    public static int maxPathSum2(TreeNode root){
        if(root == null){
        return 0;
        }
        int left = maxPathSum2(root.left);
        int right = maxPathSum2(root.right);
        return root.val + Math.max(0, Math.max(left, right));
    }
}
