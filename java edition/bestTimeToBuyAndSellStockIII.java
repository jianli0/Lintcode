public class bestTimeToBuyAndSellStockIII{
    public static void main(String[] args){
        int[] test = new int[]{4, 4, 6, 1, 1, 4, 2, 5};
        System.out.println(maxProfit(test));
    }

    public static int maxProfit(int[] prices){
        if(prices == null || prices.length == 0){
            return 0;
        }
        int count = prices.length;
        int[] left = new int[count];
        int[] right = new int[count];

        int leftMin = prices[0];
        left[0] = 0;
        for(int i = 1 ; i < count; i++){
            left[i] = ((prices[i] - leftMin) > left[i - 1]) ? (prices[i] - leftMin) : left[i - 1];
            leftMin = Math.min(leftMin,prices[i]);
        }

        int rightMax = prices[count - 1];
        right[count - 1] = 0;
        for(int i = count - 2 ; i >= 0 ; i--){
            right[i] = ((rightMax - prices[i]) > right[i + 1]) ? (rightMax - prices[i]) : right[i + 1];
            rightMax = Math.max(rightMax,prices[i]);
        }

        int profit = 0;
        for(int i = 0 ; i < count ; i++){
            System.out.println(left[i] +"\t"+ i + "\t" + right[i]);
            profit = ((left[i] + right[i]) > profit) ? (left[i] + right[i]) : profit;
        }
        return profit;
    }
}
