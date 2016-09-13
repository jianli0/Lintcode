public class jumpGameII{
    public static void main(String[] args){
        int[] test = new int[]{2, 3, 1, 1, 4};
        System.out.println(jump(test));
    }

    public static int jump(int[] A) {
        if(A == null || A.length == 0){
            return -1;
        }
        int[] f = new int[A.length];
        f[0] = 0;
        for(int i = 1; i < A.length; i++){
            f[i] = Integer.MAX_VALUE;
        }

        for(int i = 1; i < A.length; i++){
            for(int j = 0; j < i; j++){
                if(f[j] != Integer.MAX_VALUE && A[j] + j >= i){
                    f[i] = Math.min(f[i], f[j] + 1);
                }
            }
        }
        return f[A.length - 1];
    }
}

