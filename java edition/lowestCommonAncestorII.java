public class lowestCommonAncestorII{
    public static void main(String[] args){
        System.out.println();
    }

    // not efficient
    public static ParentTreeNode lowestCommonAncestorII(ParentTreeNode root,
                                                 ParentTreeNode A,
                                                 ParentTreeNode B) {
        if(root == null){
            return null;
        }
        if(A == null || B == null){
            return root;
        }

        if(A == B){
            return A;
        }else if(isAncestor(A,B)){
            return B;
        }else if(isAncestor(B,A)){
            return A;
        }else{
            return helper(root, A.parent, B.parent);
        }

    }

    private static ParentTreeNode helper(ParentTreeNode root, ParentTreeNode A, ParentTreeNode B){
        if(root == null){
            return null;
        }
        if(A == null || B == null){
            return root;
        }

        if(A == B){
            return A;
        }else if(A.parent == B){
            return B;
        }else if(B.parent == A){
            return A;
        }else{
            return helper(root, A.parent, B.parent);
        }
    }

    private static boolean isAncestor(ParentTreeNode A, ParentTreeNode B){
        ParentTreeNode cur = A;
        while(cur != null){
            if(cur == B){
                return true;
            }else{
                cur = cur.parent;
            }
        }
        return false;
    }
}
