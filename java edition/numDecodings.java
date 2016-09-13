public class numDecodings{
    /**
     * @param s a string,  encoded message
     * @return an integer, the number of ways decoding
     */
    public static void main(String[] args){
        System.out.println(numDecodings("100010"));
    }

    public static int numDecodings(String s){
        if(s == null || s.length() == 0){
            return 0;
        }

        int[] nums = new int[s.length() + 1];
        nums[0] = 1;
        nums[1] = s.charAt(0) != '0' ? 1 : 0;

        for(int i = 2; i < s.length() + 1; i++){
            if(s.charAt(i - 1) != '0'){
                nums[i] = nums[i - 1];
            }
            int val = (s.charAt(i - 2) - '0') * 10 + (s.charAt(i - 1) - '0');
            if(val >= 10 && val <= 26){
                nums[i] += nums[i - 2];
            }
        }
        return nums[s.length()];
    }
}
