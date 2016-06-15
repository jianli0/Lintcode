public class bestTimeToBuyAndSellStock{
    public static void main(String[] args){
        int[] test = new int[]{3, 2, 3, 1, 2};
        System.out.println(maxProfit(test));
    }

    public static int maxProfit(int[] prices){
        if(prices == null || prices.length == 0){
            return 0;
        }

        int minSum = Integer.MAX_VALUE;
        int sum = 0;
        int max = Integer.MIN_VALUE;

        for(int i : prices){
            sum += i;
            minSum = (minSum > sum)? sum : minSum;
            max = ((i - minSum) > max )? (i - minSum): max;
        }
        return max;
    }
}
