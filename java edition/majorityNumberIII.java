import java.util.*;

public class majorityNumberIII{
    public static void main(String[] args){
        ArrayList<Integer> a = new ArrayList<Integer>(Arrays.asList(3,1,2,3,2,3,3,4,4,4));
        System.out.println(majorityNumber(a,3));
    }

    public static int majorityNumber(ArrayList<Integer> nums, int k) {
        if(nums == null || nums.size() == 0){
            return -1;
        }

        HashMap<Integer,Integer> counters = new HashMap<Integer,Integer>();

        for(Integer i : nums){
            if(!counters.containsKey(i)){
                counters.put(i,1);
            }else if(counters.containsKey(i)){
                counters.put(i,counters.get(i) + 1);
            }

            if(counters.size() >= k){
                removeKey(counters);
            }
        }

        for(Integer i : counters.keySet()){
            counters.put(i,0);
        }

        for(Integer i : nums){
            if(counters.containsKey(i)){
                counters.put(i,counters.get(i) + 1);
            }
        }

        int maxKey = 0;
        int maxValue = Integer.MIN_VALUE;

        for(Integer i : counters.keySet()){
            if(counters.get(i) > maxValue){
                maxKey = i;
                maxValue = counters.get(i);
            }
        }
        return maxKey;
    }

    public static HashMap<Integer,Integer> removeKey(HashMap<Integer, Integer> a){
        Set<Integer> keys = a.keySet();
        ArrayList<Integer> removeList = new ArrayList<Integer>();
        for(Integer i : keys){
            a.put(i,a.get(i) - 1);
            if(a.get(i) == 0){
                removeList.add(i);
            }
        }

        for(Integer j : removeList){
            a.remove(j);
        }
        return a;
    }

}
