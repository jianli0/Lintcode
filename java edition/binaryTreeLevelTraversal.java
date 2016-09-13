import java.util.*;

public class binaryTreeLevelTraversal{
    public static void main(String[] args){
        TreeNode t1 = new TreeNode(1);
        TreeNode t2 = new TreeNode(2);
        TreeNode t3 = new TreeNode(3);
        t1.left = t2;
        t1.right = t3;
        ArrayList<ArrayList<Integer>> res = levelOrder(t1);

        System.out.println(res);
    }

    public static ArrayList<ArrayList<Integer>> levelOrder(TreeNode root) {
        ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
        if(root == null){
            return res;
        }

        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);
        while(!q.isEmpty()){
            ArrayList<Integer> level = new ArrayList<Integer>();
            int size = q.size();
            for(int i = 0; i < size; i++){
                TreeNode n = q.poll();
                level.add(n.val);
                if(n.left != null){
                    q.add(n.left);
                }
                if(n.right != null){
                    q.add(n.right);
                }
            }
            res.add(level);
        }
        return res;
    }
}
