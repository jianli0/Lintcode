import java.util.*;

public class binaryTreePathSum{
    public static void main(String[] args){
        TreeNode t1 = new TreeNode(1);
        TreeNode t2 = new TreeNode(2);
        TreeNode t3 = new TreeNode(4);
        TreeNode t4 = new TreeNode(2);
        TreeNode t5 = new TreeNode(3);
        t1.left = t2;
        t1.right = t3;
        t2.left = t4;
        t2.right = t5;

        List<List<Integer>> res = binaryTreePathSum(t1 , 5);
        // System.out.println(res.size());

        // for(int i = 0 ; i < res.size() - 1; i++){
            // for(int j = 0 ; j < res.get(i).size() - 1; j++){
                // // System.out.print("hello");
                // // System.out.print(res.get(i).get(j));
            // }
            // System.out.println();
        // }
    }

    public static List<List<Integer>> binaryTreePathSum(TreeNode root, int target) {
        List<List<Integer>> result = new ArrayList<>();
        if(root == null){
            return result;
        }

        ArrayList<Integer> path = new ArrayList<Integer>();
        path.add(root.val);
        helper(root, root.val, path, target, result);
        return result;
    }

    public static void helper(TreeNode root, int sum, ArrayList<Integer> path, int target,List<List<Integer>> result){
        // debug
        // System.out.println("root value is");
        // System.out.println(root.val);
        // System.out.println("sum value is");
        // System.out.println(sum);

        if(root.left == null && root.right == null){
            if(sum == target){
                result.add(new ArrayList<Integer>(path));
            }
            return;
        }

        if(root.left != null){
            path.add(root.left.val);
            helper(root.left, sum + root.left.val, path, target, result);
            path.remove(path.size() - 1);
        }

        if(root.right!= null){
            path.add(root.right.val);
            helper(root.right, sum + root.right.val, path, target, result);
            path.remove(path.size() - 1);
        }
    }
}

