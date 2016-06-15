import java.util.*;
public class twoSumClosest{
    public static void main(String[] args){
        int[] test = new int[]{-1, 2, 1, -4};
        System.out.println(twoSumCloset(test, 4));
    }

    public static int twoSumCloset(int[] nums, int target){
        if(nums == null || nums.length == 0){
            return 0;
        }
        int left = 0;
        int right = nums.length - 1;

        Arrays.sort(nums);
        int diff = Integer.MAX_VALUE;

        while(left < right){
            if((nums[left] + nums[right]) > target){
                if((nums[left] + nums[right] - target) < diff){
                    diff = nums[left] + nums[right] - target;
                }
                right--;
            }else{
                if((target - nums[left] - nums[right]) < diff){
                    diff = target - nums[left] - nums[right];
                }
                left++;
            }
        }
        return diff;
    }
}
