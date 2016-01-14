public class closetNumInSortedArray{
    public static void main(String[] args){
        System.out.println(closestNumber(new int[]{ 1,2,3 },2));
        System.out.println(closestNumber(new int[]{ 1,4,6 },3));
        System.out.println(closestNumber(new int[]{ 1,4,6 },5));
        System.out.println(closestNumber(new int[]{ 1,3,3,4 },2));
    }
    public static int closestNumber(int[] A, int target){
        if(A == null || A.length == 0){
            return -1;
        }

        int start = 0;
        int end = A.length - 1;
        while (start + 1 < end){
            int mid = (start + end) / 2;
            if (A[mid] == target){
            return mid;
            }else if (A[mid] < target){
                start = mid;
            }else{
                end = mid;
            }
        }

        if(Math.abs(target - A[start]) <= Math.abs(target - A[end])){
            return start;
        }else{
            return end;
        }
    }
}
