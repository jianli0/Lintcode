import java.util.*;
public class majorityNumberII{
    /**
     * @param nums: A list of integers
     * @return: The majority number that occurs more than 1/3
     */

    public static void main(String[] args){
        ArrayList<Integer> test = new ArrayList<Integer>();
        test.add(99);
        test.add(99);
        test.add(99);
        test.add(2);
        test.add(2);
        test.add(3);
        test.add(3);
        System.out.println(majorityNumber(test));
    }

    public static int majorityNumber(ArrayList<Integer> nums) {
        if(nums == null || nums.size() == 0){
            return 0;
        }
        HashMap<Integer,Integer> hm = new HashMap<Integer, Integer>();

        for(Integer i :nums){
            System.out.println("nums is " + i);
            if(hm.containsKey(i)){
                    hm.put(i, hm.get(i) + 1);
            }else if(hm.size() < 2){
                hm.put(i, 1);

            }else{
                List<Integer> removeList = new ArrayList<Integer>();
                for(Integer j : hm.keySet()){
                    hm.put(j, hm.get(j) - 1);
                    if(hm.get(j) == 0){
                        removeList.add(j);
                    }
                }

                for(Integer key : removeList){
                    hm.remove(key);
                }
            }
        }

        int maxNum = Integer.MIN_VALUE;
        int index = 0;
        for(Integer k : hm.keySet()){
            if(hm.get(k) > maxNum){
                maxNum = hm.get(k);
                index = k;
            }
        }
        return index;
    }
}

