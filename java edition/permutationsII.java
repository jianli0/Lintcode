import java.util.*;

class permutationsII{
    public static void main(String[] args){
        ArrayList<Integer> test = new ArrayList<Integer>();
        test.add(1);
        test.add(2);
        test.add(2);
        ArrayList<ArrayList<Integer>> result = permuteUnique(test);
        for(int i = 0; i < result.size(); i++){
            System.out.println(result.get(i));
        }
    }

    public static ArrayList<ArrayList<Integer>> permuteUnique(ArrayList<Integer> nums){
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        if(nums == null || nums.size() == 0){
            return result;
        }
        ArrayList<Integer> list = new ArrayList<Integer>();
        int[] visited = new int[nums.size()];

        Collections.sort(nums);
        helper(result, list, visited, nums);
        return result;
    }

    private static void helper(ArrayList<ArrayList<Integer>> result, ArrayList<Integer> list, int[] visited,
            ArrayList<Integer> nums){
        if(list.size() == nums.size()){
            result.add(new ArrayList<Integer>(list));
            return;
        }

        for(int i = 0; i < nums.size(); i++){
            if(visited[i] == 1 || (i > 0 && nums.get(i) == nums.get(i - 1) && visited[i - 1] == 0)){
                continue;
            }
            visited[i] = 1;
            list.add(nums.get(i));
            helper(result, list, visited, nums);
            list.remove(list.size() - 1);
            visited[i] = 0;
        }
    }
}
