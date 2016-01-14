import java.util.Arrays;

public class kClosestNumbersInSortedArray{
    public static void main(String[] args){
        // System.out.println(Arrays.toString(kClosestNumbers(new int[]{1,2,3}, 2, 3)));
        // System.out.println(Arrays.toString(kClosestNumbers(new int[]{1,4,6,8}, 3, 3)));
        // debuging
        System.out.println(Arrays.toString(kClosestNumbers(new int[]{1,4,8,12,16,28,38}, 12, 4)));
        // System.out.println(findPos(new int[]{1,4,8,12,16,28,38}, 12, 'l'));
        // System.out.println(findPos(new int[]{1,4,8,12,16,28,38}, 12, 'r'));
    }

    public static int[] kClosestNumbers(int[] A, int target, int k){
        int[] res;
        res = new int[k];
        if(k > A.length){
            return res;
        }

        int count = 0;
        int left = findPos(A,target,'l');
        int right = findPos(A,target,'r');
        if(left == right){
            right++;
        }

        while(left >= 0 && right <= A.length - 1){
            if(count < k){
                if(Math.abs((A[left] - target)) <= Math.abs(A[right] - target)){
                    res[count++] = A[left--];
                }else{
                    res[count++] = A[right++];
                }
            }else{
                break;
            }
        }

        while(count < k){
            if (left >= 0){
                res[count++] = A[left--];
            }else if(right < A.length){
                res[count++] = A[right++];
            }
        }
        return res;
    }

    public static int findPos(int[] A, int target, char d){
        if(A == null || A.length == 0){
            return -1;
        }
        int start = 0;
        int end = A.length - 1;

        while (start + 1 < end){
            int mid = (start + end) / 2;
            if(d == 'l'){
                if (A[mid] < target){
                    start = mid;
                }else{
                    end = mid;
                }
            }else if (d == 'r'){
                if (A[mid] <= target){
                    start = mid;
                }else{
                    end = mid;
                }
            }

        }

        if(d == 'l'){
            if(A[start] == target){
                return start;
            }else if (A[end] == target){
                return end;
            }else{
                return start;
            }
        }else if(d == 'r'){
            if(A[end] == target){
                return end;
            }else if (A[start] == target){
                return start;
            }else{
                return end;
            }
        }
        return -1;
    }
}
