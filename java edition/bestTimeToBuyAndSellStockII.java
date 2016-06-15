public class bestTimeToBuyAndSellStockII{
    public static void main(String[] args){
        int[] test = new int[]{2, 1, 2, 0, 1};
        System.out.println(maxProfit(test));
    }

    public static int maxProfit(int[] prices){
        if(prices == null || prices.length == 0){
            return 0;
        }

        int profit = 0;
        for(int i = 1; i < prices.length ; i++){
            if((prices[i] - prices[i - 1]) > 0){
                System.out.println("price[i]" + prices[i]);
                profit += (prices[i] - prices[i - 1]);
            }
        }
        return profit;
    }
}
