public class maximumSubarray{
    public static void main(String[] args){
        int []test = new int[]{-2,2,-3,4,-1,2,1,-5,3};
        int []test2 = new int[]{1,2,3,4,5,6,7,100,200,1000};
        System.out.println(maxSubArray(test));
    }
    public static int maxSubArray(int[] nums){
        if(nums == null || nums.length == 0){
            return -1;
        }
        int count = nums.length;
        int[] prefix = new int[count];

        int sum = 0;
        for(int i = 0; i < count; i++){
            sum += nums[i];
            prefix[i] = sum;
        }

        int minPrefix = prefix[0];
        int maxSub = prefix[0];
        for(int j = 1; j < count; j++){
            if((prefix[j] - minPrefix) > maxSub){
                maxSub = prefix[j] - minPrefix;
            }
            if(prefix[j] < minPrefix){
                minPrefix = prefix[j];
            }
        }
        return (maxSub > sum)? maxSub:sum;
    }
}
