public class jumpGame{
    public static void main(String[] args){
        int[] test = new int[]{2, 3, 1, 1, 4};
        int[] test1 = new int[]{3, 2, 1, 0, 4};

        System.out.println(canJump(test));
        System.out.println(canJump(test1));
    }

    public static boolean canJump(int[] A) {
        if(A == null || A.length == 0){
            return false;
        }

        boolean[] f = new boolean[A.length];
        f[0] = true;

        for(int i = 1; i < A.length; i++){
            for(int j = 0; j < i; j++){
                if(f[j] == true && A[j] + j >= i){
                    f[i] = true;
                    break;
                }
            }
        }
        return f[A.length - 1];
    }
}

