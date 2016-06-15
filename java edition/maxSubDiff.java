import java.util.*;

public class maxSubDiff{
    public static void main(String[] args){
        int[] test = new int[]{1, 2, -3, 1};
        System.out.println(maxDiffSubArrays(test));
    }

    public static int maxDiffSubArrays(int[] nums){
        int count = nums.length;
        if(nums == null || count == 0){
            return 0;
        }

        int[] copy = new int[count];

        int[] left= new int[count];
        int[] leftCopy = new int[count];
        int[] right= new int[count];
        int[] rightCopy = new int[count];

        for(int i = 0; i < count; i++){
            copy[i] = -nums[i];
        }

        // left
        int sum = 0;
        int minSum = 0;
        int max = Integer.MIN_VALUE;
        for(int i = 0; i < count; i++){
            sum += nums[i];
            max = Math.max(max,(sum - minSum));
            minSum = Math.min(minSum, sum);
            left[i] = max;
        }

        //leftCopy
        sum = 0;
        minSum = 0;
        max = Integer.MIN_VALUE;
        for(int i = 0; i < count; i++){
            // System.out.print(sum + "\t" + minSum + "\t" + max + "\n");
            sum += copy[i];
            max = Math.max(max,(sum - minSum));
            minSum = Math.min(minSum, sum);
            leftCopy[i] = max;
        }

        //right
        sum = 0;
        minSum = 0;
        max = Integer.MIN_VALUE;
        for(int i = count - 1; i >= 0 ; i--){
            sum += nums[i];
            max = Math.max(max,(sum - minSum));
            minSum = Math.min(minSum, sum);
            right[i] = max;
        }

        //rightCopy
        sum = 0;
        minSum = 0;
        max = Integer.MIN_VALUE;
        for(int i = count - 1; i >= 0; i--){
            sum += copy[i];
            max = Math.max(max,(sum - minSum));
            minSum = Math.min(minSum, sum);
            rightCopy[i] = max;
        }

        max = Integer.MIN_VALUE;

        // System.out.println(Arrays.toString(left));
        // System.out.println(Arrays.toString(leftCopy));
        // System.out.println(Arrays.toString(right));
        // System.out.println(Arrays.toString(rightCopy));

        for(int i = 0; i < count -1; i++){
            max = Math.max(max, Math.max(Math.abs(leftCopy[i] + right[i + 1]),
                    Math.abs(left[i] + rightCopy[i + 1])));
        }
        return max;
    }
}
