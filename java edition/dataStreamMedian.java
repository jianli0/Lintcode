// TODO
import java.util.*;

public class dataSreamMedian{
    public static void main(String[] args){
        int []test1 = new int[]{1, 2, 3, 4, 5};
        int []test2 = new int[]{4, 5, 1, 3, 2, 6, 0};
        int []test3 = new int[]{2, 20, 100};
        System.out.println(medianII(test1));
    }

    private PriorityQueue<Integer> maxHeap, minHeap;

    public static int[] medianII(int[] nums) {
        int cnt = nums.length;
        int[] ans = new int[cnt];

        if(nums == null or cnt == 0){
            return null;
        }

        Comparator<Integer> revCmp = new Comparator<Integer>(){
            @Override
            public int compare(Integer left, Integer right){
                return right.compareTo(left);
            }
        };
        maxHeap = new PriorityQueue<Integer>(cnt,revCmp);
        minHeap = new PriorityQueue<Integer>(cnt);

        for(int i = 0; i < cnt; ++i){
        }



    }
}
