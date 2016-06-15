import java.util.*;
public class maximumSubarrayII{
    public static void main(String[] args){
        ArrayList<Integer> test = new ArrayList<Integer>();
        test.add(1);
        test.add(3);
        test.add(-1);
        test.add(2);
        test.add(-1);
        test.add(2);

         System.out.println(maxTwoSubArrays(test));

         ArrayList<Integer> test1 = new ArrayList<Integer>();
         test1.add(-1);
         test1.add(-1);
         System.out.println(maxTwoSubArrays(test1));
     }

        public static int maxTwoSubArrays(ArrayList<Integer> nums) {
        // write your code
        int count = nums.size();
        if(nums == null || count == 0){
            return 0;
        }

        int[] left = new int[count];
        int[] right = new int[count];

        int max = Integer.MIN_VALUE;
        int minSum = 0;
        int sum = 0;

        for(int i = 0; i < count; i++){
            sum += nums.get(i);
            max = Math.max(max,(sum - minSum));
            minSum = Math.min(minSum, sum);
            left[i] = max;
        }

        max = Integer.MIN_VALUE;
        minSum = 0;
        sum = 0;

        for(int i = count -1; i >= 0; i--){
            sum += nums.get(i);
            max = Math.max(max,(sum - minSum));
            minSum = Math.min(minSum, sum);
            right[i] = max;
        }

        max = Integer.MIN_VALUE;
        for(int i = 0; i < count - 1; i++){
            max = Math.max(max, (right[i + 1] + left[i]));
        }
        System.out.print(Arrays.toString(left));
        System.out.print(Arrays.toString(right));

        return Math.max(max,right[0]);
    }
}
