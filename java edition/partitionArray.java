public class partitionArray{
    public static void main(String[] args){
        int[] test = new int[]{3,2,2,1};
        int k = 2;
        System.out.println(partitionArray(test,k));
    }

    public static int partitionArray(int[] nums, int k) {
        if(nums == null || nums.length == 0){
            return 0;
        }

        int start = 0;
        int end = nums.length - 1;

        while(start <= end){
            while (nums[start] < k){
                start++;
            }
            while(nums[end] >= k){
                end--;
            }
           if (start <= end){
               int tmp = nums[start];
               nums[start] = nums[end];
               nums[end] = tmp;
               start++;
               end--;
           }
        }
        return start;
    }
}
