import java.util.*;
public class interleavePosAndNeg{
    public static void main(String[] args){
        int[] test = new int[]{-1, -2, -3, 4, 5, 6};
        System.out.println(Arrays.toString(rerange(test)));
    }

    public static int[] rerange(int[] A){
        if(A == null || A.length == 0){
            return A;
        }

        int posNum = 0;

        for(Integer i : A){
            if (i > 0){
                posNum += 1;
            }
        }

        int pPos = 0;
        int pNeg = 1;

        if(posNum * 2 > A.length){
            pPos = 1;
            pNeg = 0;
        }

        while(pPos < A.length && pNeg < A.length){
            while(pPos < A.length && A[pPos] > 0){
                pPos += 2;
            }
            while(pNeg < A.length && A[pNeg] < 0){
                pNeg += 2;
            }

            if(pPos < A.length && pNeg < A.length){
                int tmp = A[pPos];
                A[pPos] = A[pNeg];
                A[pNeg] = tmp;
            }
        }
        return A;

    }
}
