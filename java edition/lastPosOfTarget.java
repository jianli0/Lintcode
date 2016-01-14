public class lastPosOfTarget{
    public static void main(String[] args){
        System.out.println(lastPosition(new int[]{1,2,2,4,5,5},2));
        System.out.println(lastPosition(new int[]{1,2,2,4,5,5},5));
        System.out.println(lastPosition(new int[]{1,2,2,4,5,5},6));
    }
    public static int lastPosition(int[] A, int target){
        if(A == null || A.length == 0){
            return -1;
        }

        int start = 0;
        int end = A.length - 1;
        while (start + 1 < end){
            int mid = (start + end) / 2;
            if (A[mid] <= target){
                start = mid;
            }else{
                end = mid;
            }
        }

        if(A[end] == target){
            return end;
        }else if (A[start] == target){
            return start;
        }else{
            return -1;
        }
    }
}
