class binaryTreeSerial{
    // public static void main(String[] args){
    // }


    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        if(root == null){
            return null;
        }

        serializeHelper(root, sb);
        // write your code here
    }

    public void serializeHelper(TreeNode root, StringBuilder sb){

    }

    public TreeNode deserialize(String data) {
        // write your code here
    }
}
