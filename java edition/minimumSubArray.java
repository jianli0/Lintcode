import java.util.*;
public class minimumSubArray{
    public static void main(String[] args){
        ArrayList<Integer> test = new ArrayList<Integer>();
        test.add(1);
        test.add(-1);
        test.add(-2);
        test.add(1);
        System.out.println(minSubArray(test));
    }

    public static int minSubArray(ArrayList<Integer> nums) {
        int count = nums.size();
        if(nums.size() == 0 || nums == null){
            return 0;
        }

        ArrayList<Integer> newNums = new ArrayList<Integer>();
        for(Integer i : nums){
            newNums.add(-i);
        }

        int sum = 0;
        int max = Integer.MIN_VALUE;
        int minSum = 0;

        for(int i = 0; i < count; i++){
            System.out.println(newNums.get(i));
            sum += newNums.get(i);
            max = Math.max(max, sum - minSum);
            minSum = Math.min(minSum,sum);
        }
        return -max;
        // write your code
    }
}
